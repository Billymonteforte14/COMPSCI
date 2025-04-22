import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': np.random.rand(1000000),
    'B': np.random.rand(1000000),
    'C': np.random.rand(1000000),
    'Category': np.random.choice(['X', 'Y', 'Z'], size=1000000)
})

df['Result_standard'] = df['A'] + df['B'] * df['C']
df.eval("Result_eval = A + B * C", inplace=True)

filtered_df = df.query("Result_eval > 0.5 and Category == 'X'")

df['Category'] = df['Category'].astype('category')

df['SmallInt'] = (df['A'] * 100).astype('int16')
df['Precise'] = df['B'].astype('float32')

from timeit import timeit
standard_time = timeit("df['A'] + df['B'] * df['C']", globals=globals(), number=10)
eval_time = timeit("df.eval('A + B * C')", globals=globals(), number=10)

print(f"Standard: {standard_time:.4f}s")
print(f"Eval: {eval_time:.4f}s")
print(df.memory_usage(deep=True).sum())
print(filtered_df.head())
