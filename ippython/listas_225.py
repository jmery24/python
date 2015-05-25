# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:07:42 2013

@author: daniel
"""

#programa: listas_225.py
#una lista debe modificarse para que cada elemento sea el cuadrado del original
n = int(raw_input('numero para rango de la lista: '))
a = range(1,n)
print 'el valor original de la lista <a> es: ', a
for i in range(0, len(a)):          #otra opcion es: for i in [0,1,2,3]:
    b = (a[i] ** 2)
    a[i] = b   
print 'calculamos el cuadrado de cada elemento de la lista <a>'
print 'ahora, el valor de la lista <a> es: ', a