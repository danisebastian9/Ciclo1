# Lectura y escritura 'r+'

from io import open 

archivo1 = open('archivos/archivo1.txt', 'r+')

contenido = archivo1.read()
print(contenido)

archivo1.seek(0)  # ubicarse en esa posicion
print(archivo1.readline())  # Leer linea por linea en la posicion actual.
print(archivo1.readline())  # Leer linea por linea en la posicion actual.

archivo1.seek(0)
lista = archivo1.readlines() # convertir en una lista
print(lista)

numeros = [4,8,9,4,2,6,8]
for i in numeros:
    archivo1.write(str(i) + '\n')

archivo1.close()

for i in lista:
    print(i)



