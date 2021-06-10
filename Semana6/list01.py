lista1 = [3,'Juan',8.5,7,8,'Maria',8,False]
print(lista1)
print(lista1[5])
print(lista1[2:5])
print(lista1[5:])

lista1.append('Pedro')
print(lista1)
lista1.append(input('Ingrese valor: '))
print(lista1)
lista1.insert(3,False)
print(lista1)
lista1.remove('Juan')
del lista1[3]
print(lista1)



lista2 = []
tam = int(input('Digite el tamaño de la lista -> '))

for i in range(tam):
    lista2.append(int(input('Digite un numero -> ')))
print(lista2)

numeros = input('Digite los numeros separados por espacio -> ')
lista3 = numeros.split()
print(lista3)


vocales = ['a','e','i','o','u']
x = '-'
cadenaVocales = x.join(vocales)
print(cadenaVocales)
