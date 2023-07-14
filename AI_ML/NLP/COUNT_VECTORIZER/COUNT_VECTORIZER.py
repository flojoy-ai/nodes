from typing import TypedDict
from sklearn.feature_extraction.text import CountVectorizer
from flojoy import flojoy, DataFrame, Matrix, Vector
import pandas as pd


class CountVectorizerOutput(TypedDict):
    tokens: DataFrame
    word_count_vector: Vector


@flojoy(deps={"scikit-learn": "1.2.2"})
def COUNT_VECTORIZER(default: DataFrame | Matrix | Vector) -> CountVectorizerOutput:
    """The COUNT_VECTORIZER node converts a collection (matrix) of text documents to a matrix of token counts.

    Returns
    -------
    ordered_pair DataContainer
        x -> the feature names
        y -> the word counts themselves
    """

    if isinstance(default, DataFrame):
        data = default.m.values
    elif isinstance(default, Vector):
        data = default.v
    else:
        data = default.m

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data.flatten())

    x = pd.DataFrame({"tokens": vectorizer.get_feature_names_out()})
    y = X.toarray()

    return CountVectorizerOutput(tokens=DataFrame(df=x), word_count_vector=Vector(v=y))
