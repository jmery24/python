# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 06:02:45 2013

@author: daniel
"""

#programa: funciones_ejercicio_341.py
#funcion para modificar datos
#ejercicio 341

#definir funcion <modifica_parametros>
def modifica_parametros(x, y):
    x = 1    
    y.append(3)
    y = y + [4]
    y[0] = 10
    
#cuerpo del programa
#input
a = 0
b = [0, 1, 2]

#activa funcion
modifica_parametros(a, b)

#output
print 'a: ', a
print 'b: ', b #ver nota al pie
#operaciones como <append>, <del> o la asignacion a elementos indexados de
#listas modifican a la propia lista, entonces los cambios afectan al
#parametro y el argumento. Solo toma el cambio de <append> 
#y=y+[4] bloquea el ultimo cambio