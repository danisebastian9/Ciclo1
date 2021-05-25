# Realizar un programa que imprima los numeros pares desde
# x hasta y

x = int(input('Ingrese rango inferior: '))
y = int(input('Ingrese rango superior: '))

for i in range(x, y):
    if i % 2 == 0: 
        print(i)
         