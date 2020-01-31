# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:24:11 2020

@author: CEC
"""

import numpy as np
#Primer ejemplo

#a=np..array([1,2,3])
#print (a)
#b=np.array([(1,2,3), (4,5,6)])
#print (b)

#Segundo ejemplo

"""import time
SIZE = 1000000
L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)
print("\n"*1)
print("RESULTADO USANDO LISTAS/TUPLAS EN PYTHON")

start = time.time()
result = [(x,y) for x,y in zip(L1,L2)]
print ((time.time()-start)*1000)
print("\n"*1)
print("RESULTADO USANDO NUMPY")

start = time.time()
result = A1 + A2
print ((time.time()-start)*1000)


#MAtrices de ceros y unos
import numpy  as np


unos = np.ones((3,4))
print (unos)

ceros = np.zeros((4,5))
print (ceros)

aleatorios = np.random.random((2,2))
print (aleatorios)

vacia = np.empty((3,2))
print (vacia)

full = np.full((2,2),8)
print (full)

full = np.full((5,6),'hola')
print (full)
#MAtriz con valores espaciados uniformenete

espacio1 = np.arange(0,30,5)
print (espacio1)
#MAtriz con 5 valores entre 0 y 2

espacio2 = np.linspace(0,2,5)
print (espacio2)

#crea una matriz identidad
identidad1 = np.eye(4,4)
print (identidad1)

identidad2 = np.identity(4)
print (identidad2)

#conocer las dimensiones de una matriz
a = np.array([(1,2,3),(4,5,6)])
print (a.ndim) \

#conocer el tipo de datos
a = np.array([(1,2,3),(4,5,6)])
print (a.dtype)

#conocer tamaño y forma de la matriz
#a = np.array([(1,2,3,4,5,6)])
a = np.array([(1,2,3),(4,5,6)])
print (a.size)
print (a.shape)

#cambio de forma de una matriz
a = np.array([(1,2,3),(4,5,6)])
print (a)
print("\n"*2)
a=a.reshape(3,2)
print(a)

a = np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,2])

a = np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1)
print(a[0:,1])

a = np.array([(2,4,8)])
print (a.min())
print (a.max())
print (a.sum())

a = np.array([(1,2,3),(3,4,5,)])
print("\n"*2)
print (np.sqrt(a))
print("\n"*2)
print (np.std(a))"""

x = np.array([(1,2,3),(3,4,5)])
y = np.array([(1,2,3),(3,4,5)])
print (x)
print("\n"*2)
print (y)
print("\n"*2)
print (x+y)
print("\n"*2)
print (x-y)
print("\n"*2)
print (x*y)
print("\n"*2)
print (x/y)
print("\n"*2)




