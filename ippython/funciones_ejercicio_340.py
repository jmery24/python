# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 05:41:26 2013

@author: daniel
"""

#programa: funciones_ejercicio_340.py
#crea funcion para modificacion
#ejercicio 340

#definir la funcion <modifica_parametros>
def modifica_parametros(x, y):
    x = 1
    y[0] = 1
    
#cuerpo del programa
#input
a = 0
b  = [0, 1, 2]

#activa funcion
modifica_parametros(a, b)

#output
print 'a: ', a
print 'b: ', b #ver nota al pie
#operaciones como <append>, <del> o la asignacion a elementos indexados de
#listas modifican a la propia lista, entonces los cambios afectan al
#parametro y el argumento   