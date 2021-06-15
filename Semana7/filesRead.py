from io import open # No es necesario importarlo. 

# Lectura de archivos 'r' - 

archivo1 = open('archivos/archivo1.txt', 'r')

contenido = archivo1.read()
print(contenido)

archivo1.seek(0)  # ubicarse en esa posicion
print(archivo1.readline())  # Leer linea por linea en la posicion actual.
print(archivo1.readline())  # Leer linea por linea en la posicion actual.

archivo1.seek(0)
lista = archivo1.readlines()
print(lista)

archivo1.close()

for i in lista:
    print(i)


# Lectura y escritura 'r+'


