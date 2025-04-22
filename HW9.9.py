import pandas as pd
import numpy as np

date_strings = ['2023-01-01', '2023-01-02', '2023-01-03']
dates = pd.to_datetime(date_strings)

time_range = pd.date_range(start='2023-01-01', periods=6, freq='2h')
ts = pd.Series(np.arange(len(time_range)), index=time_range)

print("Original Time Series:")
print(ts)
print()

ts_downsampled = ts.resample('D').mean()
print("Downsampled (Daily Mean):")
print(ts_downsampled)
print()

ts_upsampled = ts.resample('30min').ffill()
print("Upsampled (30min, Forward Fill):")
print(ts_upsampled)
print()

ts_asfreq = ts.asfreq('h')
print("Asfreq (Hourly, NaNs for missing):")
print(ts_asfreq)
print()

ts_shifted = ts.shift(1)
print("Shifted Time Series:")
print(ts_shifted)
print()

ts_diff = ts.diff()
print("Differenced Time Series:")
print(ts_diff)
