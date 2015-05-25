# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 07:09:02 2013

@author: daniel
"""

# programa: file_caracteres.py
# este programa cuenta los caracteres que hay en file txt

nombre = raw_input('Nombre File: ')
fichero = open(nombre, 'r')

# ambos <while> funcionan
contador = 0
while True: 
#while 1:
    caracter = fichero.read(1)
    if caracter == '':
        break
    contador += 1
fichero.close()
print contador