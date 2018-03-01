#coding: utf-8
numero=input("introduce cuantas palabras tendra la lista")
if numero < 1:
	print "es imposible"
else:
	lista=[]
	for i in range(numero):
		x=raw_input("introduce una palabra:")
		lista.append(x)
    	for i in lista:
        	lista.reverse()
print("La lista inversa es:",lista)

