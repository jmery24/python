# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:11:56 2013

@author: daniel
"""

#programa: listas_226.py
#una lista debe modificarse para que cada elemento 
#negativo sea remplazado por 0
a = [1,-22,-3,4]
print 'el valor original de la lista <a> es: ', a
for i in range(0, len(a)):          #otra opcion es: for i in [0,1,2,3]:
    if a[i] < 0:
        a[i] = 0
    else:
        b = (a[i])
        a[i] = b   
print 'sustituimos por 0 cualquier elemento negativo de la lista <a>'
print 'ahora, el valor de la lista <a> es: ', a