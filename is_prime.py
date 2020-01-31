# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:05:32 2020

@author: CEC
"""

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()

