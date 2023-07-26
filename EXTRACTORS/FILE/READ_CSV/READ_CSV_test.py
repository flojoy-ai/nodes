import pytest
import os
import numpy as np
import pandas as pd
from flojoy import DataFrame


def test_READ_CSV(mock_flojoy_decorator):
    test_path: str = (
        f"{os.path.dirname(os.path.realpath(__file__))}/assets/iris_test.csv"
    )

    import READ_CSV

    output = READ_CSV.READ_CSV(file_path=test_path)
    assert isinstance(output, DataFrame)
    assert output.m.shape == (30, 5)
    print(output.m.columns)
    assert output.m.columns.to_list() == [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "variety",
    ]
    assert output.m["variety"].tolist() == [
        "Versicolor",
        "Setosa",
        "Virginica",
        "Setosa",
        "Versicolor",
        "Virginica",
        "Virginica",
        "Setosa",
        "Setosa",
        "Setosa",
        "Virginica",
        "Versicolor",
        "Virginica",
        "Virginica",
        "Virginica",
        "Setosa",
        "Setosa",
        "Virginica",
        "Versicolor",
        "Versicolor",
        "Setosa",
        "Versicolor",
        "Versicolor",
        "Versicolor",
        "Setosa",
        "Virginica",
        "Setosa",
        "Versicolor",
        "Versicolor",
        "Virginica",
    ]
