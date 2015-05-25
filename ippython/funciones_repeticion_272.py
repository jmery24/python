# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:19:49 2013

@author: daniel
"""

#programa: funciones_repeticion_272
#crear una funcion para evaluar si es una concatenacion 
#de la cadena consigo misma

#funcion <repeticion>
def repeticion(cadena):
    if cadena[0:len(cadena)/2] == cadena[len(cadena)/2:len(cadena)]:
        return True
    return False
    
#data input
letras = raw_input('introduce una cadena de caracteres: ')

#cuerpo del programa
print 'Repite una cadena: ', repeticion(letras)