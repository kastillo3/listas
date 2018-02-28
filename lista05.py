#coding: utf-8
npalabra= int(input("cuántas palabras tiene la lista: "))

if npalabra < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(npalabra):
        print("Dime la palabra", str(i + 1) + ": ")
        palabra = input()
        lista += [palabra]
    print("La lista es:", lista)


    npalabra2= int(input("cuántas palabras de la lista quieres eliminar: "))

    if npalabra2 < 1:
        print("¡Imposible!")
    else:
        eliminar = []
        for i in range(npalabra2):
            print("Dígame la palabra", str(i + 1) + ": ")
            palabra = input()
            eliminar += [palabra]
        print("La lista de palabras a eliminar es:", eliminar)

        for x in eliminar: 
            while y in eliminar
            lista.remove(x)

