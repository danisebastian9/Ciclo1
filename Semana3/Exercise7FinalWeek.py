'''
Una Universidad colombiana asesorada por la Universidad El Bosque y siguiendo su mismo
espíritu de ayuda a las clases menos favorecidas, ha diseñado un esquema de porcentajes de
ayuda (descuento sobre la matrícula) para sus nuevos estudiantes que funciona de la siguiente
manera:
    • Cada estudiante candidato deberá dar su nombre y apellidos, su edad en años, el puntaje
obtenido en el examen y el número decimal de salarios mínimos mensuales que tiene de
ingreso familiar.
    • Presentar un examen de aptitud académica y razonamiento, calificado en números
enteros de 0 a 100.
    • Cálculo del porcentaje de apoyo según los siguientes criterios:
    • Si la edad está en el rango 15 a 18 años dar 25%, de 19 a 21 años dar 15% y de 22 a
25 años dar 10%, para mayores de 25 no dar ningún apoyo por edad.
    • Si el ingreso familiar es inferior o igual a un salario mínimo dar 30%, si es mayor a un
salario mínimo e inferior o igual a 2 salarios mínimos dar 20%, si es mayor a dos
salarios mínimos e inferior o igual a 3 salarios mínimos dar 10%, si es mayor a tres
Reto 2 [2] Semana 3
salarios mínimos e inferior o igual a 4 salarios mínimos dar 5%, para ingresos superiores no dar ningún apoyo por ingreso familiar.
    • Si puntaje de ingreso es mayor o igual a 80 y menor de 86 dar 30%, si es mayor o igual a 86 y menor de 91 dar 35%, si es mayor o igual a 91 y menor de 96 dar 40%, si es mayor o igual a 96 dar 45%. Para puntajes menores de ochenta no hay apoyo por puntaje de examen.
    • Los apoyos recibidos por edad, por ingreso familiar y por puntaje de examen se deben sumar para dar el porcentaje total de apoyo que recibirá el beneficiario, es decir, el porcentaje de descuento sobre el valor de la matrícula.

El dueño de la Universidad le ha solicitado a usted como programador, que le desarrolle un programa en lenguaje Python que le permita:
    • Leer desde el teclado el nombre y apellido del candidato, su edad entera en años, el puntaje obtenido en el examen y el número decimal de salarios mínimos mensuales de su ingreso familiar.
    • Calcular el valor total de descuento del candidato según los criterios antes definidos.
    • Mostrar en consola el nombre y apellido del beneficiario, el descuento recibido por edad, el recibido por el ingreso familiar, el recibido por el puntaje del examen y el descuento total que recibirá sobre el valor de la matrícula.   
'''

beneficiario = str(input("Ingrese su nombre y apellido: "))
edad = int(input('Ingrese su edad: '))
ingreso = float(input('Ingrese la cantidad de salarios minimos mensuales de su ingreso familiar: '))


if edad >= 15 and edad <= 18: 
    descuento = 25
elif edad >= 19 and edad <= 21:
    descuento = 15
elif edad >= 22 and edad <= 25:
    descuento = 10
else: 
    descuento = 0








