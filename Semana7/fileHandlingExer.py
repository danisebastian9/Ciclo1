from io import open

# Crear
def crearArchivo():
    archivo = open('Archivos/prueba_31.txt','w')
    archivo.close()

def insertar():
    archivo = open('Archivos/prueba_31.txt', 'a')
    estudiante = input('Digite Nombre del estudiante -> ').title()
    notaFinal = input('Digite nota final -> ')
    archivo.write(estudiante + '\n')
    archivo.write(notaFinal + '\n')
    archivo.close()

def leer():
    archivo = open('Archivos/prueba_31.txt','r')
    datos = archivo.readlines()
    archivo.close()
    cont = 0
    for i in datos:
        datos[cont] = i.replace('\n', '')
        cont += 1
    return datos

#Programa principal

# crearArchivo()

# insertar()
# insertar()

lista = leer()
print(lista)
for i in lista:
    print(i)

# Buscar
name = input('Digite el nombre del estudiante -> ').title()

if name in lista:
    posicion = lista.index(name)
    print(lista[posicion])
    print(lista[posicion + 1])


# Filtrar

letra = input('Digite letra a filtrar -> ').upper()
for i in lista():
    if i[0] == letra:
        posicion = lista.index(i)
        print(lista[posicion])
        print(lista[posicion + 1])
    

# eliminar

name = input('Digite el nombre del estudiante a eliminar -> ').title()

if name in lista:
    posicion = lista.index(name)
    lista.pop(posicion)
    lista.pop(posicion)
    archivo = open('Archivos/prueba_31.txt','w')
    for i in lista:
        archivo.write(i + '\n')
    archivo.close()
    print(lista)



