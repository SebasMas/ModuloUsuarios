#Primero, crear el CRUD


import re
Usuarios = []


while True:

    print("1 - Ingresar un usuario")
    print("2 - Cargar usuarios")
    print()
    Option = int(input("Ingrese una opción: "))

    if Option == 1:
        nombre = input("Ingrese un nombre de Usuario: ")
        if len(nombre)>6 and len(nombre)<12 and bool(re.search(r'\d', nombre)):
            Usuarios.append(nombre)
            
        else:
            print("¡El nombre de usuario debe contener entre 6 a 12 carácteres y al menos un número!")

    elif Option == 2:
        print(Usuarios)
    

