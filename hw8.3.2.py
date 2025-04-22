import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 32, 30, 29, 22],
    'Score': [85, 90, 95, 88, 76]
})

loc_result = df.loc[0:2]
iloc_result = df.iloc[0:2]

filtered = df[df['Age'] > 28]

threshold = 85
numeric_df = df.select_dtypes(include='number')
mask = numeric_df > threshold
greater_than_threshold = numeric_df[mask]

df2 = df.copy()
df2['Age_plus_5'] = df2['Age'] + 5

original = df[['Age']]
copy_safe = df[['Age']].copy()
copy_safe['Age'] = copy_safe['Age'] + 10

df3 = pd.DataFrame({
    'City': ['NY', 'LA', 'Chicago', 'Houston', 'Phoenix'],
    'Temp': [75, 85, 60, 90, 100],
    'Humidity': [65, 70, 55, 80, 20]
})
df3.index = ['A', 'B', 'C', 'D', 'E']

loc_slice = df3.loc['B':'D', ['Temp', 'Humidity']]
iloc_slice = df3.iloc[1:4, 0:2]

print("loc_result:\n", loc_result)
print("iloc_result:\n", iloc_result)
print("Filtered (Age > 28):\n", filtered)
print("Greater than threshold:\n", greater_than_threshold)
print("Original slice:\n", original)
print("Safe copy slice:\n", copy_safe)
print("loc_slice:\n", loc_slice)
print("iloc_slice:\n", iloc_slice)

