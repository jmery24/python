# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 07:14:20 2013

@author: daniel
"""

#programa: funciones_fibonacci.py
#definir una funcion que calcula la serie de Fibonacci para un numero <n>

#definir la funcion <fibonacci> (recursiva)
def fibonacci(n):
    if n == 1 or n == 2:
        resultado = 1
    elif n > 2:
        resultado = fibonacci(n-1) + fibonacci(n-2)
    return resultado
    
#definir funcion <fivonacci> (iterativa)
def fivonacci(n):
    if n == 1 or n == 2:
        f = 1
    else:
        f1 = 1
        f2 = 1
        for i in range(3, n+1):
            f = f1 + f2
            f1 = f2
            f2 = f
    return f    

#cuerpo del programa
#input
numero = int(raw_input('Escribe un numero: '))
print

#activa la funcion y output
print 'Serie de Fibonacci (recursiva)'
print 'Considerando el numero %i, la serie de fibonacci es %i' %(numero, fibonacci(numero))
print
print 'Serie de Fivonacci (iterativa)'
print 'Considerando el numero %i, la serie de fivonacci es %i' %(numero, fivonacci(numero))