def suma_lista ():
    lista = []
    pares = []

    while True:
        numero = input("ingrese el numero que desea agregar(o salir para terminar): ")
        if numero.lower() == "salir":
            break
        try:
            entidad = int(numero)
            lista.append(entidad)
        except ValueError:
            print("ERROR. valor invalido")

    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        suma = sum(pares)
    print("la suma de los numero pares es:", suma)




suma_lista()




