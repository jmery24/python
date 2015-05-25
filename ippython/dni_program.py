# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 06:45:44 2013

@author: daniel
"""

#programa:dni.py
#utiliza el operador indexacion para calcular que letra corresponde
#dado un numero

#data input
dni = int(raw_input('Numero: '))
cadena = 'TRWAGMYFPDXBNJZSQVHLCKE'

#processing and printout
num = dni % 23
print cadena[num]
