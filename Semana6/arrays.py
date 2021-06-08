import numpy as np

arr = np.array([8,'9',4,1,2,3])
print(arr[:3])
print(arr)
arr_nuevo = arr.astype(int)
print(arr_nuevo)

array1 = np.zeros(10,dtype=int)
print(array1)

array2 = np.ones(10,dtype=int)
print(array2)

array3 = np.arange(1,11)
print(array3)

array4 = np.arange(1,21,2)
print(array4)


n = int(input('Digite tamaño del arreglo: -> '))
arrayfor = np.zeros(n, dtype=int)
for i in range(n):
    arrayfor[i] = input('Digite un numero -> ')
print(arrayfor)
