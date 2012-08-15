#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import time

if len(sys.argv) < 3:
	raise Exception('switch.py <GPIO num> <delay>')

port = int(sys.argv[1])
delay = float(sys.argv[2])

GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.OUT)

GPIO.output(port, True)
time.sleep(delay)
GPIO.output(port, False)

