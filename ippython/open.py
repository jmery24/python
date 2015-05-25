# programa: open.py
# manejo de files (escritura - lectura)
# open(nombre, 'r') abre un file solo para lectura
# open(nombre, 'w') abre un file para lectura-escritura
# nombre.close() cierra el file
# utilizaremos el file: prueba.txt

# input
#nombre = raw_input('Nombre del file: ')
nombre = 'prueba.txt'

# abre file, lee todo el file y lo cierra
f = open(nombre, 'r')
print 'File: '
print '------' 
print f.read(),
f.close()

# abre file, lee la primera linea y lo cierra
f = open(nombre, 'r')
print
print 'Primera Linea: ' 
print '---------------'
print f.readline()
f.close()

# abre file, lee las lineas y lo cierra
f = open(nombre, 'r')
print
print 'Lineas: ' 
print '--------'
print f.readlines()
f.close()

# abre file, escribe, cierra file
f = open(nombre, 'w')
s = 'Tigre\nOso\nAuca\nMafalda\nChiquito\nPerica\nPepita' 
f.write(s)
f.close()
# abre file, lee todo el file y lo cierra
f = open(nombre, 'r')
print 'File: '
print '------' 
print f.read(),
f.close()
