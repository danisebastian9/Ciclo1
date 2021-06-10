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
lista3 = [int(i) for i in lista3]
print(lista3)

lista3.extend(lista2) # lista3.extend(range(20,30)) 
print(lista3)

print(lista3.count(2)) #Cuenta cuantas veces esta ese valor en la lista

lista3.pop() # elimina el ultimo elemento. 
lista3.pop(0) # busca el elemento en esa posicion y la elimina


vocales = ['a','e','i','o','u']
x = '-'
cadenaVocales = x.join(vocales)
print(cadenaVocales)
