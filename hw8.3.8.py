import pandas as pd
import numpy as np

arrays = [
    ['A', 'A', 'B', 'B', 'C', 'C'],
    ['X', 'Y', 'X', 'Y', 'X', 'Y']
]
index = pd.MultiIndex.from_arrays(arrays, names=('letters', 'subletters'))
data = np.random.randn(6, 2)
df = pd.DataFrame(data, index=index, columns=['value1', 'value2'])

print(df.loc[('A', 'X')])

stacked = df.stack()
print(stacked)
unstacked = stacked.unstack()
print(unstacked)

cross_section = df.xs('A', level='letters')
print(cross_section)

grouped = df.groupby(level='letters').sum()
print(grouped)

df_renamed = df.rename_axis(index={'letters': 'new_letters', 'subletters': 'new_subletters'})
df_renamed.columns = [col.split('_')[0] for col in df_renamed.columns]
print(df_renamed)
