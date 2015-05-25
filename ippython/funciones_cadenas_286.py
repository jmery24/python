# -*- coding: utf-8 -*-
"""
Created on Fri May 17 07:41:58 2013

@author: daniel
"""

#programa: funciones_cadena_286.py
#funcion que a una cadena la concatene consigo misma 'n' de veces
#ejercicio 286

#funcion: concatenar
def concatenar(cadena):
    cadena = (cadena*repeticion)
    return cadena
    
#cuerpo del programa
#data input
palabras = raw_input('Escribir una cadena: ')
repeticion = int(raw_input('Cantidad de repeticiones: '))

#activar la funcion
print
print 'La cadena', palabras, 'concatenada', repeticion, 'veces: ', concatenar(palabras)
print 'La cadena <%s> concatenada %i veces: %s' %(palabras, repeticion, concatenar(palabras))