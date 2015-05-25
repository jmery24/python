# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/daniel/.spyder2/.temp.py
"""

#programa: listas_pertenece.py
#verifica si un elemento pertenece o no a una lista

print 'Metodo: programa para comprobar si/no hay pertenencia' 
elemento = int(raw_input('escriba un numero: '))
lista = [1,4,5,1,7,8]
pertenece = False

for i in lista:
    if elemento == i:
        pertenece = True
        break
    
if pertenece:
    print 'El elemento pertenece a la lista'
else:
    print 'El elemento no pertenece a la lista'

#utilizando el operador python predefinido: <in>
print 'Operador python predefinido <in> si/no hay pertenencia'
elemento = int(raw_input('escriba un numero: '))
lista = [0,3,6,2,8,9]
if elemento not in lista:
    print 'El elemento no pertenece a la lista'
else:
    print 'El elemento pertenece a la lista'
print 'if not X in Y = if X not in Y'