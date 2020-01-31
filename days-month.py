# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:42:08 2020

@author: CEC
"""


def isYearLeap(anio):
    if anio % 4 == 0  and  (anio % 100 != 0  or  anio % 400 == 0):
        return True
    else:
        return False
    
    
    
def daysInMonth(anio, mes):
    list = [31, 28, 31,30,31,30,31,31,30,31,30,31]
    if anio < 1500 or  mes < 1 or mes > 12:
        return
    if isYearLeap(anio):
       list = [31, 29, 31,30,31,30,31,31,30,31,30,31]
    return list[mes-1]


     
       
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

    