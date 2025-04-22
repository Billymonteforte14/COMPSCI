import pandas as pd
import numpy as np

scores = pd.Series([88, 92, 79, 95, 67], index=['Alice', 'Bob', 'Charlie', 'David', 'Eva'])
top_scorer = scores.idxmax()
above_mean = scores[scores > scores.mean()]
print(top_scorer)
print(above_mean)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 25, 22],
    'Passed': [True, True, False]
}
df = pd.DataFrame(data)
print(df.dtypes)
print(df.describe(include='all'))

df_csv = pd.read_csv('data.csv')
print(df_csv.head())
print(df_csv.tail())
print(df_csv.info())
print(df_csv.describe(include='all'))

dates = pd.date_range('2024-01-01', periods=10)
temp_series = pd.Series(np.random.randint(60, 100, size=10), index=dates)
print(temp_series['2024-01-03':'2024-01-07'])

s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])
result = s1 + s2
print(result)
