import pandas as pd

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key': ['K0', 'K1', 'K2', 'K3']
})

df2 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
    'key': ['K0', 'K1', 'K2', 'K3']
})

merged_df1 = pd.merge(df1, df2, on='key')
print(merged_df1)

df3 = pd.DataFrame({
    'E': ['E0', 'E1', 'E2'],
    'key': ['K0', 'K1', 'K1']
})

merged_df2 = pd.merge(df1, df3, on='key', how='left')
print(merged_df2)

df4 = pd.DataFrame({
    'F': ['F0', 'F1', 'F2'],
    'key': ['K0', 'K1', 'K1']
})

merged_df3 = pd.merge(df3, df4, on='key')
print(merged_df3)

df5 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3']
})

df6 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

merged_df4 = pd.merge(df5, df6, on='key', suffixes=('_left', '_right'))
print(merged_df4)

df7 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

df8 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
}, index=['K0', 'K1', 'K3'])

joined_df1 = df7.join(df8, how='inner')
print(joined_df1)

df9 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2'],
    'X': ['X0', 'X1', 'X2']
})

df10 = pd.DataFrame({
    'key': ['K0', 'K1', 'K3'],
    'Y': ['Y0', 'Y1', 'Y2']
})

df11 = pd.DataFrame({
    'key': ['K0', 'K2', 'K3'],
    'Z': ['Z0', 'Z1', 'Z2']
})

merged_df5 = pd.merge(pd.merge(df9, df10, on='key', how='outer'), df11, on='key', how='outer', indicator=True)
print(merged_df5)