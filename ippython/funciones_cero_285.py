# -*- coding: utf-8 -*-
"""
Created on Fri May 17 06:40:16 2013

@author: daniel
"""

#programa: funciones_cero_285.py
#la funcion devuelve un 'cero' si encuentra un 'cero' en la lista 
#ejercicio 285

#funcion: cero
def cero(lista):
    control = 1
    for elemento in lista:
        if elemento == 0:
            control -= 1            
    return control
        
#cuerpo del programa
#data input
num = int(raw_input('Cantidad de elementos en la lista: '))
print

#construye la lista desde el teclado
listado = []
for i in range(num):
    elemento = int(raw_input('Elemento: '))
    listado.append(elemento)

#activa la funcion
if cero(listado) < 1:
    print 'Si hay ceros en el listado'
else:
    print 'No hay ceros en el listado'
    