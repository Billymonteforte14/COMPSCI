import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': ['x', 'y', np.nan, 'z', 'w'],
    'D': pd.date_range('20230101', periods=5)
})
df['E'] = [np.nan, 1, np.nan, 3, 4]

df_isnull = df.isnull()
df_dropna = df.dropna()
df_fillna = df.fillna(0)

df_time = df.set_index('D')
df_time = df_time.infer_objects()
df_ffill = df_time.ffill()
df_bfill = df_time.bfill()

# Interpolate only the numeric columns
df_numeric = df_time.select_dtypes(include=[np.number])
df_interp = df_numeric.interpolate()

df_subset_drop = df.dropna(subset=['A', 'B'])

def smart_fill(df):
    for col in df.columns:
        if df[col].dtype in [np.float64, np.int64]:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].ffill()
    return df

df_filled = smart_fill(df.copy())

print(df.mean(numeric_only=True))
df.plot()
plt.show()
