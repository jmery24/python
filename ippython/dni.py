# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 07:49:13 2013

@author: daniel
"""

#programa: dni.py
#definimos un modulo con dos funciones <letra> y <comprueba_letra_dni>
#modulo dni
#ejercicio 391

#definimos funciones

#definir funcion <letra>
def letra(dni):
    lista = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    return lista[dni%23]
    
#definimos la funcion <comprueba_letra_dni>
def comprueba_letra_dni(num, LETRA):
    if LETRA == letra(num):
        return True
    else:
        return False
        
#rutina de comprobacion, no funciona cuando se importa el modulo
if __name__ == '__main__':
    print 'se corresponde J y 749: ', comprueba_letra_dni(749, 'J')
    print 'se corresponde M y 749: ', comprueba_letra_dni(749, 'M')
    print 'se corresponde L y 750: ', comprueba_letra_dni(750, 'L')