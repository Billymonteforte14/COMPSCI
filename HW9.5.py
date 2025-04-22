import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=6, freq='D'),
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [200, 300, 400, 500, 600, 700],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South']
})

pivot1 = pd.pivot_table(df, values='Sales', index=['Date', 'Category'], columns='Region', aggfunc='sum')

pivot2 = pd.pivot_table(df, values='Sales', index='Category', columns='Region', aggfunc='sum', margins=True)

pivot3 = df.groupby(['Category', 'Region']).agg({'Sales': 'sum'}).unstack()

def create_pivot_table(data, index, columns, values, aggfunc='sum', margins=False):
    return pd.pivot_table(data, index=index, columns=columns, values=values, aggfunc=aggfunc, margins=margins)

pivot_custom = create_pivot_table(df, index='Category', columns='Region', values='Sales', aggfunc='sum', margins=True)

pivot1.plot(kind='bar')
plt.title('Pivot Table: Sales by Date and Category')
plt.show()

print(pivot1)
print(pivot2)
print(pivot3)
print(pivot_custom)
