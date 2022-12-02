from jupyterworkflow.data import get_bike_count_df
import pandas as pd
import numpy as np

def test_bike_count_df():
    df = get_bike_count_df()
    assert all(df.columns == ['Total', 'East', 'West'])
    assert isinstance(df.index, pd.DatetimeIndex)
    assert len(np.unique(df.index.time)) == 24
