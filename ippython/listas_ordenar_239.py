# -*- coding: utf-8 -*-
"""
Created on Fri May  3 06:54:55 2013

@author: daniel
"""

#programa: listas_ordenar_239.py
#este programa ordena una lista de nombres
#metodo de la burbuja

lista = ['Pepe', 'Juan', 'Maria', 'Ana', 'Luis', 'Pedro']
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