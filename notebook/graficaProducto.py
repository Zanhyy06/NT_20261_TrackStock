import pandas as pd
# Se importa matplotlib para crear los gráficos
import matplotlib.pyplot as plt
# Se importa seaborn para el mapa de calor con estilo mejorado
import seaborn as sns
# Se importa os para manejar rutas y crear carpetas
import os

# Ruta típica de la carpeta assets en un proyecto React con Vite
RUTA_ASSETS = r"C:\Users\Santhy\Music\Proyecto cesde\Proyecto-gestion-de-inventario\src\assets\graficos"


def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_barras_productos(datos_agrupados, columna_categorias, columna_valores,
                               titulo="Gráfico de productos", color_barras="#2196F3",
                               nombre_archivo="barras_productos.png", ruta_destino=RUTA_ASSETS):
    # Gráfico de barras vertical - cantidad de productos por categoría
    crear_ruta_si_no_existe(ruta_destino)
    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    area_dibujo.bar(
        datos_agrupados[columna_categorias],
        datos_agrupados[columna_valores],
        color=color_barras,
        edgecolor="black"
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_categorias, fontsize=12)
    area_dibujo.set_ylabel(columna_valores, fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de barras productos guardado en: {ruta_completa}")


def graficar_barras_horizontal(datos_agrupados, columna_categorias, columna_valores,
                                titulo="Gráfico horizontal", color_barras="#FF9800",
                                nombre_archivo="barras_horizontal.png", ruta_destino=RUTA_ASSETS):
    # Gráfico de barras horizontal - promedio de precios por categoría
    crear_ruta_si_no_existe(ruta_destino)
    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    area_dibujo.barh(
        datos_agrupados[columna_categorias],
        datos_agrupados[columna_valores],
        color=color_barras,
        edgecolor="black"
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_valores, fontsize=12)
    area_dibujo.set_ylabel(columna_categorias, fontsize=12)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico horizontal guardado en: {ruta_completa}")