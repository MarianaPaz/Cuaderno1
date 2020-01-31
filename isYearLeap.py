# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:07:30 2020

@author: CEC
"""

def isYearLeap(anio):
    if anio % 4 == 0  and  (anio % 100 != 0  or  anio % 400 == 0):
        return True
    else:
        return False

    
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
