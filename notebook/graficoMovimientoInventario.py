import pandas as pd
# Se importa matplotlib para crear los gráficos
import matplotlib.pyplot as plt
# Se importa seaborn para el mapa de calor con estilo mejorado
import seaborn as sns
# Se importa os para manejar rutas y crear carpetas
import os

RUTA_ASSETS = r"C:\Users\Santhy\Music\Proyecto cesde\Proyecto-gestion-de-inventario\src\assets\graficos"


def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_linea_movimientos(datos_agrupados, columna_fecha, columna_valores,
                                titulo="Movimientos por fecha", color_linea="#2196F3",
                                nombre_archivo="linea_movimientos.png", ruta_destino=RUTA_ASSETS):
    crear_ruta_si_no_existe(ruta_destino)
    figura, area_dibujo = plt.subplots(figsize=(12, 5))

    area_dibujo.plot(
        datos_agrupados[columna_fecha],
        datos_agrupados[columna_valores],
        color=color_linea,
        marker="o",
        linewidth=2,
        markersize=6
    )
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_fecha, fontsize=12)
    area_dibujo.set_ylabel(columna_valores, fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de línea guardado en: {ruta_completa}")


def graficar_torta_tipo(datos_agrupados, columna_etiquetas, columna_valores,
                         titulo="Movimientos por tipo", lista_colores=None,
                         nombre_archivo="torta_tipo.png", ruta_destino=RUTA_ASSETS):
    crear_ruta_si_no_existe(ruta_destino)

    if lista_colores is None:
        lista_colores = ["#4CAF50", "#F44336", "#2196F3", "#FF9800"]

    figura, area_dibujo = plt.subplots(figsize=(8, 8))
    cantidad_categorias = len(datos_agrupados)

    area_dibujo.pie(
        datos_agrupados[columna_valores],
        labels=datos_agrupados[columna_etiquetas],
        autopct="%1.1f%%",
        colors=lista_colores[:cantidad_categorias],
        startangle=90,
        wedgeprops={"edgecolor": "black", "linewidth": 0.5}
    )
    area_dibujo.set_title(titulo, fontsize=14)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico de torta guardado en: {ruta_completa}")