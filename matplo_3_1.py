import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


font2 = {'family':'Arial','color':'darkred','size':10}


plt.plot(x, y)

plt.title("Sports Watch Data")

plt.xlabel("Average Pulse", family = 'serif',color ='blue',size = 10)

plt.ylabel("Calorie Burnage", fontdict = font2)

plt.show()

