import matplotlib.pyplot as plt
import numpy as np

#grid() basicamente ayuda a tener una mejor lectura de lineas

x = [1,2,3,4,5]
y = [5, 15, 25, 30, 40]

plt.plot(x,y)

#puede ser unicamente y o x, o ambas
#propiedades => linewidth, color, linestyle 'dashed, dashdot, dotted'
plt.grid(axis='both', color = 'green', linestyle = 'dashdot', linewidth = 1.5)

plt.show()