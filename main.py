import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

"""
Fourier Series
f(t) = A_0 + \sum_{n=1}^{\infty} \left(A_n \cos\left(\frac{\pi nt}{L}\right) + B_n \sin\left(\frac{\pi nt}{L}\right)\right)
A_0 = \frac{1}{2L} \int_{-L}^{L} f(t) \, dt
A_n = \frac{1}{L} \int_{-L}^{L} f(t) \cos\left(\frac{\pi nt}{L}\right) \, dt
B_n = \frac{1}{L} \int_{-L}^{L} f(t) \sin\left(\frac{\pi nt}{L}\right) \, dt
"""
# Create linear space
try:
    L = float(input("Enter period (e.g. 3.14): "))
except ValueError:
    print("The input is not an float.")
    exit()
try:
    granularity = int(input("Enter granularity (e.g. 200): "))
except ValueError:
    print("The input is not an integer.")
    exit()
dx = L / granularity
x = np.arange(-L, L + dx, dx)

# Get user input for the function
user_function = input("Enter a Python expression for the function f(x): ")
try:
    exec(f"f = {user_function}")
except Exception as e:
    print(f"Error: {e}")
    exit()

# Initialize The initial Term and Fourier Series
fourier_series = np.zeros_like(x)
A0 = (1 / (2 * L)) * np.sum(f) * dx
fourier_series += A0

try:
    k = int(input("Enter the number of terms of the sum: "))
except ValueError:
    print("The input is not an integer.")
    exit()

for n in range(1, k + 1):
    An = (1 / L) * np.sum(f * np.cos(np.pi * n * x / L)) * dx
    Bn = (1 / L) * np.sum(f * np.sin(np.pi * n * x / L)) * dx
    fourier_series += An * np.cos(np.pi * n * x / L) + Bn * np.sin(np.pi * n * x / L)

# Create the main plot
fig, ax = plt.subplots()
ax.plot(x, f, "k", label="Original Function")
ax.plot(x, fourier_series, "r", label="Fourier Series")
ax.set_xlim([-4.0, 4.0])
ax.set_ylim([-4.0, 4.0])
ax.legend()
ax.set_title(f"Fourier Series for the function {user_function} \n with period {L},granularity {granularity} and {k} terms were summed", wrap=True)

# Create the inset zoomed-in plot
axins = inset_axes(ax, width="40%", height="30%", loc="lower right")
axins.plot(x, f, "k")
axins.plot(x, fourier_series, "r")
axins.set_xlim(-1.0, 1.0)
axins.set_ylim(0.0, 1.0)
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

# Save the plot as an image
plt.savefig(f"fourier-series-function-{user_function}-period-{L}-granularity-{granularity}-{k}-terms.png")
