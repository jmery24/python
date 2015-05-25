# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 07:10:50 2013

@author: daniel
"""

#programa: funciones_cajero.py
#funcion para sacar dinero del cajero
#billetes de: 50, 20, 10

#definir funcion <sacar_dinero>
def sacar_dinero(cantidad):
    global carga50, carga20, carga10
    if cantidad <= 50 * carga50 + 20 * carga20 + 10 * carga10:
        de50 = cantidad / 50
        cantidad = cantidad % 50
        if de50 >= carga50:
            cantidad = cantidad + (de50 - carga50) * 50
            de50 = carga50
        de20 = cantidad / 20
        cantidad = cantidad % 20
        if de20 >= carga20:
            cantidad = cantidad + (de20 - carga20) * 20
            de20 = carga20
        de10 = cantidad / 10 
        cantidad = cantidad % 10
        if de10 >= carga10:
            cantidad = cantidad + (de20 - carga20) * 20
            de10 = carga10
        carga50 = carga50 - de50
        carga20 = carga20 - de20
        carga10 = carga10 - de10
        return [de50, de20, de10]
    else:
        return [0, 0, 0]
            
#cuerpo del programa

#input
carga50 = 100
carga20 = 100
carga10 = 100

#programa principal
while 50 * carga50 + 20 * carga20 + 10 * carga10 > 0:
    extraer = int(raw_input('Cantidad de dinero solicitada: '))
    [de50, de20, de10] = sacar_dinero(extraer)
    if [de50, de20, de10] != [0, 0, 0]:
        if de50 > 0:
            print 'billetes de 50: ', de50
        if de20 > 0:
            print 'billetes de 20: ', de20
        if de10 > 0:
            print 'billetes de 10: ', de10
        print 'Gracias por usar nuestros servicios'
        print
    else:
        print 'Lamentamos no poder atender su peticion'
        print
print 'Cajero sin dinero, avise al Banco'   