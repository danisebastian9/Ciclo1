''' 
 Imprimir y contar los múltiplos de 3 
 desde la primera unidad hasta un número que 
 introducimos por teclado.
'''
import numpy as np

arraySize = int(input('Digite el tamaño del arreglo -> '))

'''
num = np.arange(1,arraySize)
print(num)
'''

num2 = np.zeros(arraySize,dtype=int)
for i in range(1,arraySize + 1):
    num2[i-1] = i
print(num2)

cont = 0
for i in range(arraySize):
    if num2[i] % 3 == 0:
        print(num2[i])
        cont += 1
print(f'Cantidad de multiplos de (3): {cont}')
