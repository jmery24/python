# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:38:51 2012

@author: daniel
"""

from Tkinter import *
 
def flecha_mouse(evento):     
 
        cadena['text'] = "Se detecto un clic en X = "+str(evento.x)+" Y = "+str(evento.y) 
 
ventana = Tk()

### root = Tk() 
 
ventana.minsize(400,350)
 
cuadro = Frame(ventana, width =400, height =300, bg="red") 

w = Label(ventana, text="Hola, Leticia!")

w.pack()
 
cuadro.bind("<Button-1>", flecha_mouse) 
 
cuadro.pack() 
 
cadena = Label(ventana) 
 
cadena.pack() 
 
ventana.mainloop()