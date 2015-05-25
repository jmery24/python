## programa: except.py
## definiciones
## ejemplos de excepciones

## definicion <except>
print '*-------------------------------------------------------------*'
print '| A veces queremos realizar una operacion que podria provovar |'
print '| un errror en tiempo de ejecucion, pero no queremos que se   |'
print '| pare el programa, esta situacion la podemos manejar con las |'
print '| sentencias <try> y <except>.                                |'
print '*-------------------------------------------------------------*'
print

## ejemplos

# funcion <existe>
def existe(nombre):
	try:
		f = open(nombre, 'r')
		texto = f.readlines()
		print texto
		f.close()
		return 1
	except:
		print 'El archivo no existe'
		return 0
		
## main

# input
archivo = raw_input('Nombre del File: ')

# activa funcion
f = open(archivo, 'r')
texto = f.readlines()
print texto
f.close()
#existe(archivo)
