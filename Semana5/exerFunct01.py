# 1.Crear una funcion que sirva para la vida cotidiana
# 2.Buscar 2 funciones internas y mostrarlas en clase

cantidadUnidad = int(input('Ingrese cantidad de llantas a ordenar: '))

def funcLlantas(quanLlantas):
    if  quanLlantas > 1 and quanLlantas < 5:
        precioUnidad = 300 
        totalVenta = quanLlantas * precioUnidad
    elif quanLlantas >= 5 and quanLlantas <= 10:
        precioUnidad = 250 
        totalVenta = quanLlantas * precioUnidad
    else: 
        precioUnidad = 200 
        totalVenta = quanLlantas * precioUnidad
    print(f'Por ordenar {quanLlantas} llantas, su precio unitario es ${precioUnidad} y el total es ${totalVenta}' )

funcLlantas(cantidadUnidad)
