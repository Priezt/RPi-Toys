#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import time

if len(sys.argv) < 4:
	raise Exception('switch.py <GPIO num> <interval> <times>')

port = int(sys.argv[1])
interval = float(sys.argv[2])
times = int(sys.argv[3])

GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.OUT)

for i in range(times):
	GPIO.output(port, True)
	time.sleep(interval)
	GPIO.output(port, False)
	time.sleep(interval)

