from flojoy import OrderedPair, flojoy, Scalar, ParametricOrderedTriple
from sklearn.model_selection import train_test_split


# NOTE: We are assuming that arrays is a `(X,y)` pair for now.
# TODO: Support more cases.
@flojoy(deps={"scikit-learn": "1.2.2"})
def TRAIN_TEST_SPLIT(
    arrays: OrderedPair,
    test_size=None,
    train_size=None,
    random_state=None,
    shuffle=True,
    stratify=None,
) -> ParametricOrderedTriple:
    """Split arrays or matrices into random train and test subsets.

    Quick utility that wraps input validation,
    ``next(ShuffleSplit().split(X, y))``, and application to input data
    into a single call for splitting (and optionally subsampling) data into a
    one-liner.

    Read more in the :ref:`User Guide <cross_validation>`.

    Parameters
    ----------
    *arrays : OrderedPair

    test_size : float or int, default=None
        If float, should be between 0.0 and 1.0 and represent the proportion
        of the dataset to include in the test split. If int, represents the
        absolute number of test samples. If None, the value is set to the
        complement of the train size. If ``train_size`` is also None, it will
        be set to 0.25.

    train_size : float or int, default=None
        If float, should be between 0.0 and 1.0 and represent the
        proportion of the dataset to include in the train split. If
        int, represents the absolute number of train samples. If None,
        the value is automatically set to the complement of the test size.

    random_state : int, RandomState instance or None, default=None
        Controls the shuffling applied to the data before applying the split.
        Pass an int for reproducible output across multiple function calls.
        See :term:`Glossary <random_state>`.

    shuffle : bool, default=True
        Whether or not to shuffle the data before splitting. If shuffle=False
        then stratify must be None.

    stratify : array-like, default=None
        If not None, data is split in a stratified fashion, using this as
        the class labels.
        Read more in the :ref:`User Guide <stratification>`.

    Returns
    -------
    splitting : DataContainer, type 'ordered pair'
        List containing train-test split of inputs.

    """
    X, y = arrays.x, arrays.y

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        train_size=train_size,
        random_state=random_state,
        shuffle=shuffle,
        stratify=stratify,
    )

    return ParametricOrderedTriple(X_train, X_test, y_train, y_test)
