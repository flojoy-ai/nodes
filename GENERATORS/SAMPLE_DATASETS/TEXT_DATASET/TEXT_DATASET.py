from flojoy import flojoy, DataFrame, Defaultparams
from sklearn.datasets import fetch_20newsgroups
from sklearn.utils import Bunch
import pandas as pd
from typing import cast


# TODO: Add more datasets to this node.
@flojoy
def TEXT_DATASET(default_params: Defaultparams) -> DataFrame:
    """The TEXT_DATASET node loads the 20 newsgroups dataset from scikit-learn.
    The data is returned as a dataframe with one column containing the text
    and the other containing the category.

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
    remove_headers: boolean, default=false
        Remove the headers from the data.
    remove_footers: boolean, default=false
        Remove the footers from the data.
    remove_quotes: boolean, default=false
        Remove the quotes from the data.
    """

    subset = default_params.get("subset", "train")
    categories = default_params.get("categories", None)
    remove_headers = default_params.get("remove_headers", False)
    remove_footers = default_params.get("remove_footers", False)
    remove_quotes = default_params.get("remove_quotes", False)

    to_remove = []
    if remove_headers:
        to_remove.append("headers")
    if remove_footers:
        to_remove.append("footers")
    if remove_quotes:
        to_remove.append("quotes")
    to_remove = tuple(to_remove)

    if categories:
        newsgroups = fetch_20newsgroups(
            subset=subset, categories=categories, remove=to_remove
        )
    else:
        newsgroups = fetch_20newsgroups(subset=subset, remove=to_remove)

    newsgroups = cast(Bunch, newsgroups)
    data = newsgroups.data
    labels = [newsgroups.target_names[i] for i in newsgroups.target]

    df = pd.DataFrame({"Text": data, "Label": labels})
    return DataFrame(m=df)
