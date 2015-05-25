# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:21:39 2013

@author: daniel
"""
#programa: funciones_orden_354_355.py
#dos funciones para ordenar una lista 
#orden de menor a mayor y viceversa
#ejercicios 354 y 355

#definir funciones
#funcion <ordenmayor>
def ordenmayor(lista):
    print
    print 'lista original: ', lista
    lista.sort()   
    return lista
#funcion <ordenmenor>
def ordenmenor(lista):
    print 'lista original: ', lista
    lista.sort()
    lista.reverse()
    return lista    

#menu
while 1:
    print """
        Opciones
    1.- Ordenar de Menor a Mayor.
    2.- Ordenar de Mayor a Menor.
    3.- Salir del programa.
    """
    opcion=input("Seleccione opcion: ")
    listado = [10, 2, 5, 3, 8, 7]
    print
#    print 'listado original: ', listado
    if opcion==1:
       mayor = ordenmayor(listado)
       print 'listado ordenado: ', mayor
       
    elif opcion==2:
        menor = ordenmenor(listado)
        print 'listado ordenado: ', menor
        
    elif opcion == 3:
        print 'gracias por utilizar el programa'
        break
    else:
        print 'Opcion no valida, seleccione 1. 2. 3.'