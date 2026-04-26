import random

def generar_usuarios(numero_registros):

    tipos = ["Proveedor", "Cliente"]
    nombres = ["Carlos", "Ana", "EmpresaX", "Luis", "Maria"]
    documentos = ["123", "456", "789", "101112"]
    telefonos = ["3001234567", "3109876543", "3201112233"]
    correos = ["test@mail.com", "user@mail.com", "empresa@mail.com"]
    direcciones = ["Calle 1", "Carrera 2", "Av 3"]

    usuarios = []

    for _ in range(numero_registros):
        usuario = {
            "id_usuario": random.randint(1, 1000),
            "id_movimiento": random.randint(1, 1000),  # FK
            "tipo": random.choice(tipos),
            "nombre": random.choice(nombres),
            "documento": random.choice(documentos),
            "telefono": random.choice(telefonos),
            "correo": random.choice(correos),
            "direccion": random.choice(direcciones)
        }

        # Inyección de errores controlados
        probabilidadError = random.random()

        if probabilidadError < 0.2:
            usuario["id_usuario"] = None

        elif probabilidadError < 0.4:
            usuario["id_movimiento"] = random.choice([None, -1, 9999])

        elif probabilidadError < 0.6:
            usuario["tipo"] = random.choice(["proveedor", "cliente", "otro"])

        elif probabilidadError < 0.75:
            usuario["correo"] = random.choice([None, "correo_invalido"])

        elif probabilidadError < 0.9:
            usuario["telefono"] = random.choice([None, "abc123"])

        usuarios.append(usuario)

    return usuarios