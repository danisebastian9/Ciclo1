Proceso Compra_tienda_ropa
	Escribir 'Ingrese cantidad de Pantalones para Hombre a ordenar'
	Leer cantidad123
	total123 <- cantidad123*45000
	Escribir 'Ingrese cantidad de Camisas Manga Corta a ordenar'
	Leer cantidad345
	total345 <- cantidad345*35000
	Escribir 'Ingrese cantidad de Camisetas Polo a ordenar'
	Leer cantidad456
	total456 <- cantidad456*27000
	Escribir 'Ingrese cantidad de Camisetas Cuello redondo a ordenar'
	Leer cantidad567
	total567 <- cantidad567*12000
	Escribir 'Ingrese cantidad de Medias tobilleras X par a ordenar'
	Leer cantidad678
	total678 <- cantidad678*3000
	totalOrden <- total123+total345+total456+total567+total678
	Escribir 'El total de su orden es $',totalOrden,' COP '
FinProceso
