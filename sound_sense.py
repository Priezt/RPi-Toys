#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import time

SENSE_PORT = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSE_PORT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

CHECK_INTERVAL = 0.00005

while True:
	if GPIO.input(SENSE_PORT):
		#sys.stdout.write("1")
		sys.stdout.flush()
	else:
		sys.stdout.write("0")
		sys.stdout.flush()
	time.sleep(CHECK_INTERVAL)

