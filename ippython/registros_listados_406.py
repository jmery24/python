# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:08:59 2013

@author: daniel
"""

#programa: registros_listados_406.py
#muestra la persona de mayor edad
#ejercicio 406
#cuerpo del programa
#importar modulo <record>
from record import record
#definir class <Persona>
class Persona(record):
    nombre = ''
    dni = ''
    edad = 0
#definir funcion <mostrar_persona>
def mostrar_persona(persona):
    for i in range(len(persona)):
        for j in range(0, len(persona[0])):
            if persona[i][j] < '18':
                    print persona[i][0]
#definir funcion <entrada_datos>
def entrada_datos():
    filas = int(raw_input('numero de filas: '))
    columnas = int(raw_input('numero de columnas: '))
    M = []
    for i in range(filas):
            M.append([0]*columnas) 
    opcion = 'si'
    while opcion == 'si':
        for j in range(filas):
            for k in range(columnas):
                M[j][k] = raw_input('Dame el componente (%d,%d): ' %(j,k))
        opcion = raw_input('Desea agregar mas datos ? <si/no>: ')
    print M    
    mostrar_persona(M)
        
#output
#personas = entrada_datos()
#personas = entrada_datos()
entrada_datos() 
print 'es menor de edad'
print
print 'Gracias por utilizar el programa'