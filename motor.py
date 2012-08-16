#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import time

PORTS = [11, 9, 10, 22]

ROLLING_SIG = [
	[0, 0, 0, 1],
	[0, 0, 1, 1],
	[0, 0, 1, 0],
	[0, 1, 1, 0],
	[0, 1, 0, 0],
	[1, 1, 0, 0],
	[1, 0, 0, 0],
	[1, 0, 0, 1]
]

GPIO.setmode(GPIO.BCM)
for i in range(4):
	GPIO.setup(PORTS[i], GPIO.OUT)

def set_port(status):
	for i in range(4):
		GPIO.output(PORTS[i], (status[i] == 1))

def whirl(clockwise=True, speed=1, times = 1000):
	for i in range(times):
		step = i % 8
		if not clockwise:
			step = 7 - step
		set_port(ROLLING_SIG[step])
		time.sleep(0.01 / speed)

clockwise = True
speed = 10
times = 1000
if len(sys.argv) > 1:
	clockwise = int(sys.argv[1]) == 1
if len(sys.argv) > 2:
	speed = int(sys.argv[2])
if len(sys.argv) > 3:
	times = int(sys.argv[3])

whirl(clockwise, speed, times)
