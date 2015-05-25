# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:22:46 2013

@author: daniel
"""

edad = int(raw_input('Que edad tienes: '))#data input
while edad < 18:#bucle, condicion ser menor que 18
    edad += 1 #equivale a edad = edad + 1
    print 'Felicidades, tienes ' + str(edad)#imprime resultado
    print 'Felicidades, tienes %2i ' %edad#otra manera de imprimir 
    print 'Felicidades, tienes', edad#otro modo de imprimir    