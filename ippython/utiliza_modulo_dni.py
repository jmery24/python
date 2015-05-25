# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 07:58:36 2013

@author: daniel
"""

#programa: utiliza_modulo_dni.py
#este programa utiliza las funciones del modulo <dny>
#ejercicio 391 

#activa funciones del modulo
from dni import letra, comprueba_letra_dni

#data input
print 'El programa compara el numero DNI y un letra'
print
numero = int(raw_input('Numero de DNI: '))
una_letra = raw_input('Escribe una letra Mayuscula: ')
print

#activa la funcion
respuesta = comprueba_letra_dni(numero, una_letra)
if respuesta == True:
    print 'Bienvenido al Sistema de verificacion'
else:
    print 'Ha cometido usted un error'