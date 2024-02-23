# -*- coding: utf-8 -*-

'''
El ejercicio consiste en meter dentro de una lista fragmentos de texto, usando como separador las lÃ­neas VACÃAS
'''

carpeta_nombre="F:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="acuerdo.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	lineas_lista=archivo.readlines()

parrafo=""
parrafos_lista=[]
for linea in lineas_lista:
	if linea.strip() == "":
		if parrafo != "":
			parrafos_lista.append(parrafo)
		parrafo=""
	else:
		parrafo+=linea
if parrafo!="":
	parrafos_lista.append(parrafo)

# EN ESTE PUNTO, LA SOLUCIÃ“N ESTÃ EN parrafos_lista