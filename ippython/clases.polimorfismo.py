## programa: clases_polimorfismo.py
## definicion
## ejemplo: multisuma

## definicion
print '*--------------------------------------------------------------*'
print '| Es una funcion que operar sobre mas de un tipo. Si todas las |'
print '| operaciones realizadas dentro de una funcion se pueden       |'
print '| aplicar a un tipo, la funcion se puede aplicar a ese tipo    |'
print '*--------------------------------------------------------------*'
print

## ejemplo funcion <multisuma>

# funcion <multisuma>
def multisuma(x, y, z):
	return x * y + z
	
## main

# invoca funcion
multi = multisuma(3, 2, 1)
print 'multisuma (3, 2, 1): ', multi
