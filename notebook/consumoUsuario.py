import requests

def consumo_usuario():
    url="http://localhost:8080/usuario"
    repuesta=requests.get(url)
    repuesta.raise_for_status()
    datos=repuesta.json()
    print(datos)

consumo_usuario()