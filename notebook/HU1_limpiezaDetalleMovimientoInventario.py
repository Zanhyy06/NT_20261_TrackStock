import pandas as pd

def limpiar_datos_detalle(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # Procesando los textos del DF sucios
    # (En esta tabla no hay campos de texto)
   

    # Limpieza de datos numericos
    # 1. verificar que los numeros si sean numeros
    # HU1 tabla detalle movimiento inventario
    data_frame_limpio["id_detalle"] = pd.to_numeric(data_frame_limpio["id_detalle"], errors="coerce")
    data_frame_limpio["id_movimiento"] = pd.to_numeric(data_frame_limpio["id_movimiento"], errors="coerce")
    data_frame_limpio["id_productos"] = pd.to_numeric(data_frame_limpio["id_productos"], errors="coerce")
    data_frame_limpio["cantidad"] = pd.to_numeric(data_frame_limpio["cantidad"], errors="coerce")
    data_frame_limpio["precio_unitario"] = pd.to_numeric(data_frame_limpio["precio_unitario"], errors="coerce")


    # 2. Verifiquemos los valores numericos esperados
    # HU1 tabla detalle movimiento inventario
    # IDs deben ser positivos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_detalle"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_movimiento"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_productos"] > 0]
    # Valores de negocio
    data_frame_limpio = data_frame_limpio[data_frame_limpio["cantidad"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["precio_unitario"] > 0]


    # Novedades de datos vacios
    # HU1 tabla detalle movimiento inventario
    columnas_obligatorias = ["id_detalle","id_movimiento","id_productos","cantidad","precio_unitario"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # Elimina duplicados
    # HU1 tabla detalle movimiento inventario
    data_frame_limpio = data_frame_limpio.drop_duplicates()


    return data_frame_limpio