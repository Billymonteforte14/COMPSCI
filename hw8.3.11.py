import pandas as pd
import matplotlib.pyplot as plt

area_data = pd.read_csv('states_area.csv')
population_data = pd.read_csv('states_population.csv')

merged_data = pd.merge(area_data, population_data, on='state')

merged_data['population_density'] = merged_data['population'] / merged_data['area']

top_10_dense = merged_data.nlargest(10, 'population_density')

merged_data['population_category'] = pd.cut(merged_data['population'], bins=[0, 1000000, 10000000, float('inf')], labels=['small', 'medium', 'large'])

plt.figure(figsize=(10, 6))
plt.scatter(merged_data['area'], merged_data['population'], c=merged_data['population'] > 10000000, cmap='coolwarm', label='Population > 10M')
plt.xlabel('Area (sq miles)')
plt.ylabel('Population')
plt.title('State Population vs Area')
plt.colorbar(label='Population > 10M')
plt.show()
