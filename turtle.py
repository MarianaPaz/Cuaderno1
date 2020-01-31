# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:38:56 2020

@author: CEC
"""
from turtle import *
color('red', 'red')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()