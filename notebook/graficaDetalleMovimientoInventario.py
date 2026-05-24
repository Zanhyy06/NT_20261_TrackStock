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


def graficar_barras_cantidad(datos_agrupados, columna_productos, columna_cantidad,
                             titulo="Cantidad de Productos por Detalle", color_barras="#9C27B0",
                             nombre_archivo="barras_cantidad.png", ruta_destino=RUTA_ASSETS):
    # Gráfico de barras vertical - suma de cantidad por cada id_productos
    crear_ruta_si_no_existe(ruta_destino)
    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    area_dibujo.bar(
        datos_agrupados[columna_productos],
        datos_agrupados[columna_cantidad],
        color=color_barras,
        edgecolor="black"
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_productos, fontsize=12)
    area_dibujo.set_ylabel(columna_cantidad, fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de barras cantidad guardado en: {ruta_completa}")


def graficar_mapa_calor_precio(datos_pivoteados, titulo="Matriz de Precios Unitarios",
                               paleta_colores="YlOrRd", nombre_archivo="mapa_calor_precio.png",
                               ruta_destino=RUTA_ASSETS):
    # Gráfico de mapa de calor - densidad de precio_unitario por producto y movimiento
    crear_ruta_si_no_existe(ruta_destino)
    figura, area_dibujo = plt.subplots(figsize=(10, 6))

    sns.heatmap(
        datos_pivoteados,
        annot=True,
        fmt=".1f",
        cmap=paleta_colores,
        linewidths=0.5,
        ax=area_dibujo
    )
    
    area_dibujo.set_title(titulo, fontsize=14, pad=15)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Mapa de calor precio guardado en: {ruta_completa}")