import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 13]

plt.plot(x, y, marker='o', linestyle='-', color='purple', markerfacecolor='orange')

plt.xlabel("Days of the Week")
plt.ylabel("Study Hours")
plt.title("My Study Hours Over a Week")

plt.show()
"One interesting thing I learned while messing around with Matplotlib is how easy it is to change colors and styles."
"I tried making the line purple and the dots orange, and it actually looked pretty cool. Also, adding labels"
"and a title made the graph way easier to understand—before that, it was just random points on a screen"

