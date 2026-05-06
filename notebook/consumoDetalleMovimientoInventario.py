import requests

def consumo_detalle_movimiento_inventario():
    url="http://localhost:8080/detalle-movimiento"
    repuesta=requests.get(url)
    repuesta.raise_for_status()
    datos=repuesta.json()
    print(datos)

consumo_detalle_movimiento_inventario()