# -*- coding: utf-8 -*-
"""
Created on Thu May  2 07:52:27 2013

@author: daniel
"""

#programa: listas_ordenar.py
#este programa ordena una lista
#metodo de la burbuja

lista = [2,26,4,3,1]
print 'Lista original',lista
for i in range(1, len(lista)):#bucle que hace <len(lista)-1> pasadas    
    print 'Pasada ', i
    for j in range(0, len(lista)-1):
        print '  Comparacion de los elementos en posicion %d y %d' % (j,j+1)        
        if lista[j] > lista[j+1]:
            elemento = lista[j]
            lista[j] = lista[j+1]
            lista[j+1]= elemento
            print '  Se intercambian'
        print '  Estado actual de la lista', lista
print 'Lista ordenada: ', lista        