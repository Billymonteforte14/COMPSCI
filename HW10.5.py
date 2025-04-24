import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig = plt.figure(figsize=(18, 10))
ax1 = fig.add_subplot(231, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=5)
ax1.set_title('3D Surface Plot')

ax2 = fig.add_subplot(232, projection='3d')
mesh = ax2.plot_wireframe(X, Y, Z, color='black')
ax2.set_title('Wireframe Mesh Plot')

ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')
ax3.set_title('Shaded Surface with Plasma Colormap')
fig.colorbar(ax3.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none'), ax=ax3, shrink=0.5, aspect=5)

ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(X, Y, Z, cmap='coolwarm')
ax4.contour3D(X, Y, Z, 50, cmap='binary')
ax4.set_title('Surface with Contour3D')

ax5 = fig.add_subplot(235, projection='3d')
ax5.plot_surface(X, Y, Z, cmap='inferno')
ax5.set_title('Rotation Animation')
for angle in range(0, 360, 10):
    ax5.view_init(30, angle)
    plt.pause(0.01)

plt.tight_layout()
plt.show()
