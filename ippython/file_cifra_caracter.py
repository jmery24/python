# programa: file_cifra_caracter.py
# programa abre y lee un fichero
# esa informacion le aplica un criterio de cifrado
# escribe la informacion en otro archivo

# input
nombre_entrada = raw_input('File de Entrada: ')
nombre_salida = raw_input('File de Salida: ')

# abre files de <entrada> y <salida>
f_entrada = open(nombre_entrada, 'r')
f_salida = open(nombre_salida, 'w') 

# programa de <cifrado>
while 1:
	caracter = f_entrada.read(1)
	if caracter == '':
		break
	elif caracter >= 'a' and caracter <= 'y':
		f_salida.write(chr(ord(caracter) + 1))
	elif caracter == 'z':
		f_salida.write('a')
	else:
		f_salida.write(caracter)
f_entrada.close()
f_salida.close()		
