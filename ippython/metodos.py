# programa: metodos.py
# aplicar metodos sobre listas

# input
lista = [1, 4, 3, 5, 2]
print 'Lista original: ', lista

# insert(i, x) inserta el elemento x en la posicion i
lista.insert(2, 11)
print 'Insertar elemento: ', lista

# append(x) inserta el elemento x al final de la lista
lista.append(4)
print 'Insertar elemento: ', lista

# index(x) devuelve el indice el 1er elemento <x> en la lista
indice = lista.index(2)
print 'Indice [2]: ', indice

# remove(x) remueve el primer elemento <x> de la lista
lista.remove(3)
print 'lista con <3> removido: ', lista

# sort() ordena una lista de menor a mayor
lista.sort()
print 'Lista ordenada: ', lista

# reverse() invierte el orden de una lista
lista.reverse()
print 'Lista invertida: ', lista

# count(x) cuenta el numero de veces del elemento <x> en la lista
print 'Cantidad de veces elemento <4>: ', cuenta

# del lista[i] borra de la lista elemento que corresponde al indice <i>
del lista[3]
print 'Lista con elemento indice [3] borrado: ', lista

# del lista[i:j] borra los elementos del intervalo [i a -j]
del lista[2:4]
print 'Lista con elementos borrados [2:4]: ', lista 
