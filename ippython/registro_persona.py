# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 06:27:26 2013

@author: daniel
"""

from datetime import date

class persona:
    def __init__(self,nombre, dni, sexo, dia, mes, anio):
        self.nombre = nombre
        self.dni = dni
        self.sexo = sexo
        self.nace_dia = dia
        self.nace_mes = mes
        self.nace_anio = anio

    def edad(self):
        nacimiento = date(self.nace_anio,self.nace_mes,self.nace_dia)
        dia_de_hoy = date.today()
        edad = dia_de_hoy.year - nacimiento.year
        return (edad)
        
def menor_edad(persona):
    if persona.edad() < 18:
        return True
    else:
        return False
    
def mostrar_persona(persona):
    print 'Nombre: '+ persona.nombre
    print 'dni: '+ persona.dni
    print 'Sexo: '+ persona.sexo
    print 'Edad: ', persona.edad()
    
juan = persona('Juan','23456897', 'M', 6, 5, 1967)
ana = persona('Ana','20987230', 'F', 12, 10, 1975)
    
mostrar_persona(juan)
print
mostrar_persona(ana)
print
print menor_edad(juan)
personas = [juan, ana]
for persona in personas:
    mostrar_persona(persona)
    print personas[0].dni