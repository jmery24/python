# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 07:41:15 2013

@author: daniel
"""

#programa:contador.py
#dos contadores de 6, uno de ellos utiliza range

#contador simple
for i in [1,2,3,4,5,6]:
    print i
    
#contador con range
for i in range(1, 7):
    print i
    
#otra variante de range, siempre el menor valor es cero
for i in range(7):
    print i
    

# contador para numeros pares [0, 200]
for i in range(0,201,2):
    print i
    
# contador para numeros impares [1, 200]
for i in range(1,200,2):
    print i    
    