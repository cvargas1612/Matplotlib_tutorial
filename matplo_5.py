import numpy as np
import matplotlib.pyplot as plt

#Bar char, compara datos o categoria de datos por medio de barras

categorias = np.array(["Granos", "Frutas", "Vegetales", "Proteinas", "Lacteos", "Dulces"])

valores = np.array([4, 5, 10, 3, 2, 1])

plt.barh(categorias, valores, color='skyblue')

#en caso de querer que las barras sean horizontales
#plt.barh(categorias, valores, color='skyblue')

plt.title("Consumo diario")
plt.xlabel("Comida")
plt.ylabel("Cantidad")

plt.show()