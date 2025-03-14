import numpy as np

np.random.seed(42)
rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0

days = np.arange(1, 366)
is_rainy = rainfall > 0

structured_data = np.zeros(365, dtype=[('day', 'i4'), ('rainfall', 'f4'), ('is_rainy', 'bool')])
structured_data['day'] = days
structured_data['rainfall'] = rainfall
structured_data['is_rainy'] = is_rainy

rainy_days = structured_data[structured_data['is_rainy'] == True]
average_rainfall_rainy_days = np.mean(rainy_days['rainfall'])

sorted_rainy_days = np.sort(structured_data, order='rainfall')
top_5_rainiest_days = sorted_rainy_days[-5:]

print("Average Rainfall on Rainy Days (mm):", average_rainfall_rainy_days)
print("\nTop 5 Rainiest Days:\n", top_5_rainiest_days)
