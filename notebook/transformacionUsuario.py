import pandas as pd
from notebook.graficaUsuario import graficar_barras, graficar_torta

def transformar_usuario(data_frame_limpio):
    print(data_frame_limpio.columns)

    #1. Filtro por tipo de usuario y agrupación por nombre  Útil para gráficos de barras
    filtro1 = data_frame_limpio.query("tipo == 'Cliente'")
    agrupacion1 = filtro1.groupby("nombre")["id_usuario"].count().reset_index(name="cantidad_usuarios")
    print(agrupacion1)
    graficar_barras(
        datos_agrupados=agrupacion1,
        columna_categorias="nombre",
        columna_valores="cantidad_usuarios",
        titulo="Cantidad de clientes por nombre",
        color_barras="#4CAF50",
        nombre_archivo="usuarios_barras.png"
    )

    #2. Filtro por tipo de usuario y agrupación por documento Útil para analizar tipos de identificación más frecuentes
    filtro2 = data_frame_limpio.query("tipo == 'Cliente'") 
    agrupacion2 = filtro2.groupby("documento")["id_usuario"].count().reset_index(name="cantidad_documentos")
    print(agrupacion2)
    graficar_torta(
        datos_agrupados=agrupacion2,
        columna_etiquetas="documento",
        columna_valores="cantidad_documentos",
        titulo="Tipos de documento en clientes",  
        nombre_archivo="clientes_documento_torta.png"  
    )