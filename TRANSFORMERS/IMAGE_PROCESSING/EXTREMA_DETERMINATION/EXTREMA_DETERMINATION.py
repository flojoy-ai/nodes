from flojoy import flojoy, Plotly, Image, Grayscale, Matrix, DCNpArrayType
import plotly.express as px
import plotly.graph_objects as go
from scipy.ndimage import gaussian_filter, laplace, shift
from math import floor
from itertools import combinations

import scipy.fft
from scipy.fft import _pocketfft
from os import cpu_count

from warnings import catch_warnings, simplefilter

import numpy as np
from typing import Optional

from nodes.VISUALIZERS.template import plot_layout
from PIL import Image as PILImage

from skimage.registration import phase_cross_correlation
from skimage.registration._masked_phase_cross_correlation import cross_correlate_masked
from skimage.draw import ellipse
import skimage.filters as filters
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion, disk


@flojoy(deps={"scikit-image":"0.21.0"})
def EXTREMA_DETERMINATION(
    default: Image | Grayscale | Matrix,
    mask : Optional[Grayscale | Matrix] = None,
    center: list[int] = None,
    min_dist: float = 0.0,
    persistence_algorithm: bool = True,
    high_symmetry: bool = True,
    prominence: float = 0.0,
) -> Plotly:

    """
    This function is concerned with the determination of peak finding in 
    an image. The ability to find local peaks ( or thoughs in the case of 
    minimization) will not depend on the extrema being exponentially separated
    from the neighboring values, or some ridiulously restrictive constraint like
    that. To that aim, we implement two algorithms to find the local max.  

    The first algorithm is with the technique of masked phase cross correlation [1],
    while the second uses the persistence birth/death algorithms [2, 3]. My original
    implementations of these libraries were utilized for the detection of elastic
    scattering peaks in diffraction data, found in the `scikit-ued` library of Python [4].

    I am obliged to mention that the code for the crossed correlation approach was
    developed by Laurent Rene de Cotret in the `scikit-ued` library, and the 
    functionality for autocentering and cross correlation was developed by him
    for this package. The functionality has been ported here, as the import
    of the entire library is bloating, and unnecessary. 
    
    Yet, this approach has limitations, the absolutely alrgest of which is that
    the algorithm assumes that the extrema are symmetrically distributed around
    some center point. All extrema are determined relative to the center
    position. Also, for closely spaced points, 
    extremely noisy data, or for data that has very low dynamic range, the 
    algorithm fails. This makes this approach suited then only for images with 
    high degrees of symmetry, as well as high contrast images.

    To combat these limitations, I present the second algo: the prominence algorithm, where a single
    value is applied locally to determine the relative 'peakiness' of a given pixel,
    inspecting only the neighbors around that given pixel. While computationally
    more intense for images of resolution >4K, it produces extremely accurate 
    results for the correct value of prominence in potentially low-contrast images
    

    Parameters
    ----------


    References
    ----------
    [1] Liu, Lai Chung. Chemistry in Action: Making Molecular Movies with Ultrafast
    Electron Diffraction and Data Science, Chapter 2. Springer Nature, 2020.

    [2] Huber, S. (2021). Persistent Homology in Data Science. In: Haber, P.,
    Lampoltshammer, T., Mayr, M., Plankensteiner, K. (eds) Data Science - Analytics
    and Applications. Springer Vieweg, Wiesbaden.
    https://doi.org/10.1007/978-3-658-32182-6_13

    [3] Edelsbrunner, H. and John L Harer (2010). Computational Topology. In: American
    Mathematical Society.

    [4] L. P. René de Cotret, M. R. Otto, M. J. Stern. and B. J. Siwick.
    An open-source software ecosystem for the interactive exploration of 
    ultrafast electron scattering data, Advanced Structural and Chemical 
    Imaging 4:11 (2018) 

    """

    if isinstance(default, Image):
        r = default.r
        g = default.g
        b = default.b
        a = default.a

        if a is None:
            image = np.stack((r, g, b), axis=2)
        else:
            image = np.stack((r, g, b, a), axis=2)
        image = PILImage.fromarray(image)
        image = np.array(image.convert("L"), dtype=np.uint8) # a greyscale image that can be processed
    elif isinstance(default, Grayscale) or isinstance(default, Matrix):
        image = np.array(default.m) #explicit typing just to be extra safe
        
    # This now produces an (M, N) array that we can then process! The algorthims
    # have no specificity on input data type unlike the `REGION_PROPERTIES` node.
    if mask is None:
        mask = np.ones(image.shape)
    else:
        if mask.shape != image.shape:
            raise IndexError("Provided mask is not the same shape as the input image.")

    if not persistence_algorithm:
        im = np.array(image, copy=True, dtype=float)
        im -= im.min()
        if high_symmetry:
            if center is None:
                center = autocenter(im=image, mask=mask)
                # Then we need to autodetermine the center of the iamge
                # raise ValueError("For the crossed correlated mask algorithm, the center of the peaks \
                #                   in the image must be specified")
            with catch_warnings():
                simplefilter("ignore", category=RuntimeWarning)
                im /= gaussian_filter(input=im, sigma=min(image.shape) / 20, truncate=2)
            im = np.nan_to_num(im, copy=False)

            autocorr = np.abs(
                cross_correlate_masked(arr1=im, arr2=im, m1=mask, m2=mask, mode="same")
            )
            autocorr = shift(
                autocorr,
                shift=np.asarray(center) - np.array(im.shape) / 2,
                order=1,
                mode="nearest",
            )
            laplacian = -1 * laplace(autocorr)
            threshold = filters.threshold_triangle(laplacian)
            regions = (laplacian > threshold) * mask
        else:
            regions = im * mask

        # To prevent noise from looking like actual peaks,
        # we erode labels using a small selection area
        regions = binary_erosion(regions, footprint=disk(2))

        labels = label(regions, return_num=False)
        props = regionprops(label_image=labels, intensity_image=im)
        candidates = [
            prop for prop in props if not np.any(np.isnan(prop.weighted_centroid))
        ]
        peaks = list()
        for prop in candidates:
            pos = np.asarray(prop.weighted_centroid)
            if any((np.linalg.norm(peak - pos) < min_dist) for peak in peaks):
                continue
            else:
                peaks.append(pos[::-1])
        peaks = np.array([peaks]).reshape(-1,2) #now gives us the final array of peaks
    else: # we use the persistence algorithm
        g0 = Persistence(image).persistence
        birth_death = list()
        birth_death_indices = list()
        persistencies = list()
        candidates = list()
        bd_threshold = 0.0
        for i, homclass in enumerate(g0):
            p_birth, bl, pers, p_death = homclass
            persistencies.append(pers)
            if pers <= bd_threshold:
                continue
            x, y = bl, bl - pers
            birth_death.append([x, y])
            birth_death_indices.append(i)
        for i, homclass in enumerate(g0):
            p_birth, bl, pers, p_death = homclass
            if pers <= prominence:
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
            peaks = np.array([p for p in candidates if mask[p[1], p[0]]]).reshape(-1,2)

    # Congratulations! We now have an (N,2) array of the peaks in the image;
    # let's visualize it!
    # Right now we have a greyscale image, let's create a version
    # that's black and white so we can render it. First, scale image to
    # range 0-255.
    image -= image.min()
    image = image / float(image.max())
    image *= 255

    rgb_image = np.zeros((*image.shape, 3), dtype=np.uint8) #only generated for plotting
    rgb_image[..., 0] = image * 255  # Red channel
    rgb_image[..., 1] = image * 255  # Green channel
    rgb_image[..., 2] = image * 255  # Blue channel

    layout = plot_layout(title=f"IMAGE with {peaks.shape[0]} objects")
    fig = px.imshow(img=rgb_image)
    fig.layout = layout
    marker_trace = go.Scatter(x=peaks[:,0], y=peaks[:,1], mode='markers', marker=dict(color='green', size=15), showlegend=False)
    fig.add_trace(marker_trace)

    fig.update_xaxes(range=[0, image.shape[0]])
    fig.update_yaxes(range=[0, image.shape[1]])
    return Plotly(fig=fig)

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



def autocenter(im :DCNpArrayType, mask: Optional[DCNpArrayType] = None):

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