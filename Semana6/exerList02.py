'''
Realizar una función que, dada una lista, devuelva una nueva lista cuyo 
contenido sea igual a la original pero invertida. 
Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], 
deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].
'''

def inv_lista(lista):
    listaInversa = []
    longitud = len(lista)-1
    for i in range(longitud, -1, -1):
        listaInversa.append(lista[i])
    return listaInversa

lista = ['Pedro','Juan', 'Pepe', 'Luisa']
print(inv_lista(lista))
print(lista)
lista.reverse()
print(lista)
