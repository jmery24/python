# programa: tuplas.py
# las tuplas son secuencias inmutables de objetos
# las tuplas se crean mediante una lista de elementos separados por
# coma y encerrados entre parentesis

tupla = (1, 2, 3)
print 'Tupla: ', tupla
print 'Tupla [0]: ', tupla[0]
print 'Tupla [1:3]: ', tupla[1:3]
cuenta = tupla.count(3)
print 'Cantidad de <2>: ', tupla.count(2)
print 'Cantidad de <3>: ', cuenta
indice = tupla.index(3)
print 'Indice [2]: ', tupla.index(2)
print 'Indice [1]: ', indice
