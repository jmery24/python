# programa: file_lineas.py
# otra manera de leer lineas de un fichero

# input
nombre = raw_input('Nombre del File: ')

# abre el file
f = open(nombre, 'r')
contador = 0
while 1:
	linea = f.readline()
	if linea == '':
		break
	contador += 1
	print contador, ')',
	print linea.rstrip()
f.close()
print

# otra alternativa
f = open(nombre, 'r')
contador = 0
while 1:
	for linea in f:
		contador += 1
		print contador, ')',
		print linea.rstrip()
f.close()
