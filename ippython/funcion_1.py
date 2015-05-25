# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 07:32:38 2013

@author: daniel
"""

#funcion
def imprimir(texto, veces):#funcion imprimir
    print texto * veces#imprime un texto una cantidad de veces

#data input    
palabra = raw_input('Escribe una palabra: ')
cantidad = int(raw_input('Cuantas veces repetimos la palabra: '))
    

#processing
if cantidad < 1:
    print 'No imprime'
else:
    palabra = palabra + ' '#concatena espacio, separacion entre repeticiones
    imprimir(palabra, cantidad)#llama la funcion imprimir


