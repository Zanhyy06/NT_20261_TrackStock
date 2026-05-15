import pandas as pd
def transformar_usuario(data_frame_limpio):
    print("Transformando el DataFrame de usuarios...")

    #1. Filtro por tipo de usuario y agrupación por nombre  Útil para gráficos de barras
    filtro1 = data_frame_limpio.query("tipo == 'cliente'")
    agrupacion1 = filtro1.groupby("nombre")["id_usuario"].count().reset_index(name="cantidad_usuarios")
    print(agrupacion1)

    #2. Filtro por tipo de usuario y agrupación por documento Útil para analizar tipos de identificación más frecuentes
    filtro2 = data_frame_limpio.query("tipo == 'empleado'")
    agrupacion2 = filtro2.groupby("documento")["id_usuario"].count().reset_index(name="cantidad_documentos")
    print(agrupacion2)