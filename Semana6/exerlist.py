'''
Dada una lista de numeros enteros y un entero k, escribir una funcion que: 
Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k
Devuelva una lista con aquellos que son multiplos de k
'''

def crearListas(k, numeros):
    menores = []
    mayores = []
    iguales = []
    multiplos = []
    for i in numeros:
        if i < k:
            menores.append(i)
        elif i > k:
            mayores.append(i)
        else:
            iguales.append(i)

        if i % k == 0:
            multiplos.append(i)
    return menores, mayores, iguales, multiplos

numeros = [4,9,8,7,2,0,1,7,9,54,5,42,9,3,1,7,5,12,45,9,98,99,66,30,31,35,71,63]
k = int(input('Ingrese un numero -> '))

print(crearListas(k, numeros))

menores, mayores, iguales, multiplos = crearListas(k, numeros)

print(f'Lista de Menores de {k}: {menores}')
print(f'Lista de Mayores de {k}: {mayores}')
print(f'Lista de Iguales de {k}: {iguales}')
print(f'Lista de Multiplos de {k}: {multiplos}')
