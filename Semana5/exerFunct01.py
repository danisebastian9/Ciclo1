# 1.Crear una funcion que sirva para la vida cotidiana
# 2.Buscar 2 funciones internas y mostrarlas en clase

quanLlantas = int.upper(input('Ingrese cantidad de llantas a ordenar: '))

def funcLlantas(quanLlantas):
    if  quanLlantas > 1 and quanLlantas < 5: 
        totalVenta = quanLlantas * 300
    elif quanLlantas >= 5 and quanLlantas <= 10:
        totalVenta = quanLlantas * 250
    else: 
        totalVenta = quanLlantas * 200
    print(totalVenta)
