# programa: file_cifrado.py
# cifra un texto: a cada caracter le correspondera el siguiente
# sola que a la <z> le corresponde <a>

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

# abre, lee, cifra file
fichero.close()
fichero = open(nombre, 'r')
texto = ''
while 1:
	caracter = fichero.read(1)
	if caracter == '':
		break
	elif caracter >= 'a' and caracter <= 'y':
		texto += chr(ord(caracter) + 1)
	elif caracter == 'z':
		texto += 'a'
	else:
		texto += caracter
fichero.close()

# imprime file cifrado
print
print 'File cifrado'
print '------------'
print texto
