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


# Operaciones con dos arreglos - Tienen que ser del mismo tamaño

suma_Arr = array4 + array3
print(suma_Arr)

mult_Arr = array4 * array3
print(mult_Arr)

resultado = arrayfor + 10 
print(resultado)

resultadoMult = arrayfor * 10 
print(resultadoMult)

arrNum1 = np.array([8,9,4,1,2,3])
arrNum2 = np.array([5,4,6,7,5,9])
print(arrNum1 > arrNum2)
print(all(arrNum1>arrNum2)) # Si todos son mayores al otro  
print(any(arrNum1>arrNum2)) # Si alguno es mayot al otro
print(arrNum1.min()) # Busca el valor minimo y lo imprime
print(arrNum1.max()) # Busca el valor maximo y lo imprime
print(arrNum1.mean()) # Saca el promedio del array
print(arrNum1.sum()) # Suma todos los elementos del array
print(arrNum2.prod()) # Busca el producto 
print(arrNum2.argmin()) # En que posicion esta el minimo
print(arrNum2.argmax()) # En que posicion esta el maximo
print(np.sort(arrNum2)) # ordena los numeros o cadenas

cadena = ['a','z','d','i','k','l']
print(np.sort(cadena))
