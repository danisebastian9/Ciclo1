'''
Realicen en Python un programa que lea 10 números por teclado, 
los almacene en un arreglo y muestre la suma, 
resta, multiplicación y división de todos.
'''

import numpy as np

def numList():
    longLista = 10 
    numList = np.zeros(longLista, dtype=int)

    for i in range(longLista):
        numList[i] = int(input('Ingrese el numero a guardar -> '))
    return numList    
lista = numList()

suma = lista.sum()
multiplicacion = lista.prod()


print(lista)
print(suma)
print(multiplicacion)



