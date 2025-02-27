import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

random_numbers = np.random.rand(5)
print("Random Numbers:", random_numbers)

data = {
    "Name": ["William", "James", "Harden"],
    "Age": [19, 35, 36],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print("\nSimple Table:\n", df)

categories = ["A", "B", "C"]
values = [10, 15, 7]

plt.bar(categories, values, color=['blue', 'red', 'yellow'])
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Simple Bar Chart")
plt.show()
