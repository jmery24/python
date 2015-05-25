# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:48:17 2013

@author: daniel
"""
#ejercicio 179

binario = raw_input('Introduce un numero binario: ')
marca = 0#marca es una variable para indicar el estado el numero )binario o no)

while binario != ' ':
    for i in range(0, len(binario)):
        if binario[i] < '0' or binario[i] > '1':
            print binario[i], 'no es un numero binario'
            marca += 1#numero no binario incrementa marca
    if marca == 0:#estado: condicion del numero binario
        print binario, 'es un numero binario'
    else:#marca != 0, condicion de no binario
        print binario, 'no es un numero binario'
    binario = raw_input('Introduce un numero binario: ')
    if binario == ' ':
        print 'gracias por usar el programa'
        break
            

 
        
    
        
    