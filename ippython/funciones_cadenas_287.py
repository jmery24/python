# -*- coding: utf-8 -*-
"""
Created on Tue May 21 06:50:35 2013

@author: daniel
"""

#programa: funciones_cadenas_287
#crear una funcion que devuelva la cadena mas larga
#ejercicio 287 NO FUNCIONA

#define funcion <mayor>
def mayor(cadena):
    cadena_mayor = []
    for i in range(1, len(cadena)):
#        print 'I', cadena[i]
        cadena_menor = []
        for j in range(0, len(cadena)-i):
#            print 'J', cadena[j]
            if len(cadena[j]) > len(cadena[j+1]):
                cadena_mayor = cadena[i]
#                print cadena_mayor
            elif len(cadena[j]) < len(cadena[j+1]):
                cadena_menor = cadena[j]
#                print cadena_menor
    if cadena_mayor > cadena_menor:
        return cadena_mayor
    else:
        return cadena_menor
#    return cadena_menor
    
lista = ['pepe', 'maria', 'juan', 'ana']


print 'el elemento mayor es: ', mayor(lista)            