import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s_reindexed = s.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
s_forward_fill = s.reindex(['a', 'b', 'c', 'd', 'e'], method='ffill')

df = pd.DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'], columns=['x', 'y', 'z'])
df_reindexed = df.reindex(index=['a', 'b', 'c', 'd'], columns=['x', 'y', 'z', 'w'])
df_shape = df_reindexed.shape
df_nulls = df_reindexed.isnull().sum().sum()

dates = pd.date_range('2023-01-01', periods=10)
dates_missing = dates.delete([1, 3, 5, 7])
ts = pd.Series(np.random.randn(len(dates_missing)), index=dates_missing)
ts_reindexed = ts.reindex(pd.date_range('2023-01-01', periods=10))
ts_interpolated = ts_reindexed.interpolate()

def custom_reindex(obj, new_index, method=None):
    return obj.reindex(new_index, method=method)

sample_series = pd.Series([5, 1, 3, 2], index=['d', 'a', 'c', 'b'])
sorted_index = sample_series.sort_index()
sorted_values = sample_series.sort_values()

print("Original Series:\n", s)
print("\nReindexed with fill_value:\n", s_reindexed)
print("\nReindexed with forward fill:\n", s_forward_fill)

print("\nOriginal DataFrame:\n", df)
print("\nReindexed DataFrame:\n", df_reindexed)
print("\nShape of reindexed DataFrame:", df_shape)
print("Total nulls in reindexed DataFrame:", df_nulls)

print("\nOriginal Time Series (with missing dates):\n", ts)
print("\nReindexed Time Series:\n", ts_reindexed)
print("\nInterpolated Time Series:\n", ts_interpolated)

print("\nCustom reindexed Series:\n", custom_reindex(s, ['a', 'b', 'c', 'd', 'e'], method='ffill'))

print("\nOriginal Sample Series:\n", sample_series)
print("\nSorted by index:\n", sorted_index)
print("\nSorted by values:\n", sorted_values)
