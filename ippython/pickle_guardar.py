# -*- coding: utf-8 -*-
"""
Created on Sat May  4 03:46:07 2013

@author: daniel
"""

#programa: pickle_guardar.py

import pickle

#creamos una lista
numero_a = int(raw_input('Escriba el numero menor de la lista: '))
numero_b = int(raw_input('Escriba el numero mayor de la lista: '))

lista = range(numero_a, numero_b+1)
#y ahora la guardamos en un fichero llamado <picklefichero.mio>
pickle.dump(lista, open('picklefichero.mio', 'w'))
print 'archivo <picklefichero.mio> guardado'