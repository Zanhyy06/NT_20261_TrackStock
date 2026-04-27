import pandas as pd

#zona para importar simulaciones
from utils.HU1SimulacionMovimientoinventario import generar_movimientos
from utils.HU1SimulacionDetalleMovimientoInventario import generar_detalle_movimiento
from utils.HU1SimulacionUsuarios import generar_usuarios    
from utils.HU2_1SimulacionProductos import generar_productos    


#zona para importar limpiezas
from notebook.HU1_limpiezaMovimientoinventario import limpiar_datos
from notebook.HU1_limpiezaDetalleMovimientoInventario import limpiar_datos_detalle
from notebook.HU1_limpiezaUsuario import limpiar_usuarios
from notebook.HU2_1_limpiezaProductos import limpiar_productos


#Creando las simulaciones
simulaciones = generar_movimientos(10)
simulacion_detalle = generar_detalle_movimiento(10)
simulacion_usuarios = generar_usuarios(10)
simulacion_productos = generar_productos(10)



#Ordenando las simulaciones
simulaciones_ordenadas=pd.DataFrame(simulaciones)
simulaciones_detalle_ordenadas=pd.DataFrame(simulacion_detalle)
simulacion_usuarios_ordenadas=pd.DataFrame(simulacion_usuarios)
simulacion_productos_ordenadas=pd.DataFrame(simulacion_productos)   


#limpiando el set de datos
simulaciones_limpias = limpiar_datos(simulaciones_ordenadas)
simulaciones_detalle_limpias = limpiar_datos_detalle(simulaciones_detalle_ordenadas)
simulacion_productos_limpias = limpiar_productos(simulacion_productos_ordenadas)
simulacion_usuarios_limpias = limpiar_usuarios(simulacion_usuarios_ordenadas)
print(simulacion_usuarios_limpias)
print(simulaciones_limpias)
print(simulaciones_detalle_limpias)
print(simulacion_productos_limpias)
