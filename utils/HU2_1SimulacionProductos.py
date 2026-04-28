import random 
def generar_productos(numero_registros):

    nombres = ["ProductoA", "ProductoB", "ProductoC", "ProductoD"]
    categorias = ["Categoria1", "Categoria2", "Categoria3"]
    precios = [10.99, 20.50, 15.75, 5.00]
    stock = [100, 200, 150, 50]

    productos = []

    for _ in range(numero_registros):
        producto = {
            "id_producto": random.randint(1, 1000),
            "id_movimiento": random.randint(1, 1000),  # FK
            "nombre": random.choice(nombres),
            "categoria": random.choice(categorias),
            "precio": random.choice(precios),
            "stock": random.choice(stock)
        }

        # Inyección de errores controlados
        probabilidadError = random.random()

        if probabilidadError < 0.2:
            producto["id_producto"] = None

        elif probabilidadError < 0.4:
            producto["id_movimiento"] = random.choice([None, -1, 9999])

        elif probabilidadError < 0.6:
            producto["categoria"] = random.choice(["categoria1", "categoria2", "otro"])

        elif probabilidadError < 0.75:
            producto["precio"] = random.choice([None, -10.99])

        elif probabilidadError < 0.9:
            producto["stock"] = random.choice([None, -50])

        productos.append(producto)

    return productos