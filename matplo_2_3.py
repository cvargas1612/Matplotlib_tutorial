import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 30, 25, 20])


#plt.plot(x, y, marker='o')

#markersize puede ser abreviado como ms
#plt.plot(x, y, marker='o', markersize=10)

#usar un color piker para customizar colores
#linestyle hay muchos tipos ejemplo dotted, dashdot, None, solid
#linewidth es otro argumento por default es 1, pero se puede incrementar
#color es para el color de la linea, igual usar color piker para asignar un valor

plt.plot(x, y, marker='o', markersize=10, markerfacecolor='#9459d4', linestyle='dashdot')

plt.show()