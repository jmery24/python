# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:27:53 2013

@author: daniel
"""

#programa: listas_224.py
#una lista debe modificarse para que cada elemento sea el cuadrado del original
a = [1,2,3,4]
print 'el valor original de la lista <a> es: ', a
for i in range(0, len(a)):          #otra opcion es: for i in [0,1,2,3]:
    b = (a[i] ** 2)
    a[i] = b   
print 'calculamos el cuadrado de cada elemento de la lista <a>'
print 'ahora, el valor de la lista <a> es: ', a