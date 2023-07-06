import numpy

from sklearn.feature_extraction.text import CountVectorizer
from typing import Union
from flojoy import flojoy, OrderedPair, DataFrame, Matrix


@flojoy
def COUNT_VECTORIZER(default: DataFrame | Matrix) -> OrderedPair:
    """The COUNT_VECTORIZER node converts a collection (matrix) of text documents to a matrix of token counts.

    Returns
    -------
    ordered_pair DataContainer
        x -> the feature names
        y -> the word counts themselves
    """
    vectorizer = CountVectorizer()

    X = vectorizer.fit_transform(default.m)

    return OrderedPair(x=numpy.array(vectorizer.get_feature_names_out(), y=X.toarray()))
