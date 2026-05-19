import pandas as pd

def transformar_detalle_movimiento_inventario (data_frame_limpio):
    print("Transformando el DataFrame de detalle_movimiento_inventario...")

    data_frame_limpio["subtotal"] = data_frame_limpio["cantidad"] * data_frame_limpio["precio_unitario"]

    # 1. Total de cantidad de productos movidos por ID de producto 
    filtro1 = data_frame_limpio.query("cantidad > 0")
    agrupacion1 = filtro1.groupby("id_productos")["cantidad"].sum().reset_index(name="total_cantidad")
    print(agrupacion1)

    # 2. Dinero total acumulado por ID de producto 
    filtro2 = data_frame_limpio.query("subtotal > 0")
    agrupacion2 = filtro2.groupby("id_productos")["subtotal"].sum().reset_index(name="total_dinero")
    print(agrupacion2)

    # 3. Cantidad de transacciones por movimiento principal 
    filtro3 = data_frame_limpio.query("id_movimiento > 0")
    agrupacion3 = filtro3.groupby("id_movimiento")["id_detalle"].count().reset_index(name="cantidad_detalles")
    print(agrupacion3)

    # 4. Precio promedio unitario por ID de producto 
    filtro4 = data_frame_limpio.query("precio_unitario > 0")
    agrupacion4 = filtro4.groupby("id_productos")["precio_unitario"].mean().reset_index(name="precio_promedio")
    print(agrupacion4)