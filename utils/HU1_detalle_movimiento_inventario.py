def limpiar_simulacion_inventario(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    columnas_numericas = ["id_detalle", "id_movimiento", "id_productos", "cantidad", "precio_unitario"]
    
    for col in columnas_numericas:
        data_frame_limpio[col] = pd.to_numeric(data_frame_limpio[col], errors='coerce')

    # Evaluar valores permitidos (Reglas de negocio)
    # 1. Los IDs deben ser positivos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_detalle"] > 0]
    
    # 2. La cantidad y precio deben ser mayores a 0 para ser un movimiento válido
    data_frame_limpio = data_frame_limpio[data_frame_limpio["cantidad"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["precio_unitario"] > 0]

    # Rutina para evaluar novedades (Campos obligatorios)
    # Si falta cualquier dato esencial de la tabla, se elimina la fila
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_numericas)

    # Elimina filas duplicadas (Registros exactamente iguales)
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio