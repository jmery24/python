# -*- coding: utf-8 -*-
"""
Created on Sat May 25 06:32:20 2013

@author: daniel
"""

#programa: funciones_menu_300.py
#funcion menu con opciones
#se realizan preguntas y solo se acepta: <si s SI S no n NO N>
#devuelve: True si la respuesta es afirmativa y False si es negativa
#ejercicio 300

#define funciones
#define opcion <menu>
def menu():
    opcion = ''
    while len(opcion) != 1 or opcion not in '1 2 3':
        print 'Preguntas'
        print '1) Es usted terricola ?'
        print '2) Utiliza programas Open Source ?'
        print '3) Le gusta Linux ?'
        opcion = raw_input('Escoja una pregunta: ')
        if len(opcion) != 1 or opcion not in '1 2 3':
            print
            print 'Elija opciones validas (1 2 3)'
    return opcion

#define funcion <si_o_no>
def si_o_no():
    respuesta = ''
    menu()
    while len(respuesta) != 2 or respuesta  not in 'si SI no NO':
        respuesta = raw_input('Responde la pregunta: ')
        if len(respuesta) != 2 or respuesta  not in 'si SI no NO':
            print
            print 'Elija opciones validas (si - SI - no - NO)'
    return respuesta
            
#cuerpo del programa
#activa funcion <si_o_no>
eleccion = si_o_no()
if eleccion == 'si' or eleccion == 'SI':
    print
    print 'True'
elif eleccion == 'no' or eleccion == 'NO':
    print
    print 'False'
print
print 'Gracias por usar el programa'