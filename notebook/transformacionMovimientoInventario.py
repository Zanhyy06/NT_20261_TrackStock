import pandas as pd

def transformar_movimiento_inventario(data_frame_limpio):
    print("Transformando el DataFrame de movimiento de inventario...")

    # 1. Cantidad de movimientos por fecha (útil para gráficos de líneas)
    filtro1 = data_frame_limpio.query("id_movimiento > 0")
    agrupacion1 = filtro1.groupby("fecha")["id_movimiento"].count().reset_index(name="cantidad_movimientos")
    print(agrupacion1)

    # 2. Cantidad de movimientos por tipo (útil para gráficos de barras o pastel)
    filtro2 = data_frame_limpio.query("tipo == 'entrada'")
    agrupacion2 = filtro2.groupby("tipo")["id_movimiento"].count().reset_index(name="cantidad")
    print(agrupacion2)
    
    # 3. Movimientos realizados por usuario (útil para gráficos horizontales)
    filtro3 = data_frame_limpio.query("id_usuario > 0")
    agrupacion3 = filtro3.groupby("id_usuario")["id_movimiento"].count().reset_index(name="total_movimientos")
    print(agrupacion3)

    # 4. Cantidad de movimientos por fecha y tipo (útil para gráficos de líneas múltiples)
    filtro4 = data_frame_limpio.query("id_movimiento >= 100")
    agrupacion4 = filtro4.groupby(["fecha", "tipo"])["id_movimiento"].count().reset_index(name="cantidad")
    print(agrupacion4)