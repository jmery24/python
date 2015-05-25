# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 06:38:45 2013

@author: daniel
"""

#programa: funciones_concatena_350.py
#definir una funcion, input:lista, output: lista
#propiedad: que la lista original se concatene consigo misma
#pero la lista original no debe variar
#ejercicio 350

#definir funcion <concatena>
def concatena(lista):
    nueva_lista = lista + lista
    return nueva_lista

#cuerpo del programa
#input
listado = ['A', 'B', 'C']
listado_1 = [1, 2, 3, 4]

#activa funcion
print 'listado original: ', listado
print
print 'listado concatenado: ', concatena(listado)
print
print 'listado original: ', listado
print
print 'listado original: ', listado_1
print
print 'listado concatenado: ', concatena(listado_1)
print
print 'listado original: ', listado_1    