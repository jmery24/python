# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:49:53 2013

@author: daniel
"""

class Coche:
    """Abstraccion de los objetos coche."""
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print 'Tenemos', gasolina, 'litros'
        
    def arrancar(self):
        if self.gasolina > 0:
            print 'Arranca'
        else:
            print 'No arranca'

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print 'Quedan', self.gasolina, 'litros'
        else:
            print 'No se mueve'

num = int(raw_input('Cantidad de gasolina: '))
mi_coche = Coche(num)

print 'Tenemos', mi_coche.gasolina, 'litros'
mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.arrancar()
print 'Tenemos', mi_coche.gasolina, 'litros'
