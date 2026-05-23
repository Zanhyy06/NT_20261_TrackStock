import pandas as pd

from notebook.graficoMovimientoInventario import graficar_linea_movimientos, graficar_torta_tipo


def transformar_movimiento_inventario(data_frame_limpio):
    print("Transformando el DataFrame de movimiento de inventario...")
    print("Columnas:", data_frame_limpio.columns.tolist())

    # 1. Cantidad de movimientos por fecha (útil para gráficos de líneas)
    filtro1 = data_frame_limpio[data_frame_limpio["fecha"].dt.year > 1900]
    agrupacion1 = filtro1.groupby("fecha")["id_movimiento"].count().reset_index(name="cantidad_movimientos")
    print(agrupacion1)
    graficar_linea_movimientos(
        datos_agrupados=agrupacion1,
        columna_fecha="fecha",
        columna_valores="cantidad_movimientos",
        titulo="Cantidad de movimientos por fecha",
        color_linea="#2196F3",
        nombre_archivo="movimientos_por_fecha.png"
    )

    # 2. Cantidad de movimientos por tipo (útil para gráficos de barras o pastel)
    agrupacion2 = data_frame_limpio.groupby("tipo")["id_movimiento"].count().reset_index(name="cantidad")
    print(agrupacion2)
    graficar_torta_tipo(
        datos_agrupados=agrupacion2,
        columna_etiquetas="tipo",
        columna_valores="cantidad",
        titulo="Distribución de movimientos por tipo",
        nombre_archivo="movimientos_por_tipo.png"
    )
