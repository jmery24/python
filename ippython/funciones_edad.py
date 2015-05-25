# -*- coding: utf-8 -*-
"""
Created on Thu May  9 07:50:09 2013

@author: daniel
"""

#programa: funciones_edad.py
#definir una funcion para evaluar si es mayor o menor de edad

#definir la funcion mayor_edad
def mayor_edad(edad):
    if edad < 18:
        resultado = False
    else:
        resultado = True
    return resultado
    
#definir funcion alternativa y optimizada mayoria_edad
def mayoria_edad(edad):
    if edad < 18:
        return False
    else:
        return True

#funcion alternativa, ejercicio 268
def mayoria_de_edad(edad):
    if edad < 18:
        return False
    return True
    
#funcion alternativa, ejercicio 269
def mayor_de_edad(edad):
    return edad >= 18
   
#data input
edad = int(raw_input('Que edad tienes: '))

#invoca o activa funcion
print 'eres mayor de edad? ', mayor_edad(edad)
print 'tienes mayoria de edad? ', mayoria_edad(edad)
print 'eres mayor de edad? ', mayoria_de_edad(edad)
print 'realmente eres mayor de edad?', mayor_de_edad(edad) 