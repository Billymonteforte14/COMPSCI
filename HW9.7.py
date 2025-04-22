import pandas as pd

data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
        'Value': [10, 20, 30, 40, 50, 60, 70]}
df = pd.DataFrame(data)

df['Category'] = df['Category'].astype('category')

print("Memory usage before:", df.memory_usage(deep=True))

df['Category'] = df['Category'].cat.reorder_categories(['C', 'B', 'A'], ordered=True)

df['Category_comparison'] = df['Category'] == 'A'

category_stats = df.groupby('Category', observed=False).agg({'Value': ['mean', 'sum']})
print("\nCategory stats:\n", category_stats)

df_one_hot = pd.get_dummies(df['Category'], prefix='Category')
print("\nOne-hot encoded DataFrame:\n", df_one_hot)

print("\nDataFrame with categorical data:\n", df)
