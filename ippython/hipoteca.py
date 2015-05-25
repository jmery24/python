# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:29:19 2013

@author: daniel
"""
#modulo: hipoteca.py
#agrupa funciones para calculo de la cuota y el porcentaje de interes
#que se paga por una hipoteca de <n> anios a un <interes> dado

#definir funciones del modulo
#define funcion <cuota>
def cuota(h, n, i):
    r = i / (100 * 12)
    m = h * r / (1 - (1 + r) ** (-12 * n))
    return m 
#define funcion <porciento>
def porciento(h, n, i):
    r = i / (100 * 12)
    m = h * r / (1 - (1 + r) ** (-12 * n))
    cantidad = m * 15 * 12
    interes = cantidad - h
    porcentaje = (interes * 100) / h
    return porcentaje
def menu():
    opcion = ''
    while not ('a' <= opcion <= 'c'):
        print '   Hipotecas'
        print 'a) Calculo cuota'
        print 'b) Pago de interes <porcentaje>'
        print 'c) Salida del programa'
        opcion = raw_input('Escoja una opcion: ')
        if not (opcion >= 'a' and opcion <= 'c'):
            print 'Elija opciones validas (a b c)'
    return opcion
    
#prueba de las funciones del modulo, no funciona cuando se lo invoca
if __name__ == '__main__':
    print 'Valor de la cuota: ', cuota(50000.0, 8, 2.0)
    print 'Porcentaje del capital que se paga: ', porciento(50000.0, 8, 2.0)