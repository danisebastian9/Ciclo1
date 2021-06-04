#Las cuentas solo pueden ser de tipo Ahorros o Credito
#El saldo minimo de una cuenta es el 10% del valor inicial con que se crea la cuenta.
# Consignar: incrementa el dinero de la cuenta con base en el monto de dinero que se desea consignar.
# Retirar: retira el monto dado de la cuenta siempre y cuando la cuenta no quede con un saldo inferior
#   al saldo minimo, si esto ocurre solo se retirara el saldo autorizado. 
# mostrarSaldo(): obtiene el saldo actual de la cuenta
# mostrarSaldoMinimo(): obtiene el saldo minimo de la cuenta
# mostrarCapacidadCredito(): 
# Para cuentas de ahorro, la capacidad de crédito es igual a la diferencia 
#   entre al saldo actual y el saldo mínimo # 
# y para cuentas de crédito, la capacidad de crédito es 3 veces el saldo actual 


def crearCuenta(): 
    tipo = input('Digite tipo de cuenta Ahorros/Credito: ').lower()
    saldo = 0
    saldoMinimo = 0
    if tipo == 'ahorros' or tipo == 'credito': 
        vInicial = int(input('Digite Valor Inicial: '))
        saldo = vInicial
        saldoMinimo = vInicial * 0.1
    return tipo, saldo, saldoMinimo

def retirar(saldo, saldoMinimo, monto):
    disponible = saldo - saldoMinimo
    if disponible >= monto:
        saldo -= monto
        return saldo
    else: 
        print('El maximo monto a retirar es: ', disponible)
        saldo -= disponible
        return saldo

def consignar(saldo, monto):
    saldo += monto
    return saldo 


def consultarSaldo(saldo): 
    print(f'Su saldo actual es: ', saldo)

def capacidadCredito(tipo, saldo, saldoMinimo = 0):
    if tipo == 'ahorros':
        capacidad = saldo - saldoMinimo
    elif tipo == 'credito':
        capacidad = saldo * 3
    else:
        capacidad = 0
    return capacidad

# Main Program

tipo, saldo, saldoMin = crearCuenta()

menu = int(input('-- Consignar(1) -- Retirar(2) -- Consultar Saldo(3) -- Capacidad(4) -- '))

while menu in [1,2,3,4]:
    if menu == 1:
        monto = int(input('Digite monto a consignar: '))
        saldo = consignar(saldo, monto)
        consultarSaldo(saldo)
    elif menu == 2:
        monto = int(input('Digite monto a retirar: '))
        saldo = retirar(saldo, saldoMin, monto)
        consultarSaldo(saldo)
    elif menu == 3: 
        consultarSaldo(saldo)
    elif menu == 4:
        print(f'la capacidad de Credito es: {capacidadCredito(tipo, saldo, saldoMin)}')

    menu = int(input('-- Consignar(1) -- Retirar(2) -- Consultar Saldo(3) -- Capacidad(4) -- '))

