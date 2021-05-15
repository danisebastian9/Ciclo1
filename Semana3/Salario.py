horasTrabajadas = float(input('Digite las horas trabajadas por semana '))
if horasTrabajadas > 0 and horasTrabajadas <= 80:
    if horasTrabajadas > 40 :
        horasExtras = horasTrabajadas - 40
        print('Sus horas extras son: ', horasExtras)
        valorExtras = horasExtras * 2000
        print("El valor de las horas extras son: ", valorExtras)
        valorNormal = 40 * 1600
        print('El salario basico es: ', valorNormal)
        salario = valorExtras + valorNormal
    else:
        salario = horasTrabajadas * 1600
    print("Su salario semanal es: ", valorNormal)
else:
    print("Dato invalido, ingrese un numero mayor que 0 o menor que 80 ")
