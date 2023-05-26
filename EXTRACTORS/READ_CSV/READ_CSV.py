from flojoy import flojoy, DataContainer
import pandas as pd

@flojoy
def read_csv(dc, params):
    '''
    Read a CSV file from disk or a URL, then return a dataframe.
    '''
    url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"    
    file_path = params['file_path'] if 'file_path' in params else url
    df = pd.read_csv(file_path)
    return DataContainer(type='dataframe', m=df)
