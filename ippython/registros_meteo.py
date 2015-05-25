# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 06:29:51 2013

@author: daniel
"""

#programa: registros_meteo.py
#evalua la temperatura y lluvia caida en distintas estaciones

#importa modulo <record>
from record import record
#crea clase
class Meteo(record):
    estacion = ''
    temp = [0,0,0,0]
    lluvia = [0,0,0,0]
    
#definir funcion <mostrar_meteo>
def mostrar_meteo(meteo):
    print ' Estacion Meteorologica:', meteo.estacion
    print ' ---------------------------'
    print ' Hora    Temperatura Litros/M2'
    print ' 0:00  %11.2f %9.2f' %(meteo.temp[0], meteo.lluvia[0])
    print ' 0:00  %11.2f %9.2f' %(meteo.temp[1], meteo.lluvia[1])
    print ' 0:00  %11.2f %9.2f' %(meteo.temp[2], meteo.lluvia[2])
    print ' 0:00  %11.2f %9.2f' %(meteo.temp[3], meteo.lluvia[3])

#input
cs = Meteo(estacion ='CS1', temp=[20.2,19.1,27.2,24.8], lluvia=[0,0,0,0])
vr = Meteo(estacion ='VR1', temp=cs.temp[:], lluvia=cs.lluvia[:])
#estas sentencias apuntan <vr> a <cs>, trabajan en la misma alocacion
#vr = cs
#vr.estacion = 'VR1' 
mostrar_meteo(cs)
print
mostrar_meteo(vr)