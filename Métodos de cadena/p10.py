# Función para convertir la fecha en un determinado formato
# Separar la entrada en componentes (mes, día, año) --> -/-/-
# Ingresar fecha y finalmente se imprime el resultado
# Profe, esta pregunta 

def convertir_fecha(fecha):

    m = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    if '/' in fecha:
        partes = fecha.split('/')
        mes, dia, anio = partes[0], partes[1], partes[2]
    else:
        partes = fecha.split(' ')
        mes, dia, anio = partes[0], partes[1][:-1], partes[2]

    numero_mes = str(m.index(mes) + 1).zfill(2)

    fecha_formateada = f"{anio}-{numero_mes}-{dia.zfill(2)}"

    return fecha_formateada

fecha_ingresada = input("Ingrese una fecha (en formato mes-día-año o 'Mes día, año'): ")

fecha_formateada = convertir_fecha(fecha_ingresada)
print("Fecha en formato AAAA-MM-DD:", fecha_formateada)
