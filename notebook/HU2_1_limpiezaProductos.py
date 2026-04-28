import pandas as pd

def limpiar_productos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()
    # Procesando los textos del DF SUCIO
    # 1. Limpiando textos (espacios y formato)  
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].astype("string").str.strip()
    data_frame_limpio["categoria"] = data_frame_limpio["categoria"].astype("string").str.strip().str.capitalize()           
    # 2. Control de valores esperados
    valores_esperados_categoria = ["Categoria1", "Categoria2", "Categoria3"]                
    data_frame_limpio["categoria"] = data_frame_limpio["categoria"].where(
        data_frame_limpio["categoria"].isin(valores_esperados_categoria),
        pd.NA
    )   
    # Limpieza de datos numericos
    # 1. Verificar que los numeros si sean numeros  
    data_frame_limpio["id_producto"] = pd.to_numeric(data_frame_limpio["id_producto"], errors="coerce")
    data_frame_limpio["id_movimiento"] = pd.to_numeric(data_frame_limpio["id_movimiento"], errors="coerce")
    data_frame_limpio["precio"] = pd.to_numeric(data_frame_limpio["precio"], errors="coerce")
    data_frame_limpio["stock"] = pd.to_numeric(data_frame_limpio["stock"], errors="coerce")
    # 2. Verifiquemos valores numericos esperados   
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_producto"] > 0] 
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_movimiento"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["precio"] >= 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["stock"] >= 0]
    # NOVEDADES de datos vacios     
    columnas_obligatorias = ["id_producto","id_movimiento","nombre","categoria"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)
    # Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()
    return data_frame_limpio
    