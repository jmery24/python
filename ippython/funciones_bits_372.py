# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 06:20:50 2013

@author: daniel
"""

#programa: funciones_bits_372.py
#definir una funcion para calcular la cantidad de digitos para 
#representar un numero <base 10> en forma binaria
#ejercicio 372

#definir la funcion <bits>
def bits(n):
    if n == 0 or n == 1:
        resultado = 1
    else:
        resultado = 1 + bits(n / 2)
    return resultado
    
#cuerpo del programa
#input
numero = int(raw_input('Escribe un numero entero como exponente: '))
num = 10 ** numero
print 'El numero final es: ', num

#activa funcion y output
print
print 'Se necesitan %i digitos para escribir el numero %i en forma binaria' %(bits(num), num)