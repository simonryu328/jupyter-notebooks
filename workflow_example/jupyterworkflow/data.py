import os
from urllib.request import urlretrieve
import pandas as pd

URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_bike_count_df(filename='bike_count.csv', url=URL, force_download=False):
    '''Download and cache bike count data

    Parameters
        filename: string (optional)
            location to save data
        url: string (optional)
            web location of data
        force_download: bool (optional)
        if True, force download data

    Returns
        data: pandas.DataFrame
            The bike count dataframe
    '''
    if force_download or not os.path.exists(filename):
        urlretrieve(URL, filename)
    df = pd.read_csv('bike_count.csv', index_col='Date')
    try:
        df.index = pd.to_datetime(df.index, format='%m/%d/%Y %I:%M:%S %p')
    except TypeError:
        df.index = pd.to_datetime(df.index)

    df.columns = ['Total', 'East', 'West']
    return df
