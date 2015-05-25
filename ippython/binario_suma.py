# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 08:28:49 2013

@author: daniel
"""

#programa:binario_suma.py
#programa: solicita dos numeros binarios y calcula su suma 
#ejercicio 196 NO FUNCIONA
#data input
binario_1 = int(raw_input('Primer numero binario: '))
binario_2 = int(raw_input('Segundo numero binario: '))

#processing
binario_A = '0b' + binario_1
binario_B = '0b' + binario_2

print binario_A
print binario_B
bin_1 = int(binario_A)
bin_2 = int(binario_b)
suma = bin_1 + bin_2
print bin(suma)

