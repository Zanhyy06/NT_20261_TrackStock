# ---------------------------------------------
#  HU 1 — Limpieza del set de datos
#  Tabla: USUARIO
# ---------------------------------------------

CSV_ENTRADA = "usuarios.csv"  # Nombre del archivo CSV de entrada
CSV_SALIDA  = "usuarios_limpios.csv"  # Nombre del archivo CSV de salida limpio

TIPOS_VALIDOS = {"proveedor": "Proveedor", "cliente": "Cliente"}  # Map de valores válidos para el campo tipo


def cargar_datos(csv_path: str) -> pd.DataFrame:
    if os.path.exists(csv_path):  # Comprueba si el archivo de entrada existe
        df = pd.read_csv(csv_path, encoding="utf-8")  # Lee el CSV en un DataFrame
        print(f"[OK] Dataset cargado desde '{csv_path}'  ({len(df)} filas)\n")  # Muestra mensaje con número de filas cargadas
    else:
        print(f"[AVISO] '{csv_path}' no encontrado. Generando datos de prueba...\n")  # Muestra aviso si no existe el archivo
        import random  # Importa random para generar datos de prueba reproducibles
        random.seed(42)  # Establece semilla para generar siempre los mismos datos de prueba
        df = pd.DataFrame(generar_usuarios(1200))  # Genera 1200 usuarios y crea un DataFrame
    return df  # Devuelve el DataFrame cargado o generado


def reportar_nulos(df: pd.DataFrame) -> None:
    print("=" * 50)  # Imprime un separador visual
    print("1. VALORES NULOS POR COLUMNA")  # Título de la sección
    print("=" * 50)  # Imprime otro separador
    nulos = df.isnull().sum()  # Cuenta los valores nulos en cada columna
    pct   = (nulos / len(df) * 100).round(2)  # Calcula el porcentaje de nulos por columna
    reporte = pd.DataFrame({"nulos": nulos, "porcentaje (%)": pct})  # Crea un DataFrame con el reporte
    print(reporte[reporte["nulos"] > 0].to_string())  # Muestra sólo las columnas que tienen nulos
    print(f"\nTotal celdas nulas: {nulos.sum()}\n")  # Muestra el total de celdas nulas


def eliminar_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    print("=" * 50)  # Imprime un separador visual
    print("2. REGISTROS DUPLICADOS")  # Título de la sección
    print("=" * 50)  # Imprime otro separador
    antes = len(df)  # Guarda la cantidad de filas antes de eliminar duplicados
    df = df.drop_duplicates()  # Elimina filas duplicadas
    eliminados = antes - len(df)  # Calcula cuántas filas se eliminaron
    print(f"Duplicados eliminados : {eliminados}")  # Imprime la cantidad de duplicados eliminados
    print(f"Registros restantes   : {len(df)}\n")  # Imprime el número de filas restantes
    return df  # Devuelve el DataFrame sin duplicados


def corregir_tipo(df: pd.DataFrame) -> pd.DataFrame:
    print("=" * 50)  # Imprime un separador visual
    print("3. CORRECCIÓN DE CAMPO 'tipo'")  # Título de la sección
    print("=" * 50)  # Imprime otro separador
    antes = df["tipo"].value_counts(dropna=False).to_dict()  # Cuenta la distribución original de valores de 'tipo'

    df["tipo"] = (
        df["tipo"]
        .fillna("desconocido")  # Rellena valores nulos con 'desconocido'
        .astype(str)  # Convierte el valor a cadena
        .str.strip()  # Elimina espacios en los extremos
        .str.lower()  # Convierte el texto a minúsculas
        .map(lambda v: TIPOS_VALIDOS.get(v, None))  # Mapea valores válidos a su forma canonical, invalidos a None
    )

    invalidos = df["tipo"].isnull().sum()  # Cuenta filas con tipo inválido o nulo tras la transformación
    print(f"Distribución original : {antes}")  # Muestra la distribución original de tipos
    print(f"Filas con tipo inválido/nulo -> se marcan NaN: {invalidos}")  # Informa cuántas filas quedaron inválidas
    df = df.dropna(subset=["tipo"])  # Elimina las filas que no tienen un tipo válido
    print(f"Registros tras eliminar tipos inválidos : {len(df)}\n")  # Imprime cuántas filas quedan luego de eliminar inválidos
    return df  # Devuelve el DataFrame con tipos corregidos


def limpiar_nombre_empresa(df: pd.DataFrame) -> pd.DataFrame:
    print("=" * 50)  # Imprime un separador visual
    print("4. NORMALIZACIÓN DE 'nombre_empresa'")  # Título de la sección
    print("=" * 50)  # Imprime otro separador
    con_espacios = df["nombre_empresa"].str.strip() != df["nombre_empresa"].fillna("")  # Detecta filas con espacios extra en el nombre de la empresa
    print(f"Registros con espacios extra : {con_espacios.sum()}")  # Muestra cuántos registros tenían espacios extra
    df["nombre_empresa"] = df["nombre_empresa"].str.strip().str.title()  # Normaliza el nombre eliminando espacios y aplicando Title Case
    print("Espacios eliminados y formato Title aplicado.\n")  # Mensaje de confirmación
    return df  # Devuelve el DataFrame con nombres normalizados


def validar_correo(df: pd.DataFrame) -> pd.DataFrame:
    print("=" * 50)  # Imprime un separador visual
    print("5. VALIDACIÓN DE FORMATO 'correo'")  # Título de la sección
    print("=" * 50)  # Imprime otro separador
    invalidos_mask = df["correo"].notna() & ~df["correo"].str.contains("@", na=False)  # Busca correos que no contienen '@'
    print(f"Correos sin '@' (inválidos) : {invalidos_mask.sum()}")  # Muestra cuántos correos son inválidos
    df.loc[invalidos_mask, "correo"] = None  # Reemplaza los correos inválidos por NaN
    nulos_total = df["correo"].isnull().sum()  # Cuenta cuántos correos quedan nulos tras esta validación
    print(f"Total correos nulos tras validación : {nulos_total}\n")  # Imprime el total de correos nulos
    return df  # Devuelve el DataFrame con correos validados


def rellenar_nulos_restantes(df: pd.DataFrame) -> pd.DataFrame:
    print("=" * 50)  # Imprime un separador visual
    print("6. RELLENO DE NULOS RESTANTES")  # Título de la sección
    print("=" * 50)  # Imprime otro separador
    rellenos = {
        "telefono": "Sin teléfono",  # Valor por defecto para la columna telefono
        "correo":   "Sin correo",  # Valor por defecto para la columna correo
        "direccion": "Sin dirección",  # Valor por defecto para la columna direccion
        "documento_nit": "Sin documento",  # Valor por defecto para documento_nit
    }
    for col, valor in rellenos.items():  # Recorre cada columna y su valor de reemplazo
        n = df[col].isnull().sum()  # Cuenta nulos en la columna actual
        if n > 0:
            df[col] = df[col].fillna(valor)  # Rellena los valores nulos con el texto definido
            print(f"  '{col}' -> {n} nulos reemplazados por '{valor}'")  # Muestra qué se reemplazó
    print()  # Imprime una línea en blanco de separación
    return df  # Devuelve el DataFrame con valores faltantes rellenados


if __name__ == "__main__":
    df = cargar_datos(CSV_ENTRADA)  # Carga datos desde el CSV de entrada o genera datos de prueba

    print("\n-- INICIO DE LIMPIEZA --\n")  # Mensaje que marca el inicio del proceso
    reportar_nulos(df)  # Reporta el estado de valores nulos

    df = eliminar_duplicados(df)  # Elimina filas duplicadas del DataFrame
    df = corregir_tipo(df)  # Corrige y valida la columna 'tipo'
    df = limpiar_nombre_empresa(df)  # Normaliza el nombre de la empresa
    df = validar_correo(df)  # Valida el formato del correo electrónico
    df = rellenar_nulos_restantes(df)  # Rellena los nulos restantes con valores por defecto

    df.to_csv(CSV_SALIDA, index=False, encoding="utf-8")  # Exporta el DataFrame limpio a un nuevo CSV
    print(f"[OK] Dataset limpio exportado -> '{CSV_SALIDA}'  ({len(df)} filas)")  # Mensaje final indicando éxito

