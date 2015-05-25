# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 05:24:01 2013

@author: daniel
"""

# programa: agenda.py
# campos = <nombre>, <apellido> y <telefono>
# fichero = <agenda.txt>
# funciones: busqueda, agregar y borrar

## funciones
# funcion <buscar_entrada>
def buscar_entrada(nombre, apellido):
    f = open('agenda.txt', 'r')
    while 1:
        linea1 = f.readline()
        linea2 = f.readline()
        linea3 = f.readline()
        if linea1 == ' ':
            break
        if nombre == linea1[:-1] and apellido == linea2[:-1]:
            f.close()
            return linea3[:-1]
    f.close
    return ' '
 
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
            fcopia.write(linea1)
            fcopia.write(linea2)
            fcopia.write(linea3)
    f.close()
    fcopia.close()
# copia fichero final en <agenda.txt>    
    fcopia = open('agenda.txt.copia' , 'r')
    f = open('agenda.txt', 'w')
    for linea in fcopia:
        f.write(linea)
    fcopia.close()
    f.close()
    
# funcion <menu>
def menu():
    opcion = ''
    while not ('a' <= opcion <= 'c'):
        print 'Agenda'
        print 'a) Busqueda usuario'
        print 'b) Agrega usuario'
        print 'c) Borra usuario'
        opcion = raw_input('Escoja una opcion: ')
        if not (opcion >= 'a' and opcion <= 'c'):
            print 'Elija opciones validas (a b c)'
    return opcion
    
## cuerpo del programa
# activa funcion <menu>
eleccion = menu()
if eleccion == 'a':
    nombre = raw_input('Nombre del usuario: ')
    apellido = raw_input('Apellido del Usuario: ')
    print buscar_entrada(nombre, apellido)
elif eleccion == 'b':
    nombre = raw_input('Nombre del usuario: ')
    apellido = raw_input('Apellido del Usuario: ')
    telefono = raw_input('Telefono del Usuario: ')
    anyadir_entrada(nombre, apellido, telefono)    
elif eleccion == 'c':
    nombre = raw_input('Nombre del usuario: ')
    apellido = raw_input('Apellido del Usuario: ')
    borrar_entrada(nombre, apellido)
else:
    print
    print 'opcion no valida'