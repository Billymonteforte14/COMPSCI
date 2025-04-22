import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Category1': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B', 'C'],
    'Category2': ['X', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'X', 'Y'],
    'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90]
})

grouped = df.groupby(['Category1', 'Category2']).agg({'Value': ['sum', 'mean', 'max']})

grouped_custom = df.groupby(['Category1', 'Category2']).agg({'Value': lambda x: np.std(x)})

grouped_normalized = df.groupby(['Category1', 'Category2']).agg({'Value': lambda x: ((x - x.mean()) / x.std()).mean()})

filtered_groups = df.groupby(['Category1']).filter(lambda x: x['Value'].mean() > 50)

sorted_group = df.groupby(['Category1', 'Category2']).sum().sort_values(by='Value', ascending=False)

grouped.plot(kind='bar', stacked=True)
plt.show()

print(grouped)
print(grouped_custom)
print(grouped_normalized)
print(filtered_groups)
print(sorted_group)
