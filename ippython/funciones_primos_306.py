# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:15:17 2013

@author: daniel
"""

#programa: funciones_primos_306.py
#definir la funcion <es_primo> : dtermina si un numero es primo
#definir un procedimiento <muestra_primos> entre 1 y el numero ingresado
#ejercicio 306

#definir la funcion <es_primo>
def es_primo(num):
    marca = 0
    for i in range(1, num+1):
        if num % i == 0:
            marca += 1
    if marca > 2:
        return 'No Primo'
    else:
        return i

#definir procedimiento <muestra_primos>
def muestra_primos(nro):
    lista = []
    for i in range(1, nro+1):
        if es_primo(i) != 'No Primo':
            lista.append(es_primo(i))
    print 'Listado de numeros primos: ', lista        
        
#cuerpo del programa

#data input
numero = int(raw_input('Ingresa un numero entero: '))
print

#activa funcion
muestra_primos(numero)