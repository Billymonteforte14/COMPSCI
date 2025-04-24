import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure()
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.xlabel('x-axis', fontsize=14, fontname='Arial', color='blue')
plt.ylabel('y-axis', fontsize=14, fontname='Arial', color='blue')
plt.title('Sine and Cosine Functions', fontsize=16, fontname='Arial', color='red')
plt.legend()
ax = plt.gca()
ax.set_xlim([0, 2 * np.pi])
ax.set_ylim([-1.5, 1.5])
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
ax.grid(True)

plt.text(np.pi, 0, 'Midpoint', fontsize=12, ha='center')
plt.annotate('Peak', xy=(np.pi/2, 1), xytext=(1, 1.3),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

fig, axs = plt.subplots(2, 2, figsize=(10, 6))
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('sin(x)')
axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title('cos(x)')
axs[1, 0].plot(x, np.sin(2*x))
axs[1, 0].set_title('sin(2x)')
axs[1, 1].plot(x, np.cos(2*x))
axs[1, 1].set_title('cos(2x)')
plt.tight_layout()
plt.show()
