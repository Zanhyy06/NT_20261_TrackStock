import pandas as pd

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    #Procesando los textos del DF sucios

    #1. Limpiando los textos para eliminar espacios y mayusculas
    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].str.strip().str.capitalize()


    #2. Limpiando los textos para controlar valores inesperados
    valores_esperados_tipo = ["Entrada", "Salida"]
    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].where(
        data_frame_limpio["tipo"].isin(valores_esperados_tipo),pd.NA
    )

    #Limpieza de datos numericos

    #1. verificar que los numeros si sean numeros
    data_frame_limpio["id_movimiento"] = pd.to_numeric(data_frame_limpio["id_movimiento"], errors="coerce")
    data_frame_limpio["id_usuario"] = pd.to_numeric(data_frame_limpio["id_usuario"], errors="coerce")
    data_frame_limpio["id_detalle"] = pd.to_numeric(data_frame_limpio["id_detalle"], errors="coerce")

    #2. Verifiquemos los valores numericos esperados
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_movimiento"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_usuario"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_detalle"] > 0]


    #Limpieza de datos de fecha
    #1. Verificar que el campo si es una fecha
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"])

    #2. Reemplazar fechas que no llegan por una fecha por defecto
    fecha_por_defecto = pd.Timestamp("1900-01-01")
    data_frame_limpio["fecha"] = data_frame_limpio["fecha"].fillna(fecha_por_defecto)

    # Novedades  de datos vacios
    columnas_obligatorias = ["id_movimiento", "id_usuario", "id_detalle", "fecha", "tipo"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)  

    return data_frame_limpio