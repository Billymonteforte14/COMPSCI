import numpy as np
import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s2 = pd.Series([5, 4, 3, 2, 1], index=['a', 'b', 'c', 'd', 'e'])

exp_s1 = np.exp(s1)
log_s2 = np.log(s2)

print(exp_s1)
print(log_s2)

s3 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s4 = pd.Series([5, 15, 25, 35], index=['b', 'c', 'd', 'e'])

sum_series = s3 + s4
print(sum_series)

condition_result = np.where(s1 > 3, 'Greater', 'Smaller')
condition_series = pd.Series(condition_result, index=s1.index)
print(condition_series)

def apply_ufunc_with_cleaning(series, ufunc):
    result = ufunc(series)
    result_cleaned = result.fillna(0).astype(np.float64)
    return result_cleaned

cleaned_result = apply_ufunc_with_cleaning(s1, np.log)
print(cleaned_result)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

series_result = s1 + s2
array_result = arr1 + arr2

print(series_result)
print(array_result)

print(s1.index)
print(arr1)

import time

start = time.time()
for _ in range(1000000):
    _ = s1 + s2
print("Series time:", time.time() - start)

start = time.time()
for _ in range(1000000):
    _ = arr1 + arr2
print("Array time:", time.time() - start)
