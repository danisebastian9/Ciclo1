#Leer una matriz de 5x5 y calcular la suma de cada una de sus filas y columnas, dejando dichos 
#resultados en dos vectores, uno de la suma de las filas y otro de la suma de las columnas

import numpy as np

matriz = np.zeros((5,5), dtype=int)

sumFilas = np.zeros(5, dtype=int)
sumColumn = np.zeros(5, dtype=int)

for i in range(5):
    for j in range(5):
        matriz[i][j] = input('Digite un numero -> ')
print(matriz)

for i in range(5):
    sumFilas[i] = matriz[i].sum()
print(f'Suma de Filas : {sumFilas}')

matriz_colum = matriz.transpose()
for i in range(5):
    sumColumn[i] = matriz_colum[i].sum()

print(f'Suma de columnas : {sumColumn}')


