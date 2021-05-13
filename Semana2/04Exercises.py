'''
El siguiente es el menu de un restaurante de bocadillos. 
Diseñar un algoritmo capaz de leer el numero de unidades 
consumidas de cada alimento ordenado y calcular la cuenta total. 

Bocadillo de Jamon (4 euros)
Bocadillo de Queso (3 euros)
Patatas Fritas (2 euros)
Refresco (1 euro)
Cerveza (2 euros)
'''

bocadilloJamon = int(input("Cantidad de Bocadillos de Jamon a ordenar: "))
totalBcJamon = bocadilloJamon * 4

bocadilloQueso = int(input("Cantidad de Bocadillos de Queso a ordenar: "))
totalBcQueso = bocadilloQueso * 3

patatasFritas = int(input("Cantidad de Patatas Fritas a ordenar: "))
totalPttFritas = patatasFritas * 2

refresco = int(input("Cantidad de Refrescos a ordenar: "))
totalRefrescos = refresco * 1

cerveza = int(input("Cantidad de Cervezas a ordenar: "))
totalCerveza = cerveza * 2

totalOrden = totalBcJamon + totalBcQueso + totalPttFritas + totalRefrescos + totalCerveza

print("El total de su orden son ", totalOrden, "EUR")