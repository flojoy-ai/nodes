from skimage.registration import phase_cross_correlation
from skimage.registration._masked_phase_cross_correlation import cross_correlate_masked
from skimage.draw import ellipse
import skimage.filters as filters
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion, disk
from skimage.feature import blob_log
from scipy.ndimage import gaussian_filter, laplace, shift
from warnings import catch_warnings, simplefilter

import scipy.fft
from scipy.fft import _pocketfft
from os import cpu_count
from math import floor, sqrt, acos
import numpy as np


class customFFTBackend:
    """
    Pocket fft is usually a lot faster for this type of registration.
    This class simply provides the implementation of the uarray protocol
    to the scipy context manager.
    """

    __ua_domain__ = "numpy.scipy.fft"

    @staticmethod
    def __ua_function__(method, args, kwargs):
        fn = getattr(_pocketfft, method.__name__, None)

        if fn is None:
            return NotImplemented
        workers = kwargs.pop("workers", cpu_count())
        return fn(*args, workers=workers, **kwargs)


def autocenter(im, mask=None):
    im = np.array(im, copy=True, dtype=float)
    im -= im.min()
    if mask is None:
        mask = np.ones_like(im, dtype=bool)
        weights = im
    else:
        weights = im * mask.astype(im.dtype)
    rr, cc = np.indices(im.shape)
    r_ = int(np.average(rr, weights=weights))
    c_ = int(np.average(cc, weights=weights))
    # Determine the smallest center -> side distance, and crop around that
    # 1. Some images are not centered, and so there's a lot
    # of image area that cannot be used for registration.
    # 2. radial inversion becomes simple inversion of dimensions
    side_length = floor(min([r_, abs(r_ - im.shape[0]), c_, abs(c_ - im.shape[1])]))
    rs = slice(r_ - side_length, r_ + side_length)
    cs = slice(c_ - side_length, c_ + side_length)
    im = im[rs, cs]
    mask = mask[rs, cs]

    # Certain images display a gradient in the overall intensity
    # For this purpose, we normalize the intensity by some "background",
    # i.e. very blurred diffraction pattern
    with catch_warnings():
        simplefilter("ignore", category=RuntimeWarning)
        im /= gaussian_filter(input=im, sigma=min(im.shape) / 25, truncate=2)
    im = np.nan_to_num(im, copy=False)

    # The comparison between Friedel pairs from [1] is generalized to
    # any inversion symmetry.
    im_i = im[::-1, ::-1]
    mask_i = mask[::-1, ::-1]

    # masked normalized cross-correlation is extremely expensive
    # we therefore downsample large images for essentially identical result
    # but ~4x decrease in processing time
    downsampling = 1
    if min(im.shape) > 1024:
        downsampling = 2

    with scipy.fft.set_backend(customFFTBackend):
        shift, *_ = phase_cross_correlation(
            reference_image=im[::downsampling, ::downsampling],
            moving_image=im_i[::downsampling, ::downsampling],
            reference_mask=mask[::downsampling, ::downsampling],
            moving_mask=mask_i[::downsampling, ::downsampling],
            return_error="always",
        )
    # Because images were downsampled, the correction
    # factor to the rough center should be increased from the measured shift
    correction = shift * downsampling

    return np.array([r_, c_]) + correction / 2


class UnionFind:

    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def add(self, object, weight):
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = weight

    def __contains__(self, object):
        return object in self.parents

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            assert False
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.parents[r] = heaviest


class Persistence:
    def __init__(self, im):
        self.image = im
        self.calculate()

    def calculate(self):
        h, w = self.image.shape

        # Get indices orderd by value from high to low
        indices = [(i, j) for i in range(h) for j in range(w)]
        indices.sort(key=lambda p: self.get(p), reverse=True)

        # Maintains the growing sets
        self.uf = UnionFind()

        self._groups0 = {}

        # Process pixels from high to low
        for i, p in enumerate(indices):
            v = self.get(p)
            ni = [self.uf[q] for q in self.iter_neighbors(p, w, h) if q in self.uf]
            nc = sorted([(self.get_comp_birth(q), q) for q in set(ni)], reverse=True)

            if i == 0:
                self._groups0[p] = (v, v, None)

            self.uf.add(p, -i)

            if len(nc) > 0:
                oldp = nc[0][1]
                self.uf.union(oldp, p)

                # Merge all others with oldp
                for bl, q in nc[1:]:
                    if self.uf[q] not in self._groups0:
                        # print(i, ": Merge", uf[q], "with", oldp, "via", p)
                        self._groups0[self.uf[q]] = (bl, bl - v, p)
                    self.uf.union(oldp, q)

        self._groups0 = [
            (k, self._groups0[k][0], self._groups0[k][1], self._groups0[k][2])
            for k in self._groups0
        ]
        self._groups0.sort(key=lambda g: g[2], reverse=True)
        self.persistence = self._groups0

    def get_comp_birth(self, p):
        return self.get(self.uf[p])

    def get(self, p):
        return self.image[p[0]][p[1]]

    def iter_neighbors(self, p, w, h):
        y, x = p

        # 8-neighborship
        neigh = [(y + j, x + i) for i in [-1, 0, 1] for j in [-1, 0, 1]]
        # 4-neighborship
        # neigh = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

        for j, i in neigh:
            if j < 0 or j >= h:
                continue
            if i < 0 or i >= w:
                continue
            if j == y and i == x:
                continue
            yield j, i


if __name__ == "__main__":
    from skued import diffread
    import matplotlib.pyplot as plt

    # from skimage import data
    # from skimage.color import rgb2gray
    # from scipy import ndimage
    # from scipy import spatial
    # from scipy.signal import fftconvolve
    from itertools import combinations

    # from skimage.io import imsave

    # image = data.hubble_deep_field()[0:500, 0:500]
    # image = rgb2gray(image)
    # k = 1.41
    # sigma = 1.0
    # def LoG(sigma): # first define the laplacian of a gaussian filter
    #     #window size
    #     n = np.ceil(sigma*6)
    #     y,x = np.ogrid[-n//2:n//2+1,-n//2:n//2+1]
    #     y_filter = np.exp(-(y*y/(2.*sigma*sigma)))
    #     x_filter = np.exp(-(x*x/(2.*sigma*sigma)))
    #     final_filter = (-(2*sigma**2) + (x*x + y*y) ) *  (x_filter*y_filter) * (1/(2*np.pi*sigma**4))
    #     return final_filter

    # def LoG_convolve(img): # now convolve the image with the filters
    #     log_images = [] #to store responses
    #     for i in range(0,9):
    #         y = np.power(k,i)
    #         sigma_1 = sigma*y #sigma
    #         filter_log = LoG(sigma_1) #filter generation
    #         print(img.shape)
    #         image = fftconvolve(img, filter_log, mode='same')#cv2.filter2D(img,-1,filter_log) # convolving image
    #         # image = np.pad(image,((1,1),(1,1)),'constant') #padding
    #         image = np.square(image) # squaring the response
    #         print(image.shape)
    #         log_images.append(image)
    #     log_image_np = np.array([i for i in log_images]) # storing the #in numpy array
    #     return log_image_np

    # log_image_np = LoG_convolve(image)

    # #provided in scipy doucumentaion
    # def blob_overlap(blob1, blob2):
    #     n_dim = len(blob1) - 1
    #     root_ndim = sqrt(n_dim)
    #     #print(n_dim)

    #     # radius of two blobs
    #     r1 = blob1[-1] * root_ndim
    #     r2 = blob2[-1] * root_ndim

    #     d = sqrt(np.sum((blob1[:-1] - blob2[:-1])**2))

    #     #no overlap between two blobs
    #     if d > r1 + r2:
    #         return 0
    #     # one blob is inside the other, the smaller blob must die
    #     elif d <= abs(r1 - r2):
    #         return 1
    #     else:
    #         #computing the area of overlap between blobs
    #         ratio1 = (d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d * r1)
    #         ratio1 = np.clip(ratio1, -1, 1)
    #         acos1 = acos(ratio1)

    #         ratio2 = (d ** 2 + r2 ** 2 - r1 ** 2) / (2 * d * r2)
    #         ratio2 = np.clip(ratio2, -1, 1)
    #         acos2 = acos(ratio2)

    #         a = -d + r2 + r1
    #         b = d - r2 + r1
    #         c = d + r2 - r1
    #         d = d + r2 + r1

    #         area = (r1 ** 2 * acos1 + r2 ** 2 * acos2 -0.5 * sqrt(abs(a * b * c * d)))
    #         return area/(np.pi * (min(r1, r2) ** 2))

    # def redundancy(blobs_array, min_dist = 1):
    #     sigma = blobs_array[:, -1].max()
    #     distance = 2 * sigma * sqrt(blobs_array.shape[1] - 1)
    #     tree = spatial.cKDTree(blobs_array[:, :-1])
    #     pairs = np.array(list(tree.query_pairs(distance)))
    #     if len(pairs) == 0:
    #         return blobs_array
    #     else:
    #         for (i, j) in pairs:
    #             blob1, blob2 = blobs_array[i], blobs_array[j]
    #             if blob_overlap(blob1, blob2) > min_dist:
    #             # if np.linalg.norm(blob1[:-1] - np.array(blob2[:-1])) < min_dist:
    #                 if blob1[-1] > blob2[-1]:
    #                     blob2[-1] = 0
    #                 else:
    #                     blob1[-1] = 0

    #     return np.array([b for b in blobs_array if b[-1] > 0])

    # def detect_blob(log_image_np):
    #     co_ordinates = []
    #     (h,w) = image.shape
    #     for i in range(1,h):
    #         for j in range(1,w):
    #             slice_img = log_image_np[:,i-1:i+2,j-1:j+2]
    #             result = np.amax(slice_img)
    #             #result_1 = np.amin(slice_img)
    #             if result >= 0.1:
    #                 z,x,y = np.unravel_index(slice_img.argmax(),slice_img.shape)
    #                 co_ordinates.append((i+x-1,j+y-1,k**z*sigma))
    #     return co_ordinates
    # candidates = list(set(detect_blob(log_image_np)))
    # candidates = np.array(candidates)
    # # candidates = redundancy(candidates,min_dist=0.9)
    # # candidates = [c[:2] for c in co_ordinates]
    # # combos = combinations(candidates, 2)
    # # points_to_remove = [
    # #     point2
    # #     for point1, point2 in combos
    # #     if np.linalg.norm(np.array(point1) - np.array(point2)) < min_dist
    # # ]
    # # candidates = [point for point in candidates if point not in points_to_remove]
    fig, axs = plt.subplots(1, 2)

    # for blob in candidates:
    #     y, x, r= blob
    #     cc, rr = ellipse(x, y, r/2, r/2, shape=blob_mask.shape)
    #     blob_mask[rr, cc] = 1
    #     # axs[0].scatter(x, y, s=r, facecolors='none', edgecolors='r')
    # labels = label(blob_mask)
    # rprops = regionprops(label_image = labels, intensity_image = blob_mask)
    # for props in rprops:
    #     x0, y0 = props.centroid
    #     axs[0].scatter(x0, y0, s=15, facecolors='none', edgecolors='r')

    image = diffread("assets/highrange.tif")
    mask = np.ones_like(image, dtype=bool)
    center = [125, 125]
    blob_mask = np.zeros(image.shape, dtype=np.uint8)
    min_dist = 0.0
    g0 = Persistence(image).persistence

    candidates = list()
    for i, homclass in enumerate(g0):
        p_birth, bl, pers, p_death = homclass
        if pers <= 0.1:
            continue
        y, x = p_birth
        candidates.append([x, y])
    if min_dist > 0.0:
        combos = combinations(candidates, 2)
        points_to_remove = [
            point2
            for point1, point2 in combos
            if np.linalg.norm(np.array(point1) - np.array(point2)) < min_dist
        ]
        candidates = [point for point in candidates if point not in points_to_remove]
    peaks = np.array(candidates).reshape(-1, 2)
    # remove peaks that are within the masked area
    if mask.sum() != mask.shape[0] * mask.shape[1]:
        peaks = np.array([p for p in candidates if mask[p[1], p[0]]]).reshape(-1, 2)
    axs[0].scatter(peaks[:, 0], peaks[:, 1], marker="o", color="g", s=15)

    # im = np.array(image, copy=True, dtype=float)
    # im -= im.min()

    # with catch_warnings():
    #     simplefilter("ignore", category=RuntimeWarning)
    #     im /= gaussian_filter(input=im, sigma=min(image.shape) / 20, truncate=2)
    # im = np.nan_to_num(im, copy=False)

    # autocorr = np.abs(
    #     cross_correlate_masked(arr1=im, arr2=im, m1=mask, m2=mask, mode="same")
    # )
    # autocorr = shift(
    #     autocorr,
    #     shift=np.asarray(center) - np.array(im.shape) / 2,
    #     order=1,
    #     mode="nearest",
    # )
    # laplacian = -1 * laplace(autocorr)
    # threshold = filters.threshold_triangle(laplacian)
    # regions = (laplacian > threshold) * mask

    # # To prevent noise from looking like actual peaks,
    # # we erode labels using a small selection area
    # regions = binary_erosion(regions, footprint=disk(2))

    # labels = label(regions, return_num=False)
    # props = regionprops(label_image=labels, intensity_image=im)
    # candidates = [
    #     prop for prop in props if not np.any(np.isnan(prop.weighted_centroid))
    # ]
    # peaks = list()
    # for prop in candidates:
    #     pos = np.asarray(prop.weighted_centroid)

    #     if any((np.linalg.norm(peak - pos) < 0.0) for peak in peaks):
    #         continue
    #     else:
    #         # local_image = prop.image_convex
    #         if prop.area_convex < 0.2*np.prod(image.shape) :
    #             for coord in prop.coords:
    #                 blob_mask[coord[0], coord[1]] = 1
    #         # print(prop.coords.shape)
    #         # rr, cc = pos.astype(int)
    #         # blob_mask[rr-local_image.shape[0]//2:rr+local_image.shape[0]//2, cc-local_image.shape[1]//2:cc+local_image.shape[1]//2] = local_image
    #         peaks.append(pos[::-1])
    # peaks = np.array([peaks]).reshape(-1,2) #now gives us the final array of peaksaxs[0].imshow(image, origin='lower')

    axs[0].imshow(image, origin="lower", vmin=-1, vmax=1)
    axs[1].imshow(blob_mask, origin="lower")
    plt.show()
