##Ingresar aquí todo el código respectivo
''' 
El departamento de Talento Humano de la Universidad El Bosque, 
    a raíz de la participación en un proyecto muy especial, requiere poder
    procesar la nómina de docentes contratados por horas.
    Para tal efecto ha establecido los siguientes lineamientos: 

 - La nómina será procesada semanalmente, digitando por cada docente 
    las horas trabajadas en la semana y el valor establecido por hora.
 - A todos los docentes que trabajen más de 40 horas en la semana, 
    se les reconocerán como horas extras y se pagarán a un valor de 1,5 
    de la hora normal.
 - El salario bruto será calculado como la suma del valor de las horas 
    normales más el valor de las horas extras (si las hay).
 - Al salario bruto obtenido en el punto anterior se le calculará el 9% 
    para los parafiscales.
 - Para cada docente se le calcularán provisiones para prima de servicio 8.33%, 
    cesantías 8.33%, intereses de cesantía 1.0% y vacaciones 4.17%, 
    sobre el salario bruto.
 - A cada uno se le descontará el aporte de 4% para salud y el 4% para pensión, 
    también sobre el salario bruto.

El director de Talento Humano le ha solicitado a usted como programador, 
    que le desarrolle un programa en lenguaje Python que le permita:

 - Leer desde el teclado los datos de nombre, horas trabajadas y valor hora, 
    por cada docente del proyecto. 
 - Mostrar en consola el valor de las horas normales.
 - Mostrar en consola el valor de las horas extras (si las hay).
 - Mostrar en consola el valor del salario bruto: 
    valor horas normales + valor horas extras. 
 - Mostrar en consola los descuentos por parafiscales, salud y pensión y el total.
 - Mostrar en consola el sueldo neto a pagar.
 - Mostrar en consola las provisiones hechas para prima, cesantías, 
    intereses de cesantía y vacaciones.
 - Los cálculos de sueldo bruto, descuentos, sueldo neto y provisiones, 
    deberán ser realizados a través de funciones o procedimientos y serán 
    llamados en el programa principal.

Entrada:

Los parámetros de entrada serán los siguientes
 - Horas trabajadas.
 - Valor hora.

Salida:

Los parámetros de salida deben ser:

 - Valor horas normales: ht * vh
 - Valor horas extras: (ht – 40) * 1.5*vh
 - Sueldo bruto: valor horas normales + valor horas extras.
 - Descuento parafiscales: sb * 0.09
 - Descuento salud: sb * 0.04
 - Descuento pensión: sb * 0.04
 - Suma de todos los descuentos
 - Sueldo neto: sb – (descuento parafiscales + descuento salud + descuento pensión)
 - Provisiones para prima 8.33%
 - Provisiones para cesantías 8.33%
 - Provisiones para intereses de cesantía 1.0%
 - Provisiones para vacaciones 4.17%.

'''

horasTrabajadas = int(input('Ingrese horas trabajadas: '))
valorHora = int(input('Ingrese valor de hora laboral: '))





