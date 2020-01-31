# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:40:50 2020

@author: CEC
"""

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

def dayOfYear(anio, mes, dia):
    cont = 0
    if dia < 0 or dia > 31 or  mes < 1 or mes > 12:
        return None
    
    elif mes == 2 and ((isYearLeap(anio) and dia >29) or (not isYearLeap(anio) and dia >28)):
        return None
    else:
        for i in range(1, mes):
            md = daysInMonth(anio, i)
            if md == None:
                return None
            cont += md
        md = daysInMonth(anio, mes)
    	if dias >= 1 and dias <= md:
    		return cont + day
    	else:
    		return None
       
    return "tiene " + str(cont) + " días"


def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):
		md = daysInMonth(year, m)
		if md == None:
			return None
		days += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None


       
print(dayOfYear(2020, 1, 18))
print(dayOfYear(2020, 2, 18))
print(dayOfYear(2020, 2, 30))
print(dayOfYear(2020, 2, 29))
print(dayOfYear(2000, 12, 31))


    