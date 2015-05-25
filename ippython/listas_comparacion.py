# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 08:00:42 2013

@author: daniel
"""

#programa: listas_comparacion
#ejercicio 219

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

if a < b:
    print 'a es menor que b'
else:
    print 'a no es menor que b'
    
#otro camino para comparar
flag = 0
for i in [0, 1, 2, 3]:
    print i
    if a[i] < b[i]:
        flag = 1
if flag == 1:
    print 'a es menor que b'
else:
    print 'a no es menor que b'
    
    
    

