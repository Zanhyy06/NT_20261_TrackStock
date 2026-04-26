import random

tipos = ["Proveedor", "Cliente"]
nombres = ["Distribuciones Andinas", "Comercial del Norte", "Suministros Globales",
           "Importadora del Valle", "Proveedores Unidos", "TechSupply SAS",
           "Logistica Express", "Mercantil del Sur", "Abastecedores Nacionales",
           "Grupo Comercial XYZ"]
sufijos = ["", " SAS", " SA", " Ltda", " Corp"]
dominios = ["gmail.com", "hotmail.com", "empresa.co", "outlook.com", "yahoo.com"]
ciudades = ["Medellin", "Bogota", "Cali", "Barranquilla", "Cartagena",
            "Pereira", "Manizales", "Bucaramanga", "Cucuta", "Ibague"]
vias = ["Calle", "Carrera", "Avenida", "Diagonal", "Transversal"]
prefijos = ["300", "301", "310", "311", "312", "313", "314", "315", "316", "320"]


def generar_usuarios(cantidad):
    usuarios = []
    for i in range(1, cantidad + 1):
        nombre = random.choice(nombres) + random.choice(sufijos)
        slug = nombre.lower().replace(" ", "").replace("&", "")[:12]
        correo = slug + "@" + random.choice(dominios)
        telefono = random.choice(prefijos) + str(random.randint(1000000, 9999999))
        nit = str(random.randint(800000000, 999999999)) + "-" + str(random.randint(0, 9))
        via = random.choice(vias)
        direccion = via + " " + str(random.randint(1, 120)) + " #" + str(random.randint(1, 99)) + "-" + str(random.randint(1, 99)) + ", " + random.choice(ciudades)

        usuario = {
            "id_usuario": i,
            "tipo": random.choice(tipos),
            "nombre_empresa": nombre,
            "documento_nit": nit,
            "telefono": telefono,
            "correo": correo,
            "direccion": direccion
        }

        # Inyectando errores controlados
        probabilidad = random.random()
        if probabilidad < 0.05:
            usuario["correo"] = None
        elif probabilidad < 0.10:
            usuario["telefono"] = None
        elif probabilidad < 0.15:
            usuario["tipo"] = random.choice(["proveedor", "cliente", "OTRO", None])
        elif probabilidad < 0.20:
            usuario["documento_nit"] = None
        elif probabilidad < 0.25:
            usuario["nombre_empresa"] = "  " + nombre.upper() + "  "
        elif probabilidad < 0.30:
            usuario["direccion"] = None

        usuarios.append(usuario)
    return usuarios


def exportar(usuarios, csv_path, json_path):
    df = pd.DataFrame(usuarios)
    df.to_csv(csv_path, index=False, encoding="utf-8")
    print(f"[OK] CSV exportado -> {csv_path}  ({len(df)} filas)")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=2, default=str)
    print(f"[OK] JSON exportado -> {json_path}  ({len(usuarios)} registros)")

    return df


if __name__ == "__main__":
    random.seed(42)
    datos = generar_usuarios(1200)
    df = exportar(datos, "usuarios.csv", "usuarios.json")

    print("\n-- Vista previa --")
    print(df.head(5).to_string(index=False))
    print(f"\nTotal registros : {len(df)}")
    print(f"Total columnas  : {len(df.columns)}")
    print(f"Columnas        : {list(df.columns)}")
