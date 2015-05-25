# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:08:49 2013

@author: daniel
"""

#programa: minmax.py
#dos funciones que calculan el minimo y maximo
#se incorporan como modulo

#modulo minmax

#definir funciones

#definir funcion <minimo>
def minimo(a, b):
    if a < b:
        return a
    else:
        return b
        
#definir funcion <maximo>
def maximo(a, b):
    if a > b:
        return a
    else:
        return b

#esta rutina solo comprueba el funcionamiento de las funciones
#cuando se importa las funciones del modulo no se ejecuta        
if __name__ == '__main__':
    print 'El maximo entre 3 y 10 es: ', maximo(3, 10)
    print 'El maximo entre 3 y -10 es: ', maximo(3, -10)
    print 'El minimo entre 3 y 10 es: ', minimo(3, 10)
    print 'El minimo entre 3 y -10 es: ', minimo(3, -10)