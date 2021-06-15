from io import open
import os

# Crear - w. crea el archivo o lo abre en modo escritura, si tiene informacion la borra
archivo1 = open('archivos/archivo1.txt', 'w')

# Crear - x - Crea el archivo si no existe, si existe da error y no borra la informacion existente
# archivo1 = open('archivos/archivo1.txt', 'x')


frase = 'Hola Mundo!...'
nombre = input('Digite su nombre -> \n')
# nombre = input('Digite su nombre -> ') + frase
# archivo1.write(nombre)            Imprimiria nombre + frase en una variable.

archivo1.write('La vida es bella\n')
archivo1.write(frase + os.linesep)
archivo1.write(nombre)


for i in range(1,11):
    archivo1.write(f'Escribiendo linea {i}\n')

archivo1.close

print(nombre)
print(frase)




