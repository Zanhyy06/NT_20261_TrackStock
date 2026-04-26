import pandas as pd

def limpiar_usuarios(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()


    # Procesando los textos del DF SUCIO
    # 1. Limpiando textos (espacios y formato)
    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].astype("string").str.strip().str.capitalize()
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].astype("string").str.strip()
    data_frame_limpio["documento"] = data_frame_limpio["documento"].astype("string").str.strip()
    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].astype("string").str.strip()
    data_frame_limpio["correo"] = data_frame_limpio["correo"].astype("string").str.strip().str.lower()
    data_frame_limpio["direccion"] = data_frame_limpio["direccion"].astype("string").str.strip()

    # 2. Control de valores esperados
    valores_esperados_tipo = ["Proveedor", "Cliente"]
    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].where(
        data_frame_limpio["tipo"].isin(valores_esperados_tipo),
        pd.NA
    )
    
    # Limpieza de datos numericos
    # 1. Verificar que los numeros si sean numeros
    data_frame_limpio["id_usuario"] = pd.to_numeric(data_frame_limpio["id_usuario"], errors="coerce")
    data_frame_limpio["id_movimiento"] = pd.to_numeric(data_frame_limpio["id_movimiento"], errors="coerce")

    # 2. Verifiquemos valores numericos esperados
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_usuario"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_movimiento"] > 0]

    # Limpieza de formatos especiales
    # Validar correo (muy básico)
    data_frame_limpio["correo"] = data_frame_limpio["correo"].where(
        data_frame_limpio["correo"].str.contains("@", na=False),
        pd.NA
    )

    # Validar telefono (solo numeros)
    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].where(
        data_frame_limpio["telefono"].str.isnumeric(),
        pd.NA
    )

    # NOVEDADES de datos vacios
    columnas_obligatorias = ["id_usuario","id_movimiento","tipo","nombre","documento"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio