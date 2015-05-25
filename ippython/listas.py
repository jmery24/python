# programa: listas.py
# ejercicios en el manejo de listas

def lista_s(lista):
	print '-----------'
	print 'Listado <s>'
	print 'Lista original <s>: ', lista
	print 'Indice (1): ', lista[1]
	print 'Indice (1:-1): ', lista[1:-1]
	lista[0] = lista[2]
	print 'Lista modificada: ', lista
	lista[2] = lista[1] / 2
	print 'Lista version final: ', lista

def lista_a(listado):
	print '-----------'
	print 'Listado <a>'
	print 'Lista original <a>: ', listado
	print 'Indice (2:4): ', listado[2:4]
	listado[2:4] = [3, 4, 5, 6]
	print 'Lista modificada: ', listado
	listado[2:-1] = []
	print 'Lista final: ', a
	
def lista_b(listita):
	print '-----------'
	print 'Listado <b>'
	print 'Lista * 3: ', listita * 3
	print 'Lista + Lista: ', listita + listita
	print 'Longitud de la lista: ', len(listita)
	
def lista_c(lista):
	print '-----------'
	print 'Listado <c>'
	print 'Lista original: ', lista
	d = [lista, lista + [3]]
	print 'Lista modificada: ', d
	d[1][2] = [1, 2, 3]
	print 'Lista modificada: ', d
	d[1][0] = [[],[2, 3]]
	print 'Lista version final: ', d
	  
def lista_e(lista):
	print '-----------'
	print 'Listado <e>'
	print 'Lista original: ', lista
	lista[1] = lista
	print 'Lista modificada: ',lista
	print 'Indice (1): ', lista[1]
	print 'Indice (0): ', lista[0]
	print 'Indice (1)(0): ', lista[1][0]

# input
s = [1, 1 + 1, 6 /2]
a = [1, 2, 3, 4, 5]
b = s[:-1] # b = [1, 2]


# activa funciones
lista_s(s)
lista_a(a)
lista_b(b)
lista_c(b)
lista_e(b)
