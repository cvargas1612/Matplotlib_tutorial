import numpy as np
import matplotlib.pyplot as plt

#Bar char, esta ves circular, como si fueran pedazos de pizza para representar datos

categorias = np.array(["Escuela", "Colegio", "Tecnico", "Universitario"])

valores = np.array([325, 250, 125, 173])

colores = ["red", "yellow", "blue", "green"]

#plt.pie(valores)

#plt.pie(valores, labels=categorias)

#esto me muestra el porcentaje
# se puede agregar explode = [0,0,0,0] y aumentar cada 0.1, shadow = true, startangle
plt.pie(valores, labels=categorias, autopct= "%1.1f%%", explode = (0.1,0,0,0), shadow = True, startangle = 180, colors = colores)

plt.title("Estudiantes")

plt.show()