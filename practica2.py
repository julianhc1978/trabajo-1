def lista_elementos():
    lista =set()
    repetidos = []
    while True:
        try:
            elemento = input("ingrese el elemento (o salir para terminar): ")
            if elemento.lower() == "salir":
                break
            if elemento in lista:
                repetidos.append(elemento)
            else:
                lista.add(elemento)
        except ValueError:
            print("ERROR. valor invalido")
    print("la lista de los elementos es:",lista)
    print("la lista con los elementos repepetidos es:",repetidos)

lista_elementos()



