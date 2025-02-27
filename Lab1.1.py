import numpy as np
import matplotlib.pyplot as plt

random_numbers = np.random.rand(10)

mean_value = np.mean(random_numbers)
sum_value = np.sum(random_numbers)

print("Random Numbers:", random_numbers)
print("Mean:", mean_value)
print("Sum:", sum_value)


plt.plot(random_numbers, marker='o', linestyle='-', color='b', label='Random Numbers')
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Line Plot of Random Numbers")
plt.legend()
plt.grid()
plt.show()
