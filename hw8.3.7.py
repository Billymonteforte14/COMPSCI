import pandas as pd
import numpy as np

data = {
    'A': [1, np.nan, 3, 4, np.nan],
    'B': [5, 6, np.nan, np.nan, 10],
    'C': [np.nan, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

print(df.isnull())
print(df.notnull())

df_dropped_rows = df.dropna(axis=0, how='any')
print(df_dropped_rows)

df_dropped_columns = df.dropna(axis=1, how='any')
print(df_dropped_columns)

df_dropped_threshold = df.dropna(axis=0, thresh=3)
print(df_dropped_threshold)

df_filled_constant = df.fillna(0)
print(df_filled_constant)

df_filled_forward = df.ffill()
print(df_filled_forward)

df_filled_backward = df.bfill()
print(df_filled_backward)

time_data = {
    'Date': pd.date_range('2025-01-01', periods=5, freq='D'),
    'Value': [1, np.nan, 3, np.nan, 5]
}
df_time_series = pd.DataFrame(time_data)

df_interpolated = df_time_series.interpolate(method='linear')
print(df_interpolated)

def clean_data(df, method='fill', threshold=3, fill_value=0):
    if method == 'drop':
        df_cleaned = df.dropna(axis=0, thresh=threshold)
    elif method == 'fill':
        df_cleaned = df.fillna(fill_value)
    elif method == 'ffill':
        df_cleaned = df.ffill()
    elif method == 'bfill':
        df_cleaned = df.bfill()
    else:
        df_cleaned = df
    return df_cleaned

df_cleaned = clean_data(df, method='fill', fill_value=999)
print(df_cleaned)
