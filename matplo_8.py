import matplotlib.pyplot as plt
import numpy as np

#Histogram una representacion de datos que puede ser cuantitativa, para agruparlos y clasificarlos por rangos

#loc indica la media de numeros generados
#scale que tanto se desviaran los numeros de la media
#size cuantos numeros

puntaje = np.random.normal(loc=80, scale=10, size=100)
# esto nos permite limitar que tan bajo y alto pueden desviarse los numeros

puntaje = np.clip(puntaje, 0, 100)

#parametros
#bins = 10 cuantas barras vamos a ver
#color
#edgecolor
plt.hist(puntaje)

plt.show()
