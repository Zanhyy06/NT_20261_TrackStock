# ---------------------------------------------
#  HU 3 — Simulación y exportación de datos
#  Tabla: USUARIO
# ---------------------------------------------

TIPOS = ["Proveedor", "Cliente"]  # lista de los dos tipos de usuario válidos en el sistema

NOMBRES_EMPRESAS = [  # banco de nombres de empresas base para generar datos sintéticos
    "Distribuciones Andinas", "Comercial del Norte", "Suministros Globales",
    "Importadora del Valle", "Proveedores Unidos", "TechSupply SAS",
    "Logística Express", "Mercantil del Sur", "Abastecedores Nacionales",
    "Grupo Comercial XYZ", "Inversiones Omega", "Soluciones Empresariales",
    "Distribuidora Latina", "Almacenes Progreso", "Red de Proveedores",
    "Corporación Integral", "Servicios y Bienes SA", "Cadena de Valor SAS",
    "Nexo Comercial", "GlobalTrade Colombia",
]

DOMINIOS_CORREO = ["gmail.com", "hotmail.com", "empresa.co", "outlook.com", "yahoo.com"]  # dominios posibles para los correos generados

CIUDADES = [  # ciudades colombianas que se usan al construir direcciones
    "Medellín", "Bogotá", "Cali", "Barranquilla", "Cartagena",
    "Pereira", "Manizales", "Bucaramanga", "Cúcuta", "Ibagué",
]

TIPO_VIAS = ["Calle", "Carrera", "Avenida", "Diagonal", "Transversal"]  # prefijos de vía para armar direcciones colombianas


def _empresa_aleatoria() -> str:  # función auxiliar que devuelve un nombre de empresa aleatorio con sufijo
    base = random.choice(NOMBRES_EMPRESAS)  # elige un nombre base del listado
    sufijo = random.choice(["", " SAS", " SA", " Ltda", " & Cía", " Corp"])  # elige un sufijo jurídico aleatorio (puede ser vacío)
    return base + sufijo  # concatena nombre base y sufijo para formar el nombre completo


def _nit_aleatorio() -> str:  # función auxiliar que genera un NIT simulado con dígito de verificación
    numero = random.randint(800_000_000, 999_999_999)  # genera el número principal del NIT en el rango válido
    digito = random.randint(0, 9)  # genera el dígito de verificación
    return f"{numero}-{digito}"  # devuelve el NIT formateado como "XXXXXXXXX-D"


def _telefono_aleatorio() -> str:  # función auxiliar que genera un número de celular colombiano simulado
    prefijos = ["300", "301", "310", "311", "312", "313", "314", "315",
                "316", "317", "318", "319", "320", "321", "350"]  # lista de prefijos de operadores móviles colombianos
    return random.choice(prefijos) + str(random.randint(1_000_000, 9_999_999))  # une prefijo con 7 dígitos aleatorios


def _correo_aleatorio(nombre_empresa: str) -> str:  # función auxiliar que deriva un correo desde el nombre de la empresa
    slug = nombre_empresa.lower().replace(" ", "").replace("&", "")[:12]  # convierte el nombre a minúsculas, quita espacios y "&", toma máx 12 chars
    dominio = random.choice(DOMINIOS_CORREO)  # elige un dominio aleatorio de la lista
    return f"{slug}@{dominio}"  # arma la dirección de correo completa


def _direccion_aleatoria() -> str:  # función auxiliar que construye una dirección colombiana simulada
    via = random.choice(TIPO_VIAS)  # elige el tipo de vía (Calle, Carrera, etc.)
    num1 = random.randint(1, 120)  # número principal de la vía
    num2 = random.randint(1, 99)   # primer componente del número de cruce
    num3 = random.randint(1, 99)   # segundo componente del número de cruce
    ciudad = random.choice(CIUDADES)  # ciudad aleatoria de la lista
    return f"{via} {num1} #{num2}-{num3}, {ciudad}"  # devuelve la dirección formateada


def generar_usuarios(cantidad: int = 1000) -> list[dict]:
    """Genera `cantidad` registros sintéticos para la tabla USUARIO."""
    usuarios = []  # lista vacía que acumulará los registros generados
    for i in range(1, cantidad + 1):  # itera desde 1 hasta `cantidad` para asignar IDs consecutivos
        empresa = _empresa_aleatoria()  # genera el nombre de empresa para este registro
        usuario = {  # construye el diccionario con todos los campos del usuario
            "id_usuario": i,  # identificador único secuencial
            "tipo": random.choice(TIPOS),  # tipo de usuario: Proveedor o Cliente
            "nombre_empresa": empresa,  # nombre de la empresa generado arriba
            "documento_nit": _nit_aleatorio(),  # NIT simulado
            "telefono": _telefono_aleatorio(),  # teléfono celular simulado
            "correo": _correo_aleatorio(empresa),  # correo derivado del nombre de la empresa
            "direccion": _direccion_aleatoria(),  # dirección física simulada
        }

        # -- Errores controlados (≈30 % de los registros) --
        prob = random.random()  # genera un número flotante entre 0.0 y 1.0 para decidir si se introduce error
        if prob < 0.05:  # 5 % de los casos: correo nulo
            usuario["correo"] = None  # simula un correo faltante
        elif prob < 0.10:  # siguiente 5 %: teléfono nulo
            usuario["telefono"] = None  # simula un teléfono faltante
        elif prob < 0.15:  # siguiente 5 %: tipo de usuario inválido o nulo
            usuario["tipo"] = random.choice(["proveedor", "cliente", "OTRO", None])  # introduce un valor de tipo incorrecto
        elif prob < 0.20:  # siguiente 5 %: NIT nulo
            usuario["documento_nit"] = None  # simula un NIT faltante
        elif prob < 0.25:  # siguiente 5 %: nombre con espacios y en mayúsculas (datos sucios)
            usuario["nombre_empresa"] = "  " + empresa.upper() + "  "  # añade espacios al inicio/fin y pone todo en mayúsculas
        elif prob < 0.30:  # siguiente 5 %: dirección nula
            usuario["direccion"] = None  # simula una dirección faltante

        usuarios.append(usuario)  # agrega el registro (con o sin error) a la lista

    return usuarios  # devuelve la lista completa de registros generados


def exportar(usuarios: list[dict], csv_path: str, json_path: str) -> None:
    df = pd.DataFrame(usuarios)  # convierte la lista de diccionarios en un DataFrame de pandas

    df.to_csv(csv_path, index=False, encoding="utf-8")  # guarda el DataFrame como archivo CSV sin la columna de índice
    print(f"[OK] CSV exportado -> {csv_path}  ({len(df)} filas)")  # confirma en consola la exportación del CSV

    with open(json_path, "w", encoding="utf-8") as f:  # abre (o crea) el archivo JSON en modo escritura con codificación UTF-8
        json.dump(usuarios, f, ensure_ascii=False, indent=2, default=str)  # escribe la lista de usuarios en formato JSON con indentación de 2 espacios
    print(f"[OK] JSON exportado -> {json_path}  ({len(usuarios)} registros)")  # confirma en consola la exportación del JSON

    return df  # devuelve el DataFrame para uso posterior (ej. vista previa)


if __name__ == "__main__":  # bloque que solo se ejecuta cuando el script corre directamente (no al importarlo)
    random.seed(42)  # fija la semilla aleatoria para que los datos generados sean reproducibles
    datos = generar_usuarios(1200)  # genera 1200 registros sintéticos de usuarios
    df = exportar(datos, "usuarios.csv", "usuarios.json")  # exporta los datos a CSV y JSON y obtiene el DataFrame

    print("\n-- Vista previa --")  # imprime encabezado de la sección de vista previa
    print(df.head(5).to_string(index=False))  # muestra las primeras 5 filas del DataFrame sin el índice
    print(f"\nTotal registros : {len(df)}")  # imprime el total de filas generadas
    print(f"Total columnas  : {len(df.columns)}")  # imprime el número de columnas del DataFrame
    print(f"Columnas        : {list(df.columns)}")  # imprime los nombres de todas las columnas