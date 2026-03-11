import matplotlib.pyplot as plt
import numpy as np

x = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

corredor1 = np.array([15, 25, 42, 68, 80, 96, 126, 150, 161, 181])
corredor2 = np.array([12, 30, 56, 74, 91, 115, 125, 142, 160, 179])

# se puede ahorrar tiempo teniendo esto
line_styles = dict(marker='o', markersize=10, markerfacecolor='cyan', linestyle='dashed')

#para usar line_style se usa ** al inicio, que quiere decir desempaqueta la informacion
plt.plot(x, corredor1, **line_styles)

plt.plot(x, corredor2, marker='o', markersize=10, markerfacecolor='#9459d4', linestyle='dashed')

plt.show()