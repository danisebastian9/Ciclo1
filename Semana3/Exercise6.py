'''
Una institución educativa estableció un programa para estimular a
los aprendices con buen rendimiento académico y que consiste en
lo siguiente:
    *Si el promedio es de 9.5 o más y el aprendiz es de secundaria, entonces
este podrá cursar 55 unidades y se le hará un 25% de descuento.
    *Si el promedio es mayor o igual a 9 pero menor que 9.5 y el aprendiz es de
secundaria, entonces este podrá cursar 50 unidades y se le hará un 10% de
descuento.
    *Si el promedio es mayor que 7 y menor que 9 y el aprendiz es de
secundaria, este podrá cursar 50 unidades y no tendrá ningún descuento.
    *Si el promedio es de 7 o menor, el número de materias reprobadas es de 0
a 3 y el aprendiz es de secundaria, entonces podrá cursar 45 unidades y no
tendrá descuento.
    *Si el promedio es de 7 o menor, el número de materias reprobadas es de 4
o más y el aprendiz es de secundaria, entonces podrá cursar 40 unidades y
no tendrá ningún descuento.
    *Si el promedio es mayor o igual a 9.5 y el aprendiz es de profesional,
entonces podrá cursar 55 unidades y se le hará un 20% de descuento. Sí el
promedio es menor de 9.5 y el aprendiz es de profesional, entonces podrá
cursar 55 unidades y no tendrá descuento.

Obtener el total que tendrá que pagar un aprendiz si la matrícula para
aprendices de profesional es de $300 por cada cinco unidades y para
aprendices de secundaria es de $180 por cada cinco unidades.
'''

promedio = float(input('Ingrese su promedio: '))
nivel = str.upper((input('''
Responda A o B respectivamente dependindo de su nivel educativo: 
A - Secundaria
B - Profesional
''')))

precioProfX5U = 300
precioSecX5U = 180

if nivel == 'A' and promedio >= 9.50 and promedio <= 10.00:
    unidadesCursar = 55
    totalMatricula = unidadesCursar / 5 * precioSecX5U
    descuento = totalMatricula * 25 / 100
    totalConDesc = totalMatricula - descuento

elif nivel == 'A' and promedio >= 9.00 and promedio < 9.50:
    unidadesCursar = 50
    totalMatricula = unidadesCursar / 5 * precioSecX5U
    descuento = totalMatricula * 10 / 100
    totalConDesc = totalMatricula - descuento

elif nivel == 'A' and promedio > 7.00 and promedio < 9.00:
    unidadesCursar = 50
    totalMatricula = unidadesCursar / 5 * precioSecX5U
    descuento = 0
    totalConDesc = totalMatricula

elif nivel == 'A' and promedio <= 7.00 and promedio >= 0 :
    materiasReprobadas = int(input('Ingrese cantidad de materias reprobadas: '))
    if materiasReprobadas >= 0 and materiasReprobadas <= 3:
        unidadesCursar = 45
        totalMatricula = unidadesCursar / 5 * precioSecX5U
        descuento = 0
        totalConDesc = totalMatricula
    elif materiasReprobadas >= 4:
        unidadesCursar = 40
        totalMatricula = unidadesCursar / 5 * precioSecX5U
        descuento = 0
        totalConDesc = totalMatricula
    
elif nivel == 'B' and promedio >= 9.5 and promedio <= 10.00:
    unidadesCursar = 55
    totalMatricula = unidadesCursar / 5 * precioSecX5U
    descuento = totalMatricula * 20 / 100
    totalConDesc = totalMatricula - descuento

elif nivel == 'B' and promedio < 9.5 and promedio >= 0:
    unidadesCursar = 55
    totalMatricula = unidadesCursar / 5 * precioSecX5U
    descuento = 0
    totalConDesc = totalMatricula

elif nivel != 'B' or nivel != 'A' or promedio < 0 and promedio > 10.00: 
    print("Nivel educativo o promedio no valido, responda A o B respectivamente y con promedio entre 0 y 10.00")
    unidadesCursar = 'NA'
    totalMatricula = 'NA'
    descuento = 0
    totalConDesc = totalMatricula


print('Las unidades a cursar son', unidadesCursar, '. El total de Matricula sin descuento es: $', totalMatricula, '. Su descuento es de: $', descuento, '. Y el precio final con descuento es: $', totalConDesc)
    



