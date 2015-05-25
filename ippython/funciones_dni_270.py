# -*- coding: utf-8 -*-
"""
Created on Fri May 10 07:33:42 2013

@author: daniel
"""

#programa: funciones_dni_270.py
#dado un numero del dni, calcular la ultima letra

#definimos funcion <letra>
def letra(dni):
    lista = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    return lista[dni%23]
    
#cuerpo del programa

#data input
numero = int(raw_input('Numero de DNI: '))

#data output
print 'La ultima letra es: ', letra(numero)