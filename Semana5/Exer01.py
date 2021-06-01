# Ingresar notas de estudiantes hasta que ingrese nota 0.0
# Decir cual es la nota Minima  
# Decir cual es la nota Maxima
# Cuantas son menores a 3, osea las que reprobaron
# Cuantas son mayores o iguales a 3, osea las que aprobaron
# Sacar promedio de notas que reprobaron
# Sacar promedio de notas que aprobaron
# Notas son de 0 a 5
# Porcentaje de los que aprobaron 
# Porcentaje de los que reprobaron. 

nota = float(input('Ingrese la nota: '))
max = nota
min = nota
contaMin = 0 
contaMax = 0 
sumaMax = 0 
sumaMin = 0

while nota != 0:
    if nota > 0 and nota <= 5:
        if nota > max:
            max = nota 
        elif nota < min: 
            min = nota
        
        if nota < 3:
            contaMin += 1
            sumaMin += nota
        else:
            contaMax += 1
            sumaMax += nota
    
    nota = float(input('Ingrese la nota: '))

total = contaMin + contaMax
promedioMin = sumaMin / contaMin 
promedioMax = sumaMax / contaMax
porcMin = contaMin * 100 / total
porcMax = contaMax * 100 / total

print('Nota minima: ', min)
print('Nota maxima: ', max)
print('Cantidad de reprobados: ', contaMin)
print('Cantidad de aprobados: ', contaMax)
print('Promedio de notas minimas: ', promedioMin)
print('Promedio de notas maximas: ', promedioMax)
print('Porcentaje de reprobados: ', porcMin)
print('Porcentaje de aprobados: ', porcMax)