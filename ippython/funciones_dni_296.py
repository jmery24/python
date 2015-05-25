# -*- coding: utf-8 -*-
"""
Created on Thu May 23 07:15:10 2013

@author: daniel
"""

#programa: funciones_dni_296.py
#dado un numero del dni y la letra verificar si se corresponden <True>
#ejercicio 296

#definimos funcion <letra>
def letra(dni):
    lista = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    return lista[dni%23]
    
#definimos la funcion <comprueba_letra_dni>
def comprueba_letra_dni(num, LETRA):
    if LETRA == letra(num):
        return True
    else:
        return False
    
#cuerpo del programa
#data input
numero = int(raw_input('Numero de DNI: '))
una_letra = raw_input('Escribe una letra Mayuscula: ')

#activa la funcion
print
print 'La letra y el Numero se corresponden: ', comprueba_letra_dni(numero, una_letra)