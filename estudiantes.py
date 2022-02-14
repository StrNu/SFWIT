estudiantes = {}
quit = ""
id = 0

print("\nRegistro a los talleres SFWIT\n")
while quit != "q":
    quit = input("Oprime cualquier tecla para ingresar otro registro o 'q' para salir: ")
    if quit == "q":
        break
    id = id+1
    nombre = input("Ingresa nombre completo: ")
    edad = input("Ingresa tu edad: ")
    temas = input("Ingresa temas de intereś: ")
    estudiantes[id] = {}
    estudiantes[id]["nombre"]= nombre
    estudiantes[id]['edad'] = edad
    estudiantes[id]['temas'] = temas

    if (int(edad) < 18):
        menorEdad = "Es menor de edad"
    else:
        menorEdad = "No es menor de edad"

    estudiantes[id]['menorEdad'] = menorEdad

'''print(estudiantes[id].items())'''
    
for e in estudiantes:
    print(f'\nid {e}')

    for datos in estudiantes[e]:
        print('{}:{}'.format(datos, estudiantes[e][datos]))
        