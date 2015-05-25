# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:47:24 2013

@author: daniel
"""

edad = int(raw_input('Edad: '))#data input
while edad < 18:#bucle mientras edad menor que 18
    edad = edad + 1#aumenta la edad 1 en 1
    if edad % 2 == 0:#condicion para numeros pares
        continue#si cumple la condicion anterior salta al proximo numero
    print 'Felicidades, tienes ' + str(edad)#print out