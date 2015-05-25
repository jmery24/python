# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 06:00:30 2013

@author: daniel
"""

#programa: funciones_bits.py
#definir una funcion para calcular la cantidad de digitos para 
#representar un numero digital en forma binaria

#definir la funcion <bits>
def bits(n):
    if n == 0 or n == 1:
        resultado = 1
    else:
        resultado = 1 + bits(n / 2)
    return resultado
    
#cuerpo del programa
#input
numero = int(raw_input('Escribe un numero entero: '))

#activa funcion y output
print
print 'Se necesitan %i digitos para escribir el numero %i en forma binaria' %(bits(numero), numero)