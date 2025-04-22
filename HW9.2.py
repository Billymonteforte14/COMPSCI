import pandas as pd
import numpy as np

arrays = [
    ['A', 'A', 'A', 'B', 'B', 'B'],
    [1, 2, 3, 1, 2, 3]
]
index = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number'))

df = pd.DataFrame({
    'value': [10, 20, 30, 40, 50, 60]
}, index=index)

df_swap = df.swaplevel()
df_sorted = df.sort_index()

df_unstack = df.unstack()
df_stack = df_unstack.stack(future_stack=True)

df_grouped = df.groupby(level='letter').sum()

print(df_swap)
print(df_sorted)
print(df_unstack)
print(df_stack)
print(df_grouped)
