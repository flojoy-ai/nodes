import numpy

from sklearn.feature_extraction.text import CountVectorizer

from flojoy import flojoy, DataContainer


@flojoy
def COUNT_VECTORIZER(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The COUNT_VECTORIZER node converts a collection (matrix) of text documents to a matrix of token counts.

    Returns
    -------
    ordered_pair DataContainer
        x -> the feature names
        y -> the word counts themselves
    """
    if dc_inputs[0].type not in ['dataframe', 'matrix']:
        raise ValueError(
            f"unsupported DataContainer type passed to COUNT_VECTORIZER: {dc_inputs[0].type}"
        )

    vectorizer = CountVectorizer()

    X = vectorizer.fit_transform(dc_inputs[0].m)

    return DataContainer(
        type="ordered_pair",
        x=numpy.array(vectorizer.get_feature_names_out()),
        y=X.toarray(),
    )
