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
    print("La lista inversa es:", inversa)
