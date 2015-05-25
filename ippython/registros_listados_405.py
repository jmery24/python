# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:29:22 2013

@author: daniel
"""

#programa: registros_listados_405.py
#el programa agrega nombres desde el teclado
#pregunta si queremos agregar otro dato (si/no)
#ejercicio 405
#cuerpo del programa
listado = []
opcion = 'si'
while opcion == 'si':
    nombre = raw_input('Nombre del usuario: ')
    edad = int(raw_input('Edad del usuario: '))
    listado.append(nombre)
    listado.append(edad)
    opcion = raw_input('Desea agregar mas datos ? <si/no>: ')
#output
print listado
print 'Gracias por utilizar el programa'