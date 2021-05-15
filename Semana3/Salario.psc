Proceso SalarioSemana
	Definir  salario,H_trabajadas Como Real
	Leer  H_trabajadas
	Si H_trabajadas > 0  y H_trabajadas <80 Entonces
		Si H_trabajadas > 40 y H_trabajadas > 0 Entonces
			H_extras = H_trabajadas - 40
			Escribir "Sus horas extras son: ", H_extras
			V_extras = H_extras * 2000
			Escribir "El valor de las horas extras es: ", V_extras
			V_normal = 40 * 1600
			Escribir "El salario basico es: ", V_normal
			salario = H_extras + V_normal
		SiNo
			salario = H_trabajadas * 1600		
		FinSi
		
		Escribir "Su Salario semanal es: ", salario
	SiNo
		Escribir "Dato invalido, ingrese un numero mayor que 0 y menor que 81"
	FinSi	
FinProceso
