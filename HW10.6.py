import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation
from matplotlib import cm


def capture_points():
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)), label='Sine Wave')
    ax.set_title('Click on the plot to capture points')

    points = plt.ginput(n=-1, timeout=0)
    for point in points:
        ax.plot(point[0], point[1], 'ro')
        ax.text(point[0], point[1], f'({point[0]:.2f}, {point[1]:.2f})', fontsize=12)

    plt.show()


def interactive_slider():
    fig, ax = plt.subplots()
    ax.set_title("Interactive Sine Wave with Slider")

    x = np.linspace(0, 10, 100)
    line, = ax.plot(x, np.sin(x), label="y = sin(x)")

    def update(val):
        line.set_ydata(np.sin(x + val))
        fig.canvas.draw_idle()

    ax_slider = plt.axes([0.25, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider = Slider(ax_slider, 'Shift', -10, 10, valinit=0)
    slider.on_changed(update)

    plt.show()


def datacursor_example():
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y, label='Sine Curve')

    plt.title("Click to explore points interactively")
    plt.gca().set_title('Click on the line')

    cursor = plt.gca().datacursormode(True)
    plt.show()


def animated_line_plot():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 1)
    ax.set_title("Animated Line Plot")

    line, = ax.plot([], [], 'r-', lw=2)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        xdata = np.linspace(0, frame, frame)
        ydata = np.sin(xdata)
        line.set_data(xdata, ydata)
        return line,

    ani = FuncAnimation(fig, update, frames=np.linspace(0.1, 10, 100), init_func=init, blit=True)
    plt.show()


def plot3_comet3():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    t = np.linspace(0, 10, 100)
    x = np.sin(t)
    y = np.cos(t)
    z = t

    ax.plot3D(x, y, z, 'blue', label='3D trajectory')
    ax.set_title("3D Trajectory and Animation")

    comet, = ax.plot([], [], [], 'ro')

    def update_comet(num):
        comet.set_data(x[:num], y[:num])
        comet.set_3d_properties(z[:num])
        return comet,

    ani = FuncAnimation(fig, update_comet, frames=range(1, len(t)), blit=True)
    plt.show()


capture_points()
interactive_slider()
datacursor_example()
animated_line_plot()
plot3_comet3()
