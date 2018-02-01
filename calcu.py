#!/usr/bin/python3
import sys

len_args = len(sys.argv)
if len_args != 4:
	sys.exit("Se ha producido un error, introduce 3 parámetros")

#ASIGNAMOS NOMBRES A LOS ARGUMENTOS PARA TRABAJAR MAS COMODOS
operacion = sys.argv[1] 
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])



try:

	if 'suma' in operacion:

		print("La suma de",num1,"+",num2,"es",num1+num2)
	else:

		if 'resta' in operacion:
			print("La resta de",num1,"-",num2,"es",num1-num2)

	if 'multiplicacion' in operacion:
		print("La multiplicación de",num1,"x",num2,"es",num1*num2)

	else:
		try:
			if 'division' in operacion:
				print("La división de",num1,"/",num2,"es",num1/num2)
		except ZeroDivisionError:
				print("No se puede dividir entre 0")

except NameError:
	print("Error")


            
