# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 08:42:00 2013

@author: daniel
"""

#programa:alfabetica.py
#programa que verifica si una palabra esta ordenada alfabeticamente
#ejercicio 190
#data input
cadena = raw_input('Introduce una cadena: ')

flag = 0#inicializa flag

for i in range(0, len(cadena)-1):#no quiero llegar al ultimo caracter
    if cadena[i] < cadena[i-len(cadena)+1]:#check ordenamiento alfabetico
        flag == flag#para mantener la identacion
    else:#no hay orden alfabetico
        flag = 1#flag igual a 1
if flag == 0:
    print 'cadena alfabetica'
else:
    print 'cadena no ordenada alfabeticamente'
        