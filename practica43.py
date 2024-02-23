import re
carpeta_nombre="F:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="documento2.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read() 
expresion_regular=re.compile(r"Procesamiento")
'''resultado_busqueda=expresion_regular.search(texto)
print(resultado_busqueda.group(0))
'''
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))

expresion_regular=re.compile(r"ˆ.")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))
'''
resultados_busqueda=expresion_regular.finditer(texto)
for resultado2 in resultados_busqueda:
    print(resultado2.group(0))
    '''
expresion_regular=re.compile(r".*")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado3 in resultados_busqueda:
    print(resultado3.group(0))

expresion_regular=re.compile(r"Ni+")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado4 in resultados_busqueda:
    print(resultado4.group(0))

