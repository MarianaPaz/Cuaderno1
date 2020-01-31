# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:58:30 2020

@author: CEC
"""

switches = []
devices = ["R1","R2","R3","S1","S2", "R5","R6","R7","S4","S4", "rtS"]
for item in devices:
    if "S" in item:
        switches.append(item)
print (switches)