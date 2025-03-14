import numpy as np

np.random.seed(42)
rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0

sorted_rainfall = np.sort(rainfall)
median_rainfall = np.median(rainfall)
percentile_90 = np.percentile(rainfall, 90)

print("Sorted Rainfall Data:\n", sorted_rainfall)
print("Median Rainfall (mm):", median_rainfall)
print("90th Percentile Rainfall (mm):", percentile_90)
