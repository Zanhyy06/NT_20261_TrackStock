import requests

def consumo_productos():
    url="http://localhost:8080/producto"
    repuesta=requests.get(url)
    repuesta.raise_for_status()
    datos=repuesta.json()
    print(datos)

consumo_productos()