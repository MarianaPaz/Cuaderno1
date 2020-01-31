# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:31:12 2020

@author: CEC
"""

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

while True:
    GPIO.output(18, True)
    time.sleep(3)
    GPIO.output(18,False)
    time.sleep(4)