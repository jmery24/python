# -*- coding: utf-8 -*-
"""
Created on Fri May 24 06:06:52 2013
@author: daniel
"""

#programa: funciones_lectura_teclado.py
#esta funcion lee un numero entero del teclado
#este tipo de funcion se llaman funciones sin parametros

#define funcion <lee_entero>
def lee_entero():
    return int(raw_input('Ingresa un numero entero: '))
    
#cuerpo del programa
#activa la funcion
a = lee_entero()
print
print 'El numero entero ingresado es: ', a