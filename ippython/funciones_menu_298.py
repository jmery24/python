# -*- coding: utf-8 -*-
"""
Created on Fri May 24 07:49:47 2013

@author: daniel
"""

#programa: funciones_menu_298.py
#funcion menu con opciones
#esta variante de funcion menu es mas eficiente que la anterior
#escrita en funciones_menu.py 
#ejercicio 298

#define funcion <menu>
def menu():
    opcion = ''
    while len(opcion) != 1 or opcion not in 'a b c':
        print 'Cajero Automatico'
        print 'a) Ingresa dinero'
        print 'b) Egresa dinero'
        print 'c) Consulta saldo'
        opcion = raw_input('Escoja una opcion: ')
        if len(opcion) != 1 or opcion not in 'a b c':
            print
            print 'Elija opciones validas (a b c)'
    return opcion
    
#cuerpo del programa
#activa duncion <menu>
eleccion = menu()
if eleccion == 'a':
    print
    print 'Monto de dinero a ingresar: '
elif eleccion == 'b':
    print
    print 'Cantidad de dinero deseado: '
else:
    print
    print 'Saldo no disponible'
print
print 'Gracias por usar el programa'