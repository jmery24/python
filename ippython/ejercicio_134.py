# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:59:41 2013

@author: daniel
"""

#programa:ejercicio_134.py
#introducir numeros e imprimirlos hasta que se introduzac un numero negativo
#processing
num = int(raw_input('introduce un numero, si es negativo fin del programa: '))
while num > 0:
    print num
    num = int(raw_input('>: '))
    if num < 0:
        print 'Adios'
        break
    
        