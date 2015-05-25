# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 05:21:49 2013

@author: daniel
"""

# programa: registros_calificacion_estudiantes.py
# gestion de calificaciones de estudiantes de una asignatura
# datos del estudiante: nombre, grupo de teoria, nota obtenida
# entrega de las memorias de practicas
# aprueba asginatura: si entrego la memoria y la nota >= 5
# menu: Alta estudiante, modifica datos, baja estudiante, mustra ficha, 
# listado completo, listado de nombres, salir del programa

# importamos modulo <record>
from record import record

# define clase
class Estudiante(record):
    nombre = ''
    grupo = ''
    nota = 0.0
    practica = False
    
# funciones

# funcion <existe_estudiante>
def existe_estudiante(lista, nombre):
    for estudiante in lista:
        if nombre == estudiante.nombre:
            return True
    return False

# funcion <crea_estudiante_por_teclado>
def crea_estudiante_por_teclado():
    nombre = raw_input('Nombre: ')
    grupo = raw_input('A, B , C :')
    while grupo not in ['A', 'B', 'C']:
        grupo = raw_input('A, B , C :')
    nota = float(raw_input('Nota: '))
    while nota < 0 or nota >10:
        nota = float(raw_input('Nota: '))
    entregada = raw_input('Practica entregada <s/n>: ')
    while entregada.lower() not in ['s', 'n']:
                entregada = raw_input('Practica entregada <s/n>: ')
    practica = entregada.lower() == 's' # cual es su utilidad ???
    return Estudiante(nombre=nombre,grupo=grupo,nota=nota, practica=practica)        

# funcion <anyade_estudiante>
def anyade_estudiante(lista, estudiante):
    if not existe_estudiante(lista, estudiante):
        lista.append(estudiante)
        return True
    else:
        return False
        
# funcion <modifica_estudiante>
def modifica_estudiante(lista, estudiante):
    for i in range(len(lista)):
        if lista[i].nombre == estudiante.nombre:
            lista[i] = estudiante
            return True
    return False            

# funcion <elimina_estudiante>
def elimina_estudiante(lista, nombre):
    for i in range(len(lista)):
        if lista[i].nombre == nombre:
            del lista[i]
            return True
    return False

# funcion <muestra_estudiante>
def muestra_estudiante(estudiante):
    print 'Nombre      %s' %estudiante.nombre
    print 'Grupo       %s' %estudiante.grupo
    print 'Nota        %3.1f' %estudiante.nota
    if estudiante.practica:
        print 'Memoria de practicas entregada'
    else:
        print 'Memoria de practicas no entregada'
        
# funcion <busca_y_muestra_estudiante>
def busca_y_muestra_estudiante(lista, nombre):
    for estudiante in lista:
        if estudiante.nombre == nombre:
            muestra_estudiante(estudiante)
            return
    print 'No existe en las listas el estudiante'
    
# funcion <listado_completo>
def listado_completo(lista):
    for estudiante in lista:
        muestra_estudiante(estudiante)
        
# funcion <listado_de_nombres
def listado_de_nombres(lista):
    for estudiante in lista:
        print estudiante.nombre
        
# funcion <calificacion_acta>
def calificacion_acta(estudiante):
    if not estudiante.practica:
        return 'No presentado'
    elif estudiante.nota < 5:
        return 'Suspenso'
    elif estudiante.nota < 7:
        return 'Aprobado'
    elif estudiante.nota < 8.5:
        return 'Notable'
    elif estudiante.nota < 10:
        return 'Sobresaliente'
    else:
        return 'Matricula de Honor'

# funcion <muestra_acta>
def muestra_acta(lista):
    for estudiante in lista:
        print estudiante.nombre, calificacion_acta(estudiante)
        
# funcion <nota_media>
def nota_media(lista):
    suma = 0 
    contador = 0
    for estudiante in lista:
        if estudiante.practica:
            suma += estudiante.nota
            contador += 1
    if contador != 0:
        return suma / float(contador)
    else:
        return 0
        
# funcion <muestra_nota_media>
def muestra_nota_media(lista):
    print 'Nota promedio: ', nota_media(lista)
                
# funcion <porcentaje_de_practicas_entregadas>
def porcentaje_de_practicas_entregadas(lista):
    contador = 0
    for estudiante in lista:
        if estudiante.practica:
            contador += 1
    if len(lista) != 0:
        return 100 * contador / float(len(lista))
    else:
        return 0

# funcion <muestra_porcentaje_practicas_entregadas>
def muestra_porcentaje_practicas_entregadas(lista):
    print 'Porcentaje de practicas entregadas: ', porcentaje_de_practicas_entregadas(lista) 
        
# funcion <mejores_estudiantes>
def mejores_estudiantes(lista):
    nota_mas_alta = 0
    mejores = []
    for estudiante in lista:
        if estudiante.practica:
            if estudiante.nota > nota_mas_alta:
                mejores = [estudiante]
                nota_mas_alta = estudiante.nota
            elif estudiante.nota == nota_mas_alta:
                mejores.append(estudiante)
    return mejores
    
# funcion <muestra_mejores_estudiantes>
def muestra_mejores_estudiantes(lista):
    los_mejores = mejores_estudiantes(lista)
    for estudiante in los_mejores:
        print 'Mejor estudiante: ', estudiante.nombre
        
# funcion <menu>
def menu():
    print '-' *79
    opcion = 0
    while opcion <1 or opcion > 11:
        print ' 1)  Dar de alta a nuevo estudiante.'
        print ' 2)  Modificar los datos de un estudiante.'
        print ' 3)  Dar de baja a un estudiante.'
        print ' 4)  Mostrar fiche de un estudiante'
        print ' 5)  Listado completo.'
        print ' 6)  Listado de nombres.'
        print ' 7)  Actas de calificaciones.'
        print ' 8)  Nota Media.'
        print ' 9)  Practicas entregadas % .'
        print ' 10) Mejores estudiantes.'
        print ' 11) Salir del programa.'
        opcion = int(raw_input('Escoge Opcion: '))
    return opcion

# programa principal
# input
estudiantes = []

opcion = 0
while opcion != 11:
    opcion = menu()
    if opcion == 1: # dar de alta a un estudiante
        estudiante = crea_estudiante_por_teclado()
        if anyade_estudiante(estudiantes, estudiante):
            print 'Estudiante %s dado de alta.' % estudiante.nombre
        else:
            print 'Estudiante %s pertenece a la lista.' % estudiante.nombre
    elif opcion == 2: # modificar estudiante
        estudiante = crea_estudiante_por_teclado()
        if modifica_estudiante(estudiantes, estudiante):
            print 'Estudianteb %s modificado.' % estudiante.nombre
        else:
            print 'No existe el estudiante %s.' % estudiante.nombre
    elif opcion == 3: # eliminar estudiante
        nombre = raw_input('Nombre: ')
        if elimina_estudiante(estudiantes, nombre):
            print 'Estudiante %s eliminado' % nombre
        else:
            print 'No existe el estudiante %s' % nombre
    elif opcion == 4: # mostrar ficha de un estudiante
        nombre = raw_input('Nombre: ')
        busca_y_muestra_estudiante(estudiantes, nombre)
    elif opcion == 5: # mostrar listado completo
        listado_completo(estudiantes)
    elif opcion == 6: # mostrar listado de nombres
        listado_de_nombres(estudiantes)
    elif opcion == 7:
        muestra_acta(estudiantes)
    elif opcion == 8:
        muestra_nota_media(estudiantes)
    elif opcion == 9:
        muestra_porcentaje_practicas_entregadas(estudiantes)
    elif opcion == 10:
        muestra_mejores_estudiantes(estudiantes)
        
print 'Gracias por utilizar el programa.'
