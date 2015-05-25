# -*- coding: utf-8 -*-
"""
Created on Sat May  4 03:52:42 2013

@author: daniel
"""

#programa: pickle_cargar.py

import pickle

#creamos <listado> cargandola del fichero llamado <mifichero.mio>
listado = pickle.load(open('picklefichero.mio'))
#lo mostramos en la pantalla
print 'listado es: ', listado