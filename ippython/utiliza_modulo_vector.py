# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 09:06:16 2013

@author: daniel
"""

#programa: utiliza_modulo_vectores.py
#este programa importa funciones del modulo <vector>
#invoca el modulo
from vectores import *

#cuerpo del programa
#data input
vector_1 = v_lee_vector()
vector_2 = v_lee_vector()
print
print 'Muestra vector_1: ', v_muestra_vector(vector_1)
print
print 'Muestra vector_2: ', v_muestra_vector(vector_2)
print 'Longitud del vector_1: ', v_longitud(vector_1)
print 'Longitud del vector_2: ', v_longitud(vector_2)
print 'Suma de vectores: ', v_suma(vector_1, vector_2)
print 'Producto escalar: ', v_producto_escalar(vector_1, vector_2)
print 'Producto vectorial: ', v_producto_vectorial(vector_1, vector_2)
print 'Son perpendiculares ?', v_son_perpendiculares(vector_1, vector_2)