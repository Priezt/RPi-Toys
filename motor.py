#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import time

PORTS = [11, 9, 10, 22]

GPIO.setmode(GPIO.BCM)
for i in range(4):
	GPIO.setup(PORTS[i], GPIO.OUT)

def set_port(status):
	for i in range(4):
		GPIO.output(PORTS[i], (status[i] == 1))

set_port([1,0,1,1])
time.sleep(200)
