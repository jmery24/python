# programa: file_cifra_linea.py
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
for linea in f_entrada:
	nueva_linea = ''
	for caracter in linea:
		if caracter >= 'a' and caracter <= 'y':
			nueva_linea += chr(ord(caracter) + 1)
		elif caracter == 'z':
			nueva_linea += 'a'
		else:
			nueva_linea += caracter
	f_salida.write(nueva_linea)

f_entrada.close()
f_salida.close()
