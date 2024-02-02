def convertir_fecha(fecha):
    """
    Función que convierte una fecha al formato AAAA-MM-DD.

    Parameters:
    - fecha (str): Fecha en formato mes-día-año o "Mes día, año".

    Returns:
    - str: Fecha en formato AAAA-MM-DD.
    """
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    # Separar la entrada en componentes (mes, día, año)
    if '/' in fecha:
        partes = fecha.split('/')
        mes, dia, anio = partes[0], partes[1], partes[2]
    else:
        partes = fecha.split(' ')
        mes, dia, anio = partes[0], partes[1][:-1], partes[2]

    # Obtener el número correspondiente al mes
    numero_mes = str(meses.index(mes) + 1).zfill(2)

    # Generar la fecha en formato AAAA-MM-DD
    fecha_formateada = f"{anio}-{numero_mes}-{dia.zfill(2)}"

    return fecha_formateada

# Solicitar al usuario que ingrese una fecha
fecha_ingresada = input("Ingrese una fecha (en formato mes-día-año o 'Mes día, año'): ")

# Llama a la función e imprime el resultado
fecha_formateada = convertir_fecha(fecha_ingresada)
print("Fecha en formato AAAA-MM-DD:", fecha_formateada)