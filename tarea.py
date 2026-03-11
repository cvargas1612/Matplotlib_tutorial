"""
TAREA: 5 ejercicios de Matplotlib (base: matplo_1 a matplo_10)

Regla:
- Trabaja cada ejercicio en su funcion.
- Descomenta la llamada en main() cuando quieras probarlo.
- Usa solo Matplotlib, NumPy y Pandas (como en los ejemplos).
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def ejercicio_1_version_y_linea_simple():
    """
    Tema base: matplo_1, matplo_2, matplo_2_1
    1. Imprime la version de matplotlib.
    2. Crea una grafica de linea con:
       x = [2023, 2024, 2025, 2026]
       y = [15, 30, 25, 20]
    """
    print("Version de matplotlib:", matplotlib.__version__)

    # TODO: crea la grafica de linea simple y muestra la ventana.
    x = [2023, 2024, 2025, 2026]
    y = [15, 30, 25, 20]
    plt.plot(x, y)
    plt.show()


def ejercicio_2_lineas_estilo_titulo_ejes_grid():
    """
    Tema base: matplo_2_3, matplo_2_4, matplo_3, matplo_3_1, matplo_3_2, matplo_4, matplo_4_1
    1. Grafica 2 lineas en la misma figura (y1 e y2).
    2. Aplica estilo: marker='o', markersize=8, markerfacecolor='cyan', linestyle='dashed'.
    3. Agrega titulo, xlabel, ylabel.
    4. Activa grid solo en eje x con color verde, linea '--', ancho 0.5.
    """
    x = np.array([2023, 2024, 2025, 2026])
    y1 = np.array([15, 30, 25, 20])
    y2 = np.array([18, 28, 7, 55])

    # TODO: grafica y1 e y2 con el estilo indicado.
    plt.plot(x, y1, marker="o", markersize=8, markerfacecolor="cyan", linestyle="dashed")
    plt.plot(x, y2, marker="o", markersize=8, markerfacecolor="cyan", linestyle="dashed")
    plt.title("Comparacion de dos series")
    plt.xlabel("Anio")
    plt.ylabel("Valor")
    plt.grid(axis="x", color="green", linestyle="--", linewidth=0.5)
    plt.show()


def ejercicio_3_barras_y_barras_horizontales_con_pokemon():
    """
    Tema base: matplo_5, matplo_10 (+ pokemon.csv)
    1. Carga pokemon.csv.
    2. Calcula la cantidad de Pokemon por Type1.
    3. Crea una figura con 2 subplots (1 fila, 2 columnas):
       - Izquierda: barras verticales de los 8 tipos mas frecuentes.
       - Derecha: barras horizontales de esos mismos 8 tipos.
    4. Usa titulos y etiquetas de ejes.
    """
    df = pd.read_csv("pokemon.csv")
    top_tipos = df["Type1"].value_counts().head(8)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].bar(top_tipos.index, top_tipos.values, color="skyblue", edgecolor="black")
    axes[0].set_title("Top 8 Type1 (Vertical)")
    axes[0].set_xlabel("Tipo")
    axes[0].set_ylabel("Cantidad")
    axes[0].tick_params(axis="x", rotation=45)

    axes[1].barh(top_tipos.index, top_tipos.values, color="lightcoral", edgecolor="black")
    axes[1].set_title("Top 8 Type1 (Horizontal)")
    axes[1].set_xlabel("Cantidad")
    axes[1].set_ylabel("Tipo")

    plt.tight_layout()
    plt.show()


def ejercicio_4_scatter_e_histograma():
    """
    Tema base: matplo_7, matplo_7_1, matplo_7_2, matplo_7_3, matplo_7_4, matplo_8
    1. Genera datos aleatorios:
       - x, y: enteros entre 0 y 100 (100 puntos)
       - colors: enteros entre 0 y 100
       - sizes: 10 * enteros entre 0 y 100
    2. Crea 2 subplots (1 fila, 2 columnas):
       - Izquierda: scatter con cmap='nipy_spectral', alpha=0.5 y colorbar.
       - Derecha: histograma de 100 puntajes con media 80 y desviacion 10,
         recortados entre 0 y 100.
    """
    x = np.random.randint(100, size=100)
    y = np.random.randint(100, size=100)
    colors = np.random.randint(100, size=100)
    sizes = 10 * np.random.randint(100, size=100)

    puntaje = np.random.normal(loc=80, scale=10, size=100)
    puntaje = np.clip(puntaje, 0, 100)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    sc = axes[0].scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap="nipy_spectral")
    axes[0].set_title("Scatter Aleatorio")
    axes[0].set_xlabel("X")
    axes[0].set_ylabel("Y")
    fig.colorbar(sc, ax=axes[0])

    axes[1].hist(puntaje, bins=10, color="gold", edgecolor="black")
    axes[1].set_title("Histograma de Puntajes")
    axes[1].set_xlabel("Puntaje")
    axes[1].set_ylabel("Frecuencia")

    plt.tight_layout()
    plt.show()


def ejercicio_5_tablero_2x2_integrador():
    """
    Tema base: matplo_9, matplo_9_1, matplo_9_2 + integracion de temas previos
    Crea un tablero 2x2 usando subplots con pokemon.csv:
    - (0,0) Linea: top 10 Pokemon mas pesados (Weight) ordenados ascendente.
    - (0,1) Barras: cantidad por Legendary (0 y 1).
    - (1,0) Scatter: Height vs Weight.
    - (1,1) Pie: top 5 Type1 (por cantidad) + categoria "Otros".
    Agrega titulo general con suptitle y tight_layout.
    """
    df = pd.read_csv("pokemon.csv")
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # (0,0) Linea: top 10 mas pesados
    pesados = df.nlargest(10, "Weight").sort_values("Weight")
    axes[0, 0].plot(pesados["Name"], pesados["Weight"], marker="o")
    axes[0, 0].set_title("Top 10 mas pesados")
    axes[0, 0].set_xlabel("Pokemon")
    axes[0, 0].set_ylabel("Weight")
    axes[0, 0].tick_params(axis="x", rotation=45)

    # (0,1) Barras: Legendary
    leg = df["Legendary"].value_counts().sort_index()
    axes[0, 1].bar(["No legendario", "Legendario"], leg.values, color=["#7fbf7f", "#ff7f7f"])
    axes[0, 1].set_title("Cantidad por Legendary")
    axes[0, 1].set_xlabel("Categoria")
    axes[0, 1].set_ylabel("Cantidad")

    # (1,0) Scatter: Height vs Weight
    axes[1, 0].scatter(df["Height"], df["Weight"], alpha=0.6, color="teal")
    axes[1, 0].set_title("Height vs Weight")
    axes[1, 0].set_xlabel("Height")
    axes[1, 0].set_ylabel("Weight")

    # (1,1) Pie: top 5 Type1 + Otros
    tipo_counts = df["Type1"].value_counts()
    top5 = tipo_counts.head(5)
    otros = tipo_counts.iloc[5:].sum()
    pie_labels = list(top5.index) + ["Otros"]
    pie_values = list(top5.values) + [otros]
    axes[1, 1].pie(pie_values, labels=pie_labels, autopct="%1.1f%%", startangle=90)
    axes[1, 1].set_title("Distribucion Type1")

    plt.suptitle("Dashboard Pokemon - Ejercicio Integrador")
    plt.tight_layout()
    plt.show()


def main():
    """
    Descomenta SOLO el ejercicio que quieras ejecutar.
    """
    # ejercicio_1_version_y_linea_simple()
    # ejercicio_2_lineas_estilo_titulo_ejes_grid()
    # ejercicio_3_barras_y_barras_horizontales_con_pokemon()
    # ejercicio_4_scatter_e_histograma()
    # ejercicio_5_tablero_2x2_integrador()
    pass


if __name__ == "__main__":
    main()
