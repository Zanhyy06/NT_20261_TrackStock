import requests

def consumo_movimiento_inventario():
    url="http://localhost:8080/movimiento"
    repuesta=requests.get(url)
    repuesta.raise_for_status()
    datos=repuesta.json()
    print(datos)

consumo_movimiento_inventario()