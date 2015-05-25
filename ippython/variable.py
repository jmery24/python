# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:13:48 2013

@author: daniel
"""

#programa:variables.py
#lee una cadena y verifica si el nombre sirve como nombre de variable
#bucle <while> permite salir del programa con un espacio en blanco
#ejercicio 176 - funciona: in progress

#data input
cadena = raw_input('Escribe una cadena: ')

#processing:
for i in range(0,len(cadena)):#contador de caracteres
    if cadena[i] >= '0' and cadena[i] <= '9' or cadena[i] >= 'A' or cadena[i] <= 'Z' or cadena[i] == '_' or cadena[i] <='a' and cadena[i] >= 'z':
        print '0'        
        if cadena[0] >= '0' and cadena[0] <= '9':
            print cadena[i]
            print 'Nombre de variable no aceptado'
            break
        else:
            print 'nombre de variable correcto'
            print cadena[i]
    else:
        print 'nombre de variable inaceptable'
        break
    
      
            
           