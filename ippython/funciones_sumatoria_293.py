# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:29:04 2013

@author: daniel
"""

#programa: funciones_sumatoria_293
#define una funcion para una sumatoria dados (a,b)
#ejercicio 293

#define funcion <sumatoria>
def sumatoria(a,b):
    if a > b:
        return None
    else:
        sum = 0
        for i in range(a, b+1):
            sum = sum + i
    return sum
    
#cuerpo del programa
#data input
valor_a = int(raw_input('Valor inicial: '))
valor_b = int(raw_input('Valor final: '))

#activa la funcion
print
print 'la sumatoria es : ', sumatoria(valor_a, valor_b)