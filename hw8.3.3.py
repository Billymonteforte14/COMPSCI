import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
try:
    s.index[0] = 'z'
except TypeError as e:
    print("Index is immutable:", e)

arrays = [
    ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']
]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
s2 = pd.Series(np.random.randn(8), index=index)
print(s2['bar'])
print(s2['baz', 'two'])

df = pd.DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['A', 'B', 'C'])
print(df.swaplevel())
print(df.sort_index())

df_reset = df.reset_index()
print(df_reset)

df_set = df_reset.set_index(['level_0', 'level_1'])
print(df_set)

df_reset2 = df.reset_index(drop=True)
print(df_reset2)

df1 = pd.DataFrame({'A': [1, 2]}, index=['a', 'b'])
df2 = pd.DataFrame({'A': [3, 4]}, index=['b', 'c'])
print(df1 + df2)
