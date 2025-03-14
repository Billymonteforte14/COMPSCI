import numpy as np

np.random.seed(42)
rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0

top_10_wettest_days = np.argsort(rainfall)[-10:][::-1]
top_10_rainfall = rainfall[top_10_wettest_days]

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_indices = np.cumsum([0] + days_in_months[:-1])
monthly_averages = np.array([np.mean(rainfall[start:end]) for start, end in zip(start_indices, start_indices[1:])])

print("Top 10 Wettest Days (Indices):", top_10_wettest_days)
print("Top 10 Rainfall Values (mm):", top_10_rainfall)
print("Monthly Average Rainfall (mm):", monthly_averages)
