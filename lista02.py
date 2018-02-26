#coding: utf-8
numero=input("introduce cuantas palabras tendra la lista;")
if numero < 1:
	print "es imposible"
else:
	lista=[]
	for i in range(lista):
		print("Di la palabra:")
		a=input()
		lista+=[a]
		print("la lista que es",lista)
	
	encontrar=raw_input("Que palabra quieres buscar?:")
	cont=lista.count(encontrar)
	if cont==0:
		print("la palabra",str(encontrar),"que quieres buscar sale 1 vez en la lista")
	if cont==1:
		print("la palabra",str(encontrar),"que quieres buscar sale mas de 1 vez en la lista")
	else:
		print("la palabra no aparece en la lista")

	



