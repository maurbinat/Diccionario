contacto = {"nombre" : input("Ingrese el nombre del contacto:\n")
    ,"Telefono" : int(input("Ingrese el numero de telefono del nuevo contacto : \n"))
    ,"email" : input("Ingrese el email del contacto a agregar:\n")
    ,"edad" : int(input("Ingrese la edad de su contacto:\n"))}

print(" ------- Ficha de contacto -------- ")
print("nombre : " , contacto["nombre"])
print("Telefono : " , contacto["Telefono"])
print("email : " , contacto["email"])
print("edad : " , contacto["edad"])
while True:
    editar = input("¿Quiere editar algun dato? s/n :\n ")
    if editar == "s":
        print("¿Qué dato desea editar?:\n")
        print("1.- Nombre")
        print("2.- Telefono")
        print("3.- email")
        print("4.- edad")
        opc = int(input("Elija que opcion quien quiere cambiar:\n"))
        if opc == 1:
            contacto["nombre"] = input("Ingrese el nuevo nombre:\n")
        elif opc == 2:
            contacto["Telefono"] = int(input("Ingrese el nuevo número de telefono:\n"))
        elif opc == 3:
            contacto["email"] = input("Ingrese el nuevo email de su contacto:\n")
        elif opc == 4:
            contacto["edad"] = int(input("Ingrese la nueva edad de su contacto:\n"))

        print(" ------- Ficha de contacto -------- ")
        print("nombre : " , contacto["nombre"])
        print("Telefono : " , contacto["Telefono"])
        print("email : " , contacto["email"])
        print("edad : " , contacto["edad"])
    else:
        print("Saliendo del programa.......")
        break
    #no es necesario poner una opcion de salida ya que la misma parte de editar lo sugiere 
