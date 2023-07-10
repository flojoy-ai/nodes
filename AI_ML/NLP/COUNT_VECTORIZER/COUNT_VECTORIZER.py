import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from flojoy import flojoy, OrderedPair, DataFrame, Matrix


@flojoy(deps={"scikit-learn": "1.2.2"})
def COUNT_VECTORIZER(default: DataFrame | Matrix) -> OrderedPair:
    """The COUNT_VECTORIZER node converts a collection (matrix) of text documents to a matrix of token counts.

    Returns
    -------
    ordered_pair DataContainer
        x -> the feature names
        y -> the word counts themselves
    """
    arr = []
    if isinstance(default, DataFrame):
        default.m = default.m.values

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(default.m.flatten())
    x = np.array(vectorizer.get_feature_names_out())

    y = X.toarray().flatten()
    x = np.arange(0, len(y))

    return OrderedPair(x=x, y=y)
