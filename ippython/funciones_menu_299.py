# -*- coding: utf-8 -*-
"""
Created on Sat May 25 06:20:10 2013

@author: daniel
"""

#programa: funciones_menu_299.py
#funcion menu con opciones
#esta variante de funcion menu es mas eficiente que la anterior
#escrita en funciones_menu.py 
#ejercicio 299

#define funcion <menu>
def menu():
    opcion = ''
    while len(opcion) != 1 or opcion not in '1 2 3':
        print 'Menu Generico'
        print '1) Saludar'
        print '2) Despedirse'
        print '3) salir'
        opcion = raw_input('Escoja una opcion: ')
        if len(opcion) != 1 or opcion not in '1 2 3':
            print
            print 'Elija opciones validas (1 2 3)'
    return opcion
    
#cuerpo del programa
#activa duncion <menu>
eleccion = menu()
if eleccion == '1':
    print
    print 'Hola como estas'
elif eleccion == '2':
    print
    print 'Hasta luego'
else:
    print
    print 'Cerrando archivos'
print
print 'Gracias por usar el programa'