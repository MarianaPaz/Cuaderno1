# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 19:26:22 2020

@author: CEC
"""
while True:
    
    firstname = input("What is your first name?  ")
    lastname = input("What is your last name?  ")
    location = input("What is your location?  ")
    age = int(input("What is your age?  "))
    space = " "
    print("Hola mi nombre es " + firstname+space+lastname + " mi dirección es " + location+ " tengo " + str(age) + " años")
    if age >=1 and age <=18:
        print ("Usted es joven")
    elif age >=19 and age <=30:
        print ("Usted es muy joven")
    else:
        print ("Usted es viejo")
    x =  input("Desea salir?  ")
    if x == 'SI' or x == 'S':
        break