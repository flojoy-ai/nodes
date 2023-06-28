import pandas as pd
from typing import cast
from dataclasses import dataclass
from flojoy import flojoy, DataFrame
from sklearn.model_selection import train_test_split


@dataclass(frozen=True)
class TrainTestSplitOutput:
    train: DataFrame
    test: DataFrame


@flojoy(deps={"scikit-learn": "1.2.2"})
def TRAIN_TEST_SPLIT(
    default: DataFrame, test_size: float = 0.2
) -> TrainTestSplitOutput:
    df = default.m

    train, test = cast(list[pd.DataFrame], train_test_split(df, test_size))
    return TrainTestSplitOutput(train=DataFrame(df=train), test=DataFrame(df=test))
