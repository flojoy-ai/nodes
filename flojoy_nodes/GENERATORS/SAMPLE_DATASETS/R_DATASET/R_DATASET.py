from flojoy import flojoy, DataFrame
from rdatasets import data
from typing import Literal


@flojoy(deps={"rdatasets": "0.1.0"})
def R_DATASET(
    dataset_key: Literal[
        "ability.cov",
        "airmiles",
        "AirPassengers",
        "airquality",
        "anscombe",
        "attenu",
        "attitude",
        "austres",
        "BJsales",
        "BOD",
        "cars",
        "ChickWeight",
        "chickwts",
        "co2",
        "crimtab",
        "discoveries",
        "DNase",
        "esoph",
        "euro",
        "EuStockMarkets",
        "faithful",
        "Formaldehyde",
        "freeny",
        "HairEyeColor",
        "Harman23",
        "Harman74",
        "Indometh",
        "infert",
        "InsectSprays",
        "iris",
        "iris3",
        "islands",
        "JohnsonJohnson",
        "LakeHuron",
        "LakeHuron",
        "LifeCycleSavings",
        "Loblolly",
        "longley",
        "lynx",
        "morley",
        "mtcars",
        "nhtemp",
        "Nile",
        "nottem",
        "npk",
        "occupationalStatus",
        "Orange",
        "OrchardSprays",
        "PlantGrowth",
        "precip",
        "presidents",
        "pressure",
        "Puromycin",
        "quakes",
        "randu",
        "rivers",
        "rock",
        "Seatbelts",
        "sleep",
        "stackloss",
        "sunspot.month",
        "sunspot.year",
        "sunspots",
        "swiss",
        "Theoph",
        "Titanic",
        "ToothGrowth",
        "treering",
        "trees",
        "UCBAdmissions",
        "UKDriverDeaths",
        "UKgas",
        "USAccDeaths",
        "USArrests",
        "USJudgeRatings",
        "USPersonalExpenditure",
        "USPersonalExpenditure",
        "VADeaths",
        "volcano",
        "warpbreaks",
        "women",
        "WorldPhones",
        "WWWusage",
    ] = "iris"
) -> DataFrame:
    """The R_DATASET node retrieves a pandas DataFrame from rdatasets using the provided dataset_key parameter and returns it wrapped in a DataContainer.

    Parameters:
    -----------
    dataset_key: str

    Returns:
        DataFrame: A DataContainer object containing the retrieved pandas DataFrame.
    """

    df = data(dataset_key)

    if df is None:
        raise ValueError(f"Failed to retrieve '{dataset_key}' from rdatasets package!")
    return DataFrame(df=df)
