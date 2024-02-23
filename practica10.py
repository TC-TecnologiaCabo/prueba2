# -*- coding: utf-8 -*-

'''
El ejercicio consiste en segmentar un texto en oraciones. Se entiende por oraciÃ³n todo lo que hay entre una mayÃºscula y un punto.
Para garantizar esta segmentaciÃ³n se recorre una lista con todas las mayÃºsculas.
'''

import re

carpeta_nombre="D:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="documento2.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()

mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ã‘","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for letra in mayusculas:
	expresion_regular=re.compile(letra+r"*.*?\.")
	resultado_busqueda=expresion_regular.finditer(texto)
	for resultado in resultado_busqueda:
		print(resultado.group(0))