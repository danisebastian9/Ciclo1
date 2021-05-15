'''
Hacer un algoritmo que imprima el nombre de un artículo, 
clave, precio original y su precio con descuento. 
El descuento lo hace en base a la clave, si la clave es D1 
el descuento es del 10% y si la clave es 
D2 el descuento en del 20% (solo existen dos claves)
'''

articuloNombre = input("Ingrese nombre del articulo: ")
articuloClave = input("Ingrese codigo de articulo: ")
articuloPrecio = float(input("Ingrese precio del articulo: "))
articuloDescuento = str(input("Increse codigo de descuento: "))

if articuloDescuento.upper() == 'D1':
    descuento = articuloPrecio * 10 / 100 
    precioFinal = articuloPrecio - descuento 
elif articuloDescuento.upper() == 'D2':
    descuento = articuloPrecio * 20 / 100
    precioFinal = articuloPrecio - descuento
else:
    print('Codigo de descuento no valido ')

print("Su articulo ", articuloNombre, "con codigo ", articuloClave, "precio original ", articuloPrecio, "tiene un precio final de ", precioFinal)



