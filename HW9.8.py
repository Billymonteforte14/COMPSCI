import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start='2023-01-01', periods=10, freq='D')
ts = pd.Series(np.random.randint(10, 100, size=10), index=dates)

ts['2023-01-03':'2023-01-07']

ts_resampled = ts.resample('2D').mean()

rolling_mean = ts.rolling(window=3).mean()
rolling_std = ts.rolling(window=3).std()

ts_missing = ts.copy()
ts_missing['2023-01-05'] = np.nan
ts_interpolated = ts_missing.interpolate()

ts.plot(label='Original')
rolling_mean.plot(label='Rolling Mean')
rolling_std.plot(label='Rolling Std')
ts_interpolated.plot(label='Interpolated', linestyle='dashed')
plt.legend()
plt.show()
