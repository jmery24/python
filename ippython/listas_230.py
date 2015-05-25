# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 06:53:48 2013

@author: daniel
"""
#programa: listas_230.py
# introduce desde el teclado numeros pero no acepta numeros negativos
#si se introduce un numero negativo da la opcion de introduccion
#nuevamente en reemplazo de ese numero negativo
#no funciona del todo correcto


lista = []
k = 0
numero = int(raw_input('cantidad de elementos de la lista: '))
while k < numero:
    elemento = int(raw_input('dame un elemento: '))
    print k
    if elemento >= 0:
        lista.append(elemento)
#        k += 1
    else:
        print 'no se aceptan numeros negativos'
        print 'entre un numero entero positivo'
        k -= 1
#        elemento = int(raw_input('dame un elemento: '))
#        if elemento >= 0:
#            lista.append(elemento)
print lista