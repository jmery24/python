# -*- coding: utf-8 -*-
"""
Created on Fri May 24 07:34:04 2013

@author: daniel
"""

#programa: funciones_menu.py
#funcion menu con opciones

#define funcion <menu>
def menu():
    opcion = ''
    while not ('a' <= opcion <= 'c'):
        print 'Cajero Automatico'
        print 'a) Ingresa dinero'
        print 'b) Egresa dinero'
        print 'c) Consulta saldo'
        opcion = raw_input('Escoja una opcion: ')
        if not (opcion >= 'a' and opcion <= 'c'):
            print 'Elija opciones validas (a b c)'
    return opcion
    
#cuerpo del programa
#activa funcion <menu>
eleccion = menu()
if eleccion == 'a':
    print
    print 'Monto de dinero a ingresar: '
elif eleccion == 'b':
    print
    print 'Cantidad de dinero deseado: '
elif eleccion == 'c':
    print
    print 'Saldo no disponible'
else:
    print
    print 'opcion no valida'
