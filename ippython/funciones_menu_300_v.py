# -*- coding: utf-8 -*-
"""
Created on Sat May 25 07:13:50 2013

@author: daniel
"""

#programa: funciones_menu_300_v.py
#variante del ejercicio 300
#se realizan preguntas y solo se acepta: <si SI no NO>
#devuelve: True si la respuesta es afirmativa y False si es negativa
#ejercicio 300_v

#define funcion <si_o_no>
def si_o_no():
    respuesta = ''
    while len(respuesta) != 2 or respuesta  not in 'si SI no NO':
        respuesta = raw_input('Responde la pregunta: ')
        if len(respuesta) != 2 or respuesta  not in 'si SI no NO':
            print
            print 'Elija opciones validas (si - SI - no - NO)'
    return respuesta
            
#cuerpo del programa
#data input
pregunta = ''
while pregunta != '0':
    pregunta = raw_input('Genera una pregunta: ')
    if pregunta == '0':
        break
    contesta = si_o_no()
    if contesta == 'si' or contesta == 'SI':
        print
        print 'True'
    elif contesta == 'no' or contesta == 'NO':
        print
        print 'False'
print
print 'Gracias por usar el programa'