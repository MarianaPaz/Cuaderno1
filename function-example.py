# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:31:46 2020

@author: CEC
"""

def pultiply(a, b):
    return a * b

print(pultiply(3, 4))

def pultiply(a, b):
    return  

print(pultiply(3, 4))


def wishes():
    return "Happy Birthday!"

w = wishes()

print(w)


def wishes():
    print("My Wishes")
    return "Happy Birthday!"

wishes()

def wishes():
    print("My Wishes")
    return "Happy Birthday!"

print(wishes())


#Puede usar una lista como argumento
def hiEverybody(mylist):
    for name in mylist:
        print("Hi,", name)
        
hiEverybody(["Victor", "Kevin", "Mariana", "Ivonne"])

def hiEverybody(mylist):
    for name in mylist:
        print("Hi,", name)
        
hiEverybody(["Victor", "Kevin"])

#Una lista es el resultado de una funcion
def createList(n):
    myList = []
    for i in range(n):
        myList.append(i)
    return myList

print(createList(10))

