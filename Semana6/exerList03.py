'''
Pedir numeros y agregarlos a una lista, cuando el usuario meta un 0
ya dejaremos de insertar. 
Por ultimo, muestre los numeros ordenados de menor a mayor.
'''

numeros = []

num = int(input('Ingrese un numero -> '))

while num != 0:
    numeros.append(num)
    num = int(input('Ingrese un numero -> '))
print(numeros)
numeros.sort()
print(numeros)

# max = 0
# cont = 1
# longitud = len(numeros)
# for i in numeros:
#     while cont < longitud:
#         if i > numeros[cont]:
#             max = i
#             numeros[cont - 1] = numeros[cont]
#             numeros[cont] = max
#         cont += 1
# print(numeros)

data_list = numeros
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print(new_list)
