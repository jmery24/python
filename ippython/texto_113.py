# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 06:41:00 2013

@author: daniel
"""

#programa:texto_113
#introduzca un texto, no esta permitido letras mayusculas

#data input
texto = [" "]
texto = raw_input('introduzca un texto: ')

#condicion: no esta permitido letras mayusculas
while texto < 'a' or texto > 'z':
    print 'solo esta permitido utilizar letras minusculas'
    texto = raw_input('introduzca un texto: ')
    
print 'texto correcto', texto