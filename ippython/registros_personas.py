# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:35:13 2013

@author: daniel
"""

#programa registros_personas.py
#se crea un registro para manejar datos de las personas

#importar modulo <record>
from record import record
#definir class <Persona>
class Persona(record):
    nombre = ''
    dni = ''
    edad = 0
#definir funcion <mostrar_persona>
def mostrar_persona(persona):
    print 'Nombre: ', persona.nombre
    print 'DNI: ', persona.dni
    print 'Edad: ', persona.edad
#cuerpo del programa
#input
juan = Persona(nombre = 'Juan Paz', dni = '12345678Z', edad = 19)
ana = Persona(nombre = 'Ana Mir', dni = '23456789Z', edad = 18)
listado = [juan, ana]
#activar funcion
mostrar_persona(juan)
mostrar_persona(ana)
print '*****************'
mostrar_persona(listado[0]),
mostrar_persona(listado[1])
print '*****************'
for i in range(len(listado)):
    mostrar_persona(listado[i])   