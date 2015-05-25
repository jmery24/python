# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:45:05 2013

@author: daniel
"""

#programa: subcadena_7.py
#cual es el prefijo comun y mas largo a dos cadenas
#operador de corte
#ejercicio 209. no trabaja ok
#data input
cadena_a = raw_input('Escribe cadena A: ')
cadena_b = raw_input('Escribe cadena B: ')
flag = 0
subcadena_a = ''
subcadena_b = ''
prefijo = ''


for k in range(0, len(cadena_a)):
    subcadena_a = subcadena_a + cadena_a[k]
    print 'A', subcadena_a
    for i in range(0, len(cadena_a)):
        print len(cadena_b)
        print 'valor i', i
        if i <= len(cadena_b):
            subcadena_b = subcadena_b + cadena_b[i]
            print 'B', subcadena_b
            if cadena_a[i] == subcadena_b[i]:
                flag = flag + 1
                print 'flag', flag
        else:
            print 'paso'
                             
print flag
if flag > 0:
    for l in range(0, len(cadena_b)):
        prefijo = cadena_a[l]
        prefijo = prefijo + cadena_a[0:l]
        print prefijo
else:
    print 'cadena_b no es prefijo de cadena_a'
    
if flag > 0:
    print 'el prefijo comun mas largo es: '#, cadena_a(0, flag)
    
       
