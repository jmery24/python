# programa: file_vocales_465.py
# cifra un texto: cambiar vocales por numeros
# a=6, e=3, i=1, o=0, u=5
# ejercicio 465

# abre, lee e imprime file original
nombre = raw_input('Nombre del File: ')
fichero = open(nombre, 'r')
print
print 'File original'
print '-------------'
for linea in fichero:
	if linea[-1] == '\n':
            linea = linea[:-1]
	print linea

# abre, lee, sustituye vocales en el file
fichero.close()
fichero = open(nombre, 'r')
texto = ''
while 1:
	caracter = fichero.read(1)
	if caracter == '':
		break
	elif caracter == 'a':
		texto += '6'
	elif caracter == 'e':
		texto += '3'
	elif caracter == 'i':
		texto += '1'
	elif caracter == 'o':
		texto += '0'
	elif caracter == 'u':
		texto += '5'
	else:
		texto += caracter
fichero.close()

# imprime file cifrado
print
print 'File vocales sustituidas'
print '------------------------'
print texto
