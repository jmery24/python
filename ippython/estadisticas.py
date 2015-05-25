# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 06:28:11 2013

@author: daniel
"""
#programa: estadisticas.py
#modulo estadisticas con funciones para calcular: media, varianza y
#desviacion tipica

#importa funcion <sqrt> frl modulos <math>
from math import sqrt

#definir funciones

#definir funcion <media>
def media(lista):
    s = 0
    for elemento in lista:
        s += elemento
    return s / float(len(lista))
#definir funcion <varianza>
def varianza(lista):
    s = 0
    for elemento in lista:
        s += (elemento - media(lista)) ** 2
    return s / float(len(lista))
#definir funcion <desviacion tipica>
def desviacion_tipica(lista):
    return sqrt(varianza(lista))
    
#prueba de las funciones del modulo, no funciona cuando se lo invoca
if __name__ == '__main__':
    listado = [5.0, 6.0, 7.0, 3.0, 4.0, 5.0]
    print 'Lista: ' , listado
    print
    print '    Media: %16.2f' %media(listado)
    print '    Varianza: %13.2f' %varianza(listado)
    print '    Desviacion Tipica: %2.2f' %desviacion_tipica(listado)    