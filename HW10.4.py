import numpy as np
import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D']
y = [10, 15, 7, 12]
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1)
plt.bar(x, y, color='skyblue')
plt.title('Bar Plot')

plt.subplot(2, 3, 2)
plt.barh(x, y, color='lightgreen')
plt.title('Horizontal Bar Plot')

data = np.random.normal(0, 1, 1000)
plt.subplot(2, 3, 3)
plt.hist(data, bins=20, color='orange', edgecolor='black')
plt.title('Histogram')

x_vals = np.random.rand(100)
y_vals = np.random.rand(100)
sizes = np.random.rand(100) * 100
plt.subplot(2, 3, 4)
plt.scatter(x_vals, y_vals, s=sizes, alpha=0.5, color='purple')
plt.title('Scatter Plot')

labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [35, 25, 20, 20]
plt.subplot(2, 3, 5)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')

x_area = np.arange(0, 10, 0.1)
y1 = np.sin(x_area)
y2 = np.sin(x_area) + 0.5
plt.subplot(2, 3, 6)
plt.stackplot(x_area, y1, y2, labels=['y1', 'y2'], colors=['#1f77b4', '#ff7f0e'])
plt.legend(loc='upper left')
plt.title('Stacked Area Plot')

plt.tight_layout()
plt.show()
