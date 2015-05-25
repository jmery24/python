# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 08:49:23 2013

@author: daniel
"""

#programa: registros_animales_404.py
#print el primer nombre del registro de animales
#ejercicio 404
#llama modulo record
from record import record
#definir funcion <muestra_animales>
def nombre_pila(mascotas):
    print mascotas.nombre[:]
    
class Mascota(record):
    nombre = ''
    tipo = ''
    sexo = ''
    edad = 0
#input
listado = [[Mascota(nombre = 'Tigre Mery', tipo = 'gato', sexo = 'M', edad = 1)],\
          [Mascota(nombre = 'Oso Merrym', tipo = 'perro', sexo = 'M', edad = 17)],\
          [Mascota(nombre = 'Auca Martinez', tipo = 'perro', sexo = 'H', edad = 28)]]
#output
print '----------------'
print 'Nombres de Pila:'
print
for i in range(len(listado)):
    nombre_pila(listado[i][0]) #funciona si solo si: listado[i][0] 
#--------------------------------------------------------