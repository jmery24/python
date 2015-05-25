# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 06:54:40 2013

@author: daniel
"""

# programa: agenda_alternativa.py
# el programa tiene las mismas caracteristicas del programa <agenda.py>
# pero se maneja con registros, o sea definimos un nuevo tipo de dato

# importa la funcion <record> del modulo <record>
from record import record

# tipo entrada
class Entrada(record):
    nombre = ''
    apellido = ''
    telefono = ''
    
# funcion <lee_entrada>
def lee_entrada():
    nombre = raw_input('Nombre: ')
    apellido = raw_input('Apellido: ')
    telefono = raw_input('Telefono: ')
    return Entrada(nombre=nombre, apellido=apellido, telefono=telefono)
    
# tipo agenda
class Agenda(record):
    lista = []
    
# funcion <cargar_agenda>
def cargar_agenda(agenda):
    agenda.lista = []
    f = open('agenda.txt', 'r')
    while 1:
        linea1 = f.readline()
        linea2 = f.readline()
        linea3 = f.readline()
        if linea1 == '':
            break
        entrada = Entrada(nombre=linea1[:-1], apellido=linea2[:-1], telefono=linea3[:-1])
        agenda.lista.append(entrada)
    f.close()
    
# funcion <guardar_agenda>
def guardar_agenda(agenda):
    f = open('agenda.txt', 'w')
    for entrada in agenda.lista:
        f.write(entrada.nombre + '\n')
        f.write(entrada.apellido + '\n')
        f.write(entrada.telefono + '\n')
    f.close()
    
# estas tres funciones no trabajan con el fichero, sino con los datos
# almacenados previamente en la memoria

# funcion <buscar_telefono>
def buscar_telefono(agenda, nombre, apellido):
    for entrada in agenda.lista:
        if entrada.nombre == nombre and entrada.apellido == apellido:
            return entrada.telefono
    return ''

# funcion <anyadir_entrada>
def anyadir_entrada(agenda, entrada):
    agenda.lista.append(entrada)
    
# funcion <borrar_entrada>
def borrar_entrada(agenda, nombre, apellido):
    for i in range(len(agenda.lista)):
        if agenda.lista[i].nombre == nombre and agenda.lista[i].apellido == apellido:
            del agenda.lista[i]
            return
            
# funcion <menu>
def menu():
    print '     ------'
    print '     AGENDA'
    print '     ------'
    print '1) Agregar Entrada'
    print '2) Consultar Agenda'
    print '3) Borrar Entrada'
    print '4) Salir del Programa'
    print
    opcion = int(raw_input('Elije Opcion: '))
    while opcion < 1 and opcion >4:
        opcion = int(raw_input('Elije Opcion <1 2 3 4>: '))
    return opcion
    
# programa principal
agenda = Agenda()
cargar_agenda(agenda)
opcion = menu()
while opcion != 4:
    if opcion == 1:
        entrada = lee_entrada()
        anyadir_entrada(agenda, entrada)        
    elif opcion == 2:
        nombre = raw_input('Nombre: ')
        apellido = raw_input('Apellido: ')        
        telefono = buscar_telefono(agenda, nombre, apellido)
        if telefono == '':
            print ' No esta en la Agenda'
        else:
            print 'Telefono', telefono
    elif opcion == 3:
        
        borrar_entrada(agenda, nombre, apellido)
    opcion = menu()
    guardar_agenda(agenda)