# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:29:07 2013

@author: daniel
"""

#programa: funciones_raiz_cubica(262).py
#ejercicio 262

#definir la funcion para calcular la raiz cubica de un numero
def raiz_cubica(x):
    return x ** (1.0/3.0)
    
#data input
numero = float(raw_input('Entra un valor: '))
print

#invocar o activar la funcion
print 'La raiz cubica de %f es <%f>' %(numero, raiz_cubica(numero))