# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:15:31 2020

@author: CEC
"""

def isprime(n):
    '''chequear si un entero es primo'''
    # chequear que la entrada sea un entero positivo
    n = abs(int(n))
    # 0 y 1 no son primos
    if n < 2:
        return False
    # 2 es el unico primo par
    if n == 2: 
        return True    
    # El resto de pares no son primos
    if not n & 1: 
        return False
    #El rango comienza en 3 y solo necesita subir hasta la raiz cuadrada de n 
    # para todos los impares
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

print(isprime(17))

for i in range(1, 20):
	if isprime(i + 1):
			print(i + 1, end=" ")
print()
