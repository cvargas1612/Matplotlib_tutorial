import matplotlib.pyplot as plt
import numpy as np

#Figure = es una pizarra de dibujo virtual o canvas
#Ax = es una grafica

#print(plt.subplots(2,2))

datos = np.array([1,2,3,4,5])

#lineas 2
#columnas 2
figure, axes = plt.subplots(2,2)

#parametros
#color
axes[0,0].plot(datos,datos*2)
axes[0,0].set_title('x*2')

axes[0,1].plot(datos,datos**2)
axes[0,1].set_title('x**2')

axes[1,0].plot(datos,datos**3)
axes[1,0].set_title('x**3')

axes[1,1].plot(datos,datos**4)
axes[1,1].set_title('x**4')

#permite acomodar todos los titulos
plt.tight_layout()

plt.show()