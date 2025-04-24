import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
y_exp = np.exp(x / (2 * np.pi))

plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.plot(x, y_sin)
plt.title('sin(x)')
plt.subplot(2, 2, 2)
plt.plot(x, y_cos)
plt.title('cos(x)')
plt.subplot(2, 2, 3)
plt.plot(x, y_tan)
plt.ylim(-10, 10)
plt.title('tan(x)')
plt.subplot(2, 2, 4)
plt.plot(x, y_exp)
plt.title('exp(x / 2π)')
plt.tight_layout()
plt.show()

fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=False)
axs[0, 0].plot(x, y_sin)
axs[0, 0].set_title('sin(x)')
axs[0, 1].plot(x, y_cos)
axs[0, 1].set_title('cos(x)')
axs[1, 0].plot(x, y_tan)
axs[1, 0].set_ylim(-10, 10)
axs[1, 0].set_title('tan(x)')
axs[1, 1].plot(x, y_exp)
axs[1, 1].set_title('exp(x / 2π)')
for ax in axs.flat:
    ax.label_outer()
plt.tight_layout()
plt.show()

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
plots = [axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1]]
data = [y_sin, y_cos, y_tan, y_exp]
titles = ['sin(x)', 'cos(x)', 'tan(x)', 'exp(x / 2π)']
for ax, y, title in zip(plots, data, titles):
    ax.plot(x, y)
    ax.set_title(title)
axs[1, 0].set_ylim(-10, 10)
for ax in axs.flat:
    ax.label_outer()
plt.tight_layout()
plt.show()

with PdfPages('multi_panel_plots.pdf') as pdf:
    fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharex=True)
    axs[0, 0].plot(x, y_sin)
    axs[0, 0].set_title('sin(x)')
    axs[0, 1].plot(x, y_cos)
    axs[0, 1].set_title('cos(x)')
    axs[1, 0].plot(x, y_tan)
    axs[1, 0].set_ylim(-10, 10)
    axs[1, 0].set_title('tan(x)')
    axs[1, 1].plot(x, y_exp)
    axs[1, 1].set_title('exp(x / 2π)')
    for ax in axs.flat:
        ax.label_outer()
    plt.tight_layout()
    pdf.savefig(fig)
    plt.close(fig)
