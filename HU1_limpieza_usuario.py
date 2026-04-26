import pandas as pd



def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # Procesando los textos del DF SUCIO

    # 1. Limpiando los textos para eliminar espacios y mayusculas
    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].astype("string").str.strip().str.lower().str.title()
    data_frame_limpio["nombre_empresa"] = data_frame_limpio["nombre_empresa"].astype("string").str.strip().str.title()
    data_frame_limpio["correo"] = data_frame_limpio["correo"].astype("string").str.strip().str.lower()
    data_frame_limpio["documento_nit"] = data_frame_limpio["documento_nit"].astype("string").str.strip()

    # 2. Limpiando los textos para controlar valores inesperados
    valores_esperados_tipo = ["Proveedor", "Cliente"]
    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].where(
        data_frame_limpio["tipo"].isin(valores_esperados_tipo),
        pd.NA
    )

    # 3. Validar que el correo tenga @
    data_frame_limpio["correo"] = data_frame_limpio["correo"].where(
        data_frame_limpio["correo"].str.contains("@", na=False),
        pd.NA
    )

    # Limpieza de datos numericos

    # 1. Verificar que los numeros si sean numeros
    data_frame_limpio["id_usuario"] = pd.to_numeric(data_frame_limpio["id_usuario"], errors="coerce")

    # 2. Verificar los valores numericos esperados
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_usuario"] > 0]

    # Relleno de nulos en columnas opcionales
    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].fillna("Sin telefono")
    data_frame_limpio["correo"] = data_frame_limpio["correo"].fillna("Sin correo")
    data_frame_limpio["direccion"] = data_frame_limpio["direccion"].fillna("Sin direccion")
    data_frame_limpio["documento_nit"] = data_frame_limpio["documento_nit"].fillna("Sin documento")

    # NOVEDADES de datos vacios
    columnas_obligatorias = ["id_usuario", "tipo", "nombre_empresa"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio


if __name__ == "__main__":
    random.seed(42)
    datos = generar_usuarios(1200)
    df_sucio = pd.DataFrame(datos)

    df_limpio = limpiar_datos(df_sucio)

    df_limpio.to_csv("usuarios_limpios.csv", index=False, encoding="utf-8")
    print(f"[OK] Dataset limpio exportado  ({len(df_limpio)} filas)")
    print(df_limpio.head(5).to_string(index=False))
