# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 07:30:57 2013

@author: daniel
"""

# programa: registros_407.py
# ejercicio 407
# importa modulo <record>
from record import record
# define una clase
class Persona(record):
    nombre = ''
    dni = ''
    edad = 0
# define funcion <copia> 
def copia(pers):
	return Persona(nombre=pers.nombre[:], dni=pers.dni[:], edad=pers.edad)
# define funcion <nada_util
def nada_util(persona1, persona2):
	persona1.edad = persona1.edad + 1
	persona3 = persona2
	persona4 = copia(persona2)
	persona3.edad = persona3.edad - 1
	persona4.edad = persona4.edad - 2
	return persona4
# cuerpo del programa
# input
juan = Persona(nombre='Juan Paz', dni='12345679Z', edad=19)
pedro = Persona(nombre='Pedro Lopez', dni='23456789D', edad=18)
# activa funcion
otro = nada_util(juan, pedro)
# output
print juan
print pedro
print otro