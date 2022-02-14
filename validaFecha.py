def validaFecha(Fecha):
    dia, mes, anio = Fecha.split('/')
    lenAnio = len(anio)

    print (dia,mes,anio,lenAnio)

    if (0 < int(dia) <=31) and (0 < int(mes) <= 12) and (999 < int(anio) and int(lenAnio) == 4):
        return "Fecha correcta"
    else: 
        return "Fecha incorrecta"
 
Fecha = input("Escribe una fecha con formato 01/01/2022: ")
print(validaFecha(Fecha))

