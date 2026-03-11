import numpy as np
import matplotlib.pyplot as plt

#scatter graph
#           se utiliza para establecer una relacion entre dos datos

x = [0,1,1,2,3,4,5,6,7,7,8] # Horas estudiadas
y = [55,60,62,65,62,68,70,75,82,85,87] # Notas
y2 = [15,40,68,75,82,88,91,95,98,99,100] # Notas


#parametros color=,
#   alpha = 0.0 transparencia
#   s = 0 tamanno de los puntos
# label = "nombre" y llamar plt.legend()


plt.scatter(x,y, alpha=0.5, s = 15, label = "Estudiantes")
plt.scatter(x,y2, alpha=0.5, s = 15, label = "Profesores")
plt.legend()


plt.xlabel("Horas estudiandas")
plt.ylabel("Notas")

plt.title("Notas por hora")

plt.show()