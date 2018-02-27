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

    inversa = []
    for i in lista:
        inversa = [i] + inversa
    print("La lista inversa es:", inversa)coding: utf-8
npalabra= int(input("cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(npalabra):
        print("Dígame la palabra", str(i + 1) + ":")
        palabra=input()
        lista+=[palabra]
    print("La lista creada es:", lista)

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

        for i in eliminar:
            for o in range(len(lista)-1, -1, -1):
                if lista[o] == i:
                    del(lista[o])
        print("La lista es:", lista)
