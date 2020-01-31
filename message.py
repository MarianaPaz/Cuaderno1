# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:08:20 2020

@author: CEC
"""

def message():
    print("Enter  next value")

print("We start here")
message()
print("The end is here")

#Funciones con Parámetros

def hi(name):
    print("HI",name)
hi("Victor")

#Funciones con dos Parámetros

def hiAll(name1, name2):
    print("HI",name1)
    print("HI",name2)
hiAll("Mariana", "Kevin")


#Funciones con tres Parámetros

def address(street, city, postalCode):
    print("Your addres is:", street, "St.,",city, postalCode)
    
s= input("Street: ")
pC= input("Postal Code: ")
c= input("City: ")
    
address(s, c, pC)

#Primera forma de pasar valores
def subtra(a, b):
    print(a - b)

subtra(5, 2)
subtra(2, 5)

#Segunda forma de pasar valores
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)
subtra(b=2, a=5)

#Tercera forma de pasar valores
def subtra(a, b):
    print(a - b)

subtra(5, b=2)
subtra(5, 2)

