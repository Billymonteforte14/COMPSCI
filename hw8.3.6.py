import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randint(1, 10, size=(3, 3)), columns=['A', 'B', 'C'])
df2 = pd.DataFrame(np.random.randint(1, 10, size=(3, 3)), columns=['A', 'B', 'C'])

result_add = df1.add(df2)
result_sub = df1.sub(df2)
result_mul = df1.mul(df2)
result_div = df1.div(df2)

print(result_add)
print(result_sub)
print(result_mul)
print(result_div)

df1_with_nan = pd.DataFrame([[1, 2, np.nan], [4, 5, 6], [7, np.nan, 9]], columns=['A', 'B', 'C'])
df2 = pd.DataFrame([[10, 20, 30], [40, 50, 60], [70, 80, 90]], columns=['A', 'B', 'C'])

result_add_fill = df1_with_nan.add(df2, fill_value=0)
print(result_add_fill)

column_stats = df1.agg(['mean', 'sum'])
row_stats = df1.agg(['mean', 'sum'], axis=1)

print(column_stats)
print(row_stats)

column_stats_apply = df1.apply(np.mean, axis=0)
row_stats_apply = df1.apply(np.mean, axis=1)

print(column_stats_apply)
print(row_stats_apply)

df_normalized_rows = df1.apply(lambda x: (x - x.mean()) / x.std(), axis=1)
print(df_normalized_rows)

df_normalized_columns = df1.apply(lambda x: (x - x.mean()) / x.std(), axis=0)
print(df_normalized_columns)

def z_score_normalize(df):
    return df.apply(lambda x: (x - x.mean()) / x.std(), axis=0)

df_normalized = z_score_normalize(df1)
print(df_normalized)
