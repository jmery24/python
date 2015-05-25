# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 05:34:17 2013

@author: daniel
"""

#programa: registros_personas.py
#utiliza el modulo <record> para implementar los registros
#Persona define nombre, dni, edad

#importa funcion <record> del modulo <record>
from record import record

class Persona(record):
   nombre = ''
   dni = ''
   edad = 0
   
juan = Persona(nombre = 'Juan Mery', dni = '12345', edad = 32)
diana = Persona(nombre = 'Diana Paola Borgia', dni = '45677', edad = 17)

print juan
print juan.nombre
print juan.dni
print diana
print diana.edad
if diana.edad > 18:
    print diana.nombre, 'mayor de edad'
else:
    print diana.nombre, 'es menor de edad'