# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 06:34:48 2013

@author: daniel
"""

#definir funcion <muestra>
def muestra(a):
    print a[0],
    for i in range(1, len(a)):
        print '+', a[i], 'X **', i,
    print
#definir funcion <evalua>
def evalua(a, x):
    s = 0
    for i in range(len(a)):
        s = s + a[i] * x**i
    return s
#definir funcion <suma>
def suma(a, b):
    #creamos un polinomio nulo de orden igual al de mayor orden
    c = [0] * max(len(a), len(b))
    #sumamos los coeficientes hasta el orden menor
    for i in range(min(len(a), len(b))):
        c[i] = a[i] + b[i]
    #copiamos el resto de los coeficientes del polinomio de mayor orden
    if len(a) > len(b):
        for i in range(len(b), len(c)):
            c[i] = a[i]
    else:
        for i in range(len(a), len(c)):
            c[i] = b[i]
    #devolvemos el polinomio c
    normaliza(c)
    return c
#definir funcion <sumatorio> alternativa a funcion <suma>
def sumatorio( a, b):
    c = []
    m = min(len(a), len(b))
    for i in range(m):
        c.append(a[i] + b[i])
    c = c + a[m:] + b[m:]
    normaliza(c)
    return c
#definir funcion <normaliza>
def normaliza(a):
    while len(a) > 0 and a[-1] == 0:
        del a[-1]
#definir funcion <resta>
def resta(a, b):
    #creamos un polinomio nulo de orden igual al de mayor orden
    c = [0] * max(len(a), len(b))
    #sumamos los coeficientes hasta el orden menor
    for i in range(min(len(a), len(b))):
        c[i] = a[i] - b[i]
    #copiamos el resto de los coeficientes del polinomio de mayor orden
    if len(a) > len(b):
        for i in range(len(b), len(c)):
            c[i] = a[i]
    else:
        for i in range(len(a), len(c)):
            c[i] = b[i]
    #devolvemos el polinomio c
    normaliza(c)
    return c
#definir funcion <sustraccion> alternativa a funcion <resta>
def sustraccion( a, b):
    c = []
    m = min(len(a), len(b))
    for i in range(m):
        c.append(a[i] - b[i])
    c = c + a[m:] + b[m:]
    normaliza(c)
    return c 
#definir funcion <multiplica>
def multiplica(a, b):
    orden = len(a) + len(b) - 2
    c = [0] * (orden + 1)
    for i in range(orden+1):
        s=0
        for j in range(i+1):
            s += a[j] * b[i-j]
            c[i] == s
    return c
   
#prueba de las funciones del modulo, no funciona cuando se lo invoca
if __name__ == '__main__':
    polinomio_a = [1, 2, 4, 5, 0, 6]
    polinomio_b = [1, 3, 6, 7, 8, 6]
    #prueba funcion <muestra>
    print 'Polinomio A = ',  
    muestra(polinomio_a)
    #prueba funcion <evalua>
    variable = 2
    print 'Polinomio A = ',
    print evalua(polinomio_a, variable)
    #prueba funcion <suma>
    print 'polinomio A + polinomio B = ',
    print suma(polinomio_a, polinomio_b)
    muestra(suma(polinomio_a, polinomio_b))
    #prueba funcion <sumatorio>
    print 'polinomio A + polinomio B = ',
    print sumatorio(polinomio_a, polinomio_b)
    muestra(sumatorio(polinomio_a, polinomio_b))
    #prueba funcion <resta>
    print 'polinomio A - polinomio B = ',
    print resta(polinomio_a, polinomio_b)
    muestra(resta(polinomio_a, polinomio_b))
    #prueba funcion <sustraccion>
    print 'polinomio A - polinomio B = ',
    print sustraccion(polinomio_a, polinomio_b)
    muestra(sustraccion(polinomio_a, polinomio_b))
    #prueba funcion <multiplica>
    print 'polinomio A x polinomio B = ',
    print multiplica(polinomio_a, polinomio_b)
    muestra(multiplica(polinomio_a, polinomio_b))