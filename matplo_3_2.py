import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 30, 25, 20])
y2 = np.array([18, 28, 7, 55])
y3 = np.array([5, 24, 45, 10])

#propiedades fontsize, family, fontweight = bold,
plt.title("Clase")
plt.xlabel("Average Pulse",)

plt.ylabel("Calorie Burnage")

plt.plot(x, y1)

plt.plot(x, y2)

plt.plot(x, y3)

plt.xticks(x)
plt.tick_params(axis = 'both', colors = 'red')

plt.show()