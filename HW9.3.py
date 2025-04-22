import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value1': [1, 2, 3, 4]
})
df2 = pd.DataFrame({
    'key': ['B', 'C', 'D', 'E'],
    'value2': [5, 6, 7, 8]
})
df_inner = pd.merge(df1, df2, on='key', how='inner')
df_outer = pd.merge(df1, df2, on='key', how='outer')

df_concat = pd.concat([df1, df2], keys=['df1', 'df2'])

df_time1 = pd.DataFrame({
    'value': [10, 20, 30],
}, index=pd.date_range('20230101', periods=3))
df_time2 = pd.DataFrame({
    'value': [100, 200, 300],
}, index=pd.date_range('20230102', periods=3))
df_time_joined = df_time1.join(df_time2, how='outer', lsuffix='_left', rsuffix='_right')
df_time_joined = df_time_joined.ffill()

def merge_data(*dfs):
    return pd.concat(dfs, axis=1, join='outer')

df_merged = merge_data(df1, df2)

df_dup = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=[0, 1, 1])
df_dup_resolved = df_dup.groupby(df_dup.index).sum()

print(df_inner)
print(df_outer)
print(df_concat)
print(df_time_joined)
print(df_merged)
print(df_dup_resolved)
