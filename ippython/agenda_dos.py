# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 06:44:41 2013

@author: daniel
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 05:24:01 2013

@author: daniel
"""

# programa: agenda_dos.py
# campos = <nombre>, <apellido> y <telefono>
# fichero = <agenda.txt>
# funciones: busqueda, agregar y borrar
# implementa <menu> con salida

## funciones
# funcion <buscar_entrada>
def buscar_entrada(nombre, apellido):
    f = open('agenda.txt', 'r')
    while 1:
        linea1 = f.readline()
        linea2 = f.readline()
        linea3 = f.readline()
        if linea1 == '':
            break
        if nombre == linea1[:-1] and apellido == linea2[:-1]:
            f.close()
            return linea3[:-1]
    f.close()
    return ''
 
# funcion <anyadir_entrada>
def anyadir_entrada(nombre, apellido, telefono):
    f = open('agenda.txt', 'a')
    f.write(nombre + '\n')
    f.write(apellido + '\n')
    f.write(telefono + '\n')
    f.close()
    
# funcion <borrar_entrada>
def borrar_entrada(nombre, apellido):
    f = open('agenda.txt', 'r')
    fcopia = open('agenda.txt.copia', 'w')
    while 1:
        linea1 = f.readline()
        linea2 = f.readline()
        linea3 = f.readline()
        if linea1 == '':
            break
        if nombre != linea1[:-1] or apellido != linea2[:-1]:
            fcopia.write(linea1 + linea2 + linea3) # sustituye las 3 lineas 
#            fcopia.write(linea1)
#            fcopia.write(linea2)
#            fcopia.write(linea3)
    f.close()
    fcopia.close()
# copia fichero final en <agenda.txt>    
    fcopia = open('agenda.txt.copia' , 'r')
    f = open('agenda.txt', 'w')
    for linea in fcopia:
        f.write(linea)
    fcopia.close()
    f.close()
    
## programa principal
# menu de opciones y procesamiento
opcion = ''
while True:
    print '      ------'
    print '      Agenda'
    print '      ------'
    print 'a) Busqueda usuario'
    print 'b) Agrega usuario'
    print 'c) Borra usuario'
    print 'd) Salida del programa'
    print
    opcion = raw_input('Escoja una opcion: ')
    if not (opcion >= 'a' and opcion <= 'd'):
        print 'Elija opciones validas (a b c d)'
    if opcion == 'a':
        nombre = raw_input('Nombre del usuario: ')
        apellido = raw_input('Apellido del Usuario: ')
        print buscar_entrada(nombre, apellido)
    elif opcion == 'b':
        nombre = raw_input('Nombre del usuario: ')
        apellido = raw_input('Apellido del Usuario: ')
        telefono = raw_input('Telefono del Usuario: ')
        anyadir_entrada(nombre, apellido, telefono)
    elif opcion == 'c':
        nombre = raw_input('Nombre del usuario: ')
        apellido = raw_input('Apellido del Usuario: ')
        borrar_entrada(nombre, apellido)
    elif opcion == 'd':
        print '--------------------------------'
        print 'Gracias por utilizar el programa'
        print '--------------------------------'
        break