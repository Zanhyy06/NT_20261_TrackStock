import pandas as pd

def transformar_productos(data_frame_limpio):
    print("Transformando el DataFrame de productos...")

    # 1. Productos por categoría (útil para gráfico de barras)
    filtro1 = data_frame_limpio.query("stock > 0")
    agrupacion1 = filtro1.groupby("categoria")["id_producto"].count().reset_index(name="cantidad_productos")
    print(agrupacion1)

    # 2. Promedio de precios por categoría # (útil para gráfico de barras o boxplot)
    filtro2 = data_frame_limpio.query("precio >= 50")
    agrupacion2 = filtro2.groupby("categoria")["precio"].mean().reset_index(name="promedio_precio")
    print(agrupacion2)

    # 3. Stock total por nombre de producto (útil para gráfico horizontal)
    filtro3 = data_frame_limpio.query("stock < 50")
    agrupacion3 = filtro3.groupby("nombre")["stock"].sum().reset_index(name="stock_total")
    print(agrupacion3)