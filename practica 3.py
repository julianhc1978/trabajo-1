def lista_inversa():
    lista = []
    while True:
        elemento = input("ingrese un elemento (o sailr para terminar): ")
        if elemento.lower() == "salir":
            break
        lista.append(elemento)
    print("la lista es:", lista)
    lista.reverse()
    print("la lista invertida es:",lista)

lista_inversa()