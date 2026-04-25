import pandas as pd

#zona para importar simulaciones
from utils.HU2_simulacion_movimientoinventario import generar_movimientos

#zona para importar limpiezas
from notebook.limpieza import limpiar_datos


#Creando las simulaciones
simulaciones = generar_movimientos(10)


#Ordenando las simulaciones
simulaciones_ordenadas=pd.DataFrame(simulaciones)


#limpiando el set de datos
simulaciones_limpias = limpiar_datos(simulaciones_ordenadas)
print(simulaciones_limpias)