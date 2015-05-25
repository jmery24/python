# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/daniel/.spyder2/.temp.py
"""

#programa: funciones_letras_271.py
#programa evalua una cadena; True = minuscula and False = mayuscula
#desarrollar una funcion para evualar la condicion

#funcion <letras>
def letras(letra):
    if 'a' <= letra <= 'z':
        return True
    elif 'A' <= letra <= 'Z':
        return False
    else:
        return None
        
#cuerpo del programa

#data input
cadena = raw_input('Escriba una cadena: ')

#data output
print 'Es la primer letra minuscula? ', letras(cadena)   