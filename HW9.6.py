import pandas as pd

df = pd.DataFrame({
    'Name': ['  Alice  ', 'BOB', '  Charlie  ', 'David   '],
    'Description': ['  Good student. ', 'Excellent in math!', '  Needs improvement. ', 'Great at sports. ']
})

df['Name'] = df['Name'].str.strip().str.lower()
df['Description'] = df['Description'].str.strip().str.replace(r'\.', '', regex=True).str.lower()

regex_df = df['Description'].str.extract(r'(great|good|excellent)', expand=False)

df['Combined'] = df['Name'] + ': ' + df['Description']

df['Name_length'] = df['Name'].str.len()

filtered_df = df[df['Description'].str.contains('student')]

print(df)
print(regex_df)
print(filtered_df)
