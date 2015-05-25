# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 07:02:22 2013

@author: daniel
"""

#programa:contador_v2
#numeros positivos en un intervalo [0, num] con un incremento

#data input
incremento = 0
num = int(raw_input('Numero final de la serie: '))
while incremento == 0:
    print 'el incremento no debe ser igual a 0'
    incremento = int(raw_input('Incremento de: '))
    

#proccesing and printout
for i in range(0,num,incremento):
    print i
