# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:38:18 2013

@author: daniel
"""

#programa: funciones_hanoi.py
#definir una funcion para mover las torres de Hanoi

#definir la funcion <hanoi>
def hanoi(n, inicial, final, libre):
    if n == 1:
        print 'Mover disco superior de aguja ', inicial, 'a', final
    else:
        hanoi(n-1, inicial, libre, final)
        print 'Mover disco superior de aguja ', inicial, 'a' , final
        hanoi(n-1, libre, final, inicial)
        
#cuerpo principal del programa
#input y activa funcion
hanoi(3, 1, 3, 2)        