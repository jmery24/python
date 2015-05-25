# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:00:15 2013

@author: daniel
"""

#programa: funciones_anios_276.py
#introducir un anio y determinar si es bisiesto o no
#crear una funcion que devuelva el numero de idas que tenga una anio
#algoritmo:a%4!=0 y a%100!=0 y a%400!=0 (365 dias)
#algoritmo:a%4=0 y a%100!=0 y a%400!=0 (366 dias)
#algoritmo:a%4=0 y a%100=0 y a%400!=0 (365 dias)
#algoritmo:a%4=0 y a%100=0 y a%400=0 (366 dias)
#ejercicio 276

#definir funcion <cantidad_dias>
def cantidad_dias(year):
    if year%4==0 and year%100==0 and year%400==0:
        dias = 366
        return dias
    if year%4==0 and year%100==0 and year%400!=0:
        dias = 365
        return dias
    if year%4==0 and year%100!=0 and year%400!=0:
        dias = 366
        return dias
    if year%4!=0 and year%100!=0 and year%400!=0:
        dias = 365
        return dias
        
#cuerpo del programa
#data input
anio = int(raw_input('Introduzca un anio: '))

#activa la funcion
print 'el anio', anio, 'tiene', cantidad_dias(anio), 'dias'        