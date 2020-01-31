# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:31:12 2020

@author: CEC
"""

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(25,GPIO.IN)

while True:
    if GPIO.input(25):
        GPIO.output(22,False)
    else:
        GPIO.output(22,True)
