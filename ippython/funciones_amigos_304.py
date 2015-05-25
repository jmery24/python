# -*- coding: utf-8 -*-
"""
Created on Sun May 26 07:57:48 2013

@author: daniel
"""

#programa: funciones_amigos_304.py
#dado un <numero> calcula los numeros amigos entre 1 y <numero>
#crear una funcion y un procedimiento
#ejercicio 304
#crear funcion y procedimiento
#definir funcion <divisores>
def divisores(num):
    sumatorio = 0
    for i in range(1, num):
        if num % i == 0:
            sumatorio += i
    return num, sumatorio

#definir procedimiento <tabla_amigos>  es una funcion sin <return>
def tabla_amigos(nro):
    for i in range(1, nro+1):
        resultado = divisores(i)
        nuevo = divisores(resultado[1])
        if resultado[0] == nuevo[1]:
            if resultado[0] != nuevo[0]:
                print resultado[0], 'y', nuevo[0], 'son numeros amigos'
            else:
                print #resultado[0], 'y', nuevo[0], 'son numeros perfectos'
            
#cuerpo del programa
#data input
numero = int(raw_input('Escribe un numero: '))

#activa funcion
tabla_amigos(numero)   