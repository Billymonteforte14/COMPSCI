import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

concat_rows = pd.concat([df1, df2], axis=0)
concat_cols = pd.concat([df1, df2], axis=1)
print(concat_rows)
print(concat_cols)

concat_with_keys = pd.concat([df1, df2], axis=0, keys=['df1', 'df2'], names=['DataFrame', 'Row'])
print(concat_with_keys)

df_appended = pd.concat([df1, df2], ignore_index=True)
concat_appended = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df_appended)
print(concat_appended)

df_overlap = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df_overlap2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
concat_overlap = pd.concat([df_overlap, df_overlap2], axis=0)

df_non_overlap = pd.DataFrame({'A': [1, 2], 'C': [3, 4]})
df_non_overlap2 = pd.DataFrame({'B': [5, 6], 'D': [7, 8]})
concat_non_overlap = pd.concat([df_non_overlap, df_non_overlap2], axis=0)

print(concat_overlap)
print(concat_non_overlap)

def combine_and_clean(dfs):
    combined = pd.concat(dfs, axis=0, ignore_index=True)
    combined.columns = [col.strip() for col in combined.columns]
    return combined

dfs = [df1, df_overlap, df_non_overlap]
cleaned_combined_df = combine_and_clean(dfs)
print(cleaned_combined_df)
