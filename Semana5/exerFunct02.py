#Citas Medicas - función donde me diga el tipo cita 
#TipoCita: General(1-3) - Especialista (4 o 5) - Usuario ingresa tipocita en numero 
#Valor Final de la cita - ValorGeneral= 50% descuento sobre la tarifa #ValorEspecialista= 50% aumento sobre la tarifa 
#El usuario ingresa la tarifa

def tipoCita(): 
    tipo = int(input('Digite el codigo para tipo de cita (1 - 5): '))
    if tipo >= 1 and tipo <= 3:
        return 'General'
    elif tipo >= 4 and tipo <= 5:
        return 'Especialista'
    else:
        return 'Tipo de cita invalido'
    
def valorCita(tipo, tarifa):
    if tipo == 'General':
        vFinal = tarifa * 0.5
    elif tipo == 'Especialista':
        vFinal = tarifa * 1.5
    else: 
        vFinal = 0
    return vFinal

tipo = tipoCita()
print(f'Su tipo de cita es {tipo}')
tarifa = int(input('Digite la tarifa de su cita: '))
total = valorCita(tipo,tarifa)
print(f'El valor a pagar es: {total}')