from flojoy import flojoy, DataContainer
from sklearn.datasets import fetch_20newsgroups
from sklearn.utils import Bunch
import pandas as pd
from typing import cast


@flojoy
def TEXT_DATASET(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The TEXT_DATASET node loads the 20 newsgroups dataset from scikit-learn.

    Parameters
    ----------
    subset: "train" | "test" | "all", default="train"
        Select the dataset to load: "train" for the training set, "test" for the test set, "all" for both.
    categories: list of str, optional
        Select the categories to load. By default, all categories are loaded.
        The list of all categories is:
        'alt.atheism',
        'comp.graphics',
        'comp.os.ms-windows.misc',
        'comp.sys.ibm.pc.hardware',
        'comp.sys.mac.hardware',
        'comp.windows.x',
        'misc.forsale',
        'rec.autos',
        'rec.motorcycles',
        'rec.sport.baseball',
        'rec.sport.hockey',
        'sci.crypt',
        'sci.electronics',
        'sci.med',
        'sci.space',
        'soc.religion.christian',
        'talk.politics.guns',
        'talk.politics.mideast',
        'talk.politics.misc',
        'talk.religion.misc'
    """

    subset = params.get("subset", "train")
    categories = params.get("categories", None)

    if categories:
        newsgroups = fetch_20newsgroups(subset=subset, categories=categories)
    else:
        newsgroups = fetch_20newsgroups(subset=subset)

    newsgroups = cast(Bunch, newsgroups)
    data = newsgroups.data
    labels = [newsgroups.target_names[i] for i in newsgroups.target]

    df = pd.DataFrame({"Text": data, "Label": labels})
    return DataContainer(type="dataframe", m=df)
