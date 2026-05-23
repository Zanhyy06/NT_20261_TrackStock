import pandas as pd
from notebook.graficaProducto import graficar_barras_productos, graficar_barras_horizontal

def transformar_productos(data_frame_limpio):
    print("Transformando el DataFrame de productos...")

    # 1. Productos con precio igual o mayor a la mediana - gráfico de barras vertical
    mediana_precio = data_frame_limpio["precio"].median()
    filtro1 = data_frame_limpio[data_frame_limpio["precio"] >= mediana_precio]
    agrupacion1 = filtro1.groupby("categoria")["id_producto"].count().reset_index(name="cantidad_productos")
    print(f"Mediana de precio: {mediana_precio:.2f}")
    print(agrupacion1)
    graficar_barras_productos(
        datos_agrupados=agrupacion1,
        columna_categorias="categoria",
        columna_valores="cantidad_productos",
        titulo=f"Productos con precio mayor o igual a la mediana (${mediana_precio:.2f})",
        color_barras="#2196F3",
        nombre_archivo="productos_por_categoria.png"
    )

     # 2. Promedio de precios por todas las categorías - gráfico de barras horizontal
    filtro2 = data_frame_limpio.groupby("categoria").filter(lambda x: len(x) >= 1)
    agrupacion2 = filtro2.groupby("categoria")["precio"].mean().reset_index(name="promedio_precio")
    print(agrupacion2)
    graficar_barras_horizontal(
        datos_agrupados=agrupacion2,
        columna_categorias="categoria",
        columna_valores="promedio_precio",
        titulo="Promedio de precios por categoría",
        color_barras="#FF9800",
        nombre_archivo="promedio_precios_categoria.png"
    )

    

  