# Buscar -

archivo1 = open('archivos/archivo1.txt', 'r')
datos = archivo1.readlines()
archivo1.close()

print(datos)
cont = 0

for i in datos:
    datos[cont] = i.replace('\n', '')
    cont += 1
print(datos)

buscar = input('Digite dato a buscar -> ')
if buscar in datos:
    print('Encontro')
    posicion = datos.index(buscar)
    print(datos[posicion])
    print(datos[posicion + 1])
    print(datos[posicion + 2])
else:
    print('No encontro')

