import random
import pandas as pd
from datetime import datetime, timedelta

def generar_simulacion_inventario(numeroSimulaciones):
    # Datos base para la simulación
    ids_movimientos = [10, 20, 30]
    ids_productos = [500, 600, 700]
    precios = [15000, 50000, 120000]
    
    simulaciones = []
    
    for _ in range(numeroSimulaciones):
        simulacion = {
            "id_detalle": random.randint(1, 1000),
            "id_movimiento": random.choice(ids_movimientos),
            "id_productos": random.choice(ids_productos),
            "cantidad": random.randint(1, 100),
            "precio_unitario": random.choice(precios)
        }

        # Inyectando errores controlados (Manteniendo tu lógica original)
        probabilidadError = random.random()
        
        if probabilidadError < 0.2:
            simulacion["id_detalle"] = None
        elif probabilidadError < 0.4:
            # Error: ID de producto inexistente o fuera de rango
            simulacion["id_productos"] = random.choice([-99, 0])
        elif probabilidadError < 0.5:
            # Error: Valores económicos inválidos
            simulacion["precio_unitario"] = random.choice([0, -5000, None])
        elif probabilidadError < 0.8:
            # Error: Cantidad nula o errónea
            simulacion["cantidad"] = None
            
        simulaciones.append(simulacion)
        
    return pd.DataFrame(simulaciones)