#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import time

BEEP_PORT = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(BEEP_PORT, GPIO.OUT)

time.sleep(0.1)
GPIO.output(BEEP_PORT, True)
time.sleep(0.1)
GPIO.output(BEEP_PORT, False)
