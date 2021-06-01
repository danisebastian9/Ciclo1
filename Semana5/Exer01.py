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

while nota != 0:
    if nota > 0 and nota <= 5:
        