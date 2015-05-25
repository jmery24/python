# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 06:30:32 2013

@author: daniel
"""

from datetime import date

class mascota:
    def __init__(self,nombre, clase, dni, edad):
        self.nombre = nombre
        self.clase = clase
        self.dni = dni
        self.edad = edad

#    def edad(self):
#        nacimiento = date(self.nace_anio,self.nace_mes,self.nace_dia)
#        dia_de_hoy = date.today()
#        edad = dia_de_hoy.year - nacimiento.year
#        return str(edad)
    
def mostrar_mascota(mascota):
    print 'Nombre: '+ mascota.nombre
    print 'Clase: '+ mascota.clase
    print 'dni: '+ mascota.dni
    print 'Edad: ', mascota.edad
    
tigre = mascota('Tigre', 'gato', '23456897', 1)
oso = mascota('Oso', 'perro', '20987230', 17)
    
mostrar_mascota(tigre)
mostrar_mascota(oso)