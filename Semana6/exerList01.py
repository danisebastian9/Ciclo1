'''
Pide un numero por teclado y guarda en una lista su tabla de 
multiplicar hasta el 10. 
Por ejemplo, si pide el 5 la lista tendra: 
5,10,15,20,25,30,35,40,45,50
'''

num = int(input('Digite un numero -> '))
tabla = []

for i in range(1,11):
    mult = num * i
    tabla.append(mult)
print(tabla)

