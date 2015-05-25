# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/daniel/.spyder2/.temp.py
"""
# importa funcion sqrt
from math import sqrt

#data input
ax = int(raw_input("abcisa punto A: "))
ay = int(raw_input("ordenada punto A: ")) 
bx = int(raw_input("abcisa punto B: "))
by = int(raw_input("ordenada punto B: "))
cx = int(raw_input("abcisa punto C: "))
cy = int(raw_input("ordenada punto C: "))
dx = int(raw_input("abcisa punto D: "))
dy = int(raw_input("ordenada punto D: "))
ex = int(raw_input("abcisa punto E: "))
ey = int(raw_input("ordenada punto E: "))

#processing data
canx = bx
cany = by
if abs(sqrt((ax-cx)**2+(ay-cy)**2)) < abs(sqrt((ax-canx)**2+(ay-cany)**2)):
    canx = cx
    cany = cy
if abs(sqrt((ax-dx)**2+(ay-dy)**2)) < abs(sqrt((ax-canx)**2+(ay-cany)**2)):
    canx = dx
    cany = dy
if abs(sqrt((ax-ex)**2+(ay-ey)**2)) < abs(sqrt((ax-canx)**2+(ay-cany)**2)):
    canx = ex
    cany = ey
    
#printout
print 'el punto ','(', canx,',', cany,')' 'es el mas cercano al punto ', '(', ax,',', ay, ')'


