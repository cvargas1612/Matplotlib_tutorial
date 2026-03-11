import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('pokemon.csv')

#value_counts me regresa la cantidad de cada uno respecto al filtro
#print(df["Type1"].value_counts())

contador_de_tipos = df["Type1"].value_counts()

#parametros
#ascending = true
#color
#edgecolor
plt.barh(contador_de_tipos.index,contador_de_tipos.values)

plt.title('Pokemons por Tipo 1')
plt.xlabel('Cantidad')
plt.ylabel('Tipo')
plt.tight_layout()
plt.show()