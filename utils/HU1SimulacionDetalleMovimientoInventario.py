import random
import pandas as pd

def generar_detalle_movimiento(numero_registros):

    productos = [500, 600, 700]
    precios = [15000, 50000, 120000]
    cantidades = [1, 5, 10, 20]
    detalles = []

    for _ in range(numero_registros):
        detalle = {
            "id_detalle": random.randint(1, 1000),
            "id_movimiento": random.randint(1, 1000),  
            "id_productos": random.choice(productos),
            "cantidad": random.choice(cantidades),
            "precio_unitario": random.choice(precios)
        }

        # Inyectar errores controlados
        probabilidadError = random.random()

        if probabilidadError < 0.2:
            detalle["id_detalle"] = None

        elif probabilidadError < 0.4:
            detalle["id_productos"] = random.choice([None, -10, 9999])

        elif probabilidadError < 0.6:
            detalle["cantidad"] = random.choice([None, -5, 0])

        elif probabilidadError < 0.8:
            detalle["precio_unitario"] = random.choice([None, -1000, 0])

        detalles.append(detalle)

    return pd.DataFrame(detalles)