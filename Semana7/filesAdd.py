# añadir al archivo 'a'
# Añade al final del archivo

archivo1 = open('archivos/archivo1.txt', 'a' )

nombre = input('Digite Nombre -> ')
edad = input('Digite su edad -> ')

archivo1.write(nombre + '\n')
archivo1.write(edad + '\n')