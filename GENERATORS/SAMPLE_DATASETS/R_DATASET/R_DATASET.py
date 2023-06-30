from typing import Literal
from flojoy import flojoy, DataContainer, DefaultParams
from rdatasets import data

@flojoy
def R_DATASET(default: DataContainer, default_parmas: DefaultParams, dataset_key: Literal['ability.cov', 'airmiles', 'AirPassengers', 'airquality', 'anscombe', 'attenu', 'attitude', 'austres', 'BJsales', 'BOD', 'cars', 'ChickWeight', 'chickwts', 'co2', 'crimtab', 'discoveries', 'DNase', 'esoph', 'euro', 'EuStockMarkets', 'faithful', 'Formaldehyde', 'freeny', 'HairEyeColor', 'Harman23', 'Harman74', 'Indometh', 'infert', 'InsectSprays', 'iris', 'iris3', 'islands', 'JohnsonJohnson', 'LakeHuron', 'LakeHuron', 'LifeCycleSavings', 'Loblolly', 'longley', 'lynx', 'morley', 'mtcars', 'nhtemp', 'Nile', 'nottem', 'npk', 'occupationalStatus', 'Orange', 'OrchardSprays', 'PlantGrowth', 'precip', 'presidents', 'pressure', 'Puromycin', 'quakes', 'randu', 'rivers', 'rock', 'Seatbelts', 'sleep', 'stackloss', 'sunspot.month', 'sunspot.year', 'sunspots', 'swiss', 'Theoph', 'Titanic', 'ToothGrowth', 'treering', 'trees', 'UCBAdmissions', 'UKDriverDeaths', 'UKgas', 'USAccDeaths', 'USArrests', 'USJudgeRatings', 'USPersonalExpenditure', 'USPersonalExpenditure', 'VADeaths', 'volcano', 'warpbreaks', 'women', 'WorldPhones', 'WWWusage']='iris') -> DataContainer:
    """
    Retrieves a pandas DataFrame from rdatasets using the provided dataset_key parameter and returns it wrapped in a DataContainer.

    Args:
        dc_inputs (list[DataContainer]): A list of DataContainer objects, but not used in this function.
        params (dict): A dictionary of parameters for this function.
            dataset_key (str): The key used to retrieve the DataFrame.

    Returns:
        DataContainer: A DataContainer object containing the retrieved pandas DataFrame.
    """
    df = data(dataset_key)
    return DataContainer(type='dataframe', m=df)