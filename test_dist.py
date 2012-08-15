#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import time

TRIGGER_PORT = 0
ECHO_PORT = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PORT, GPIO.OUT)
GPIO.setup(ECHO_PORT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

E_PULSE = 0.00005
CHECK_INTERVAL = 0.00005
CHECK_TIMES = 1000

echo_cache = []

GPIO.output(TRIGGER_PORT, False)
time.sleep(0.1)
GPIO.output(TRIGGER_PORT, True)
time.sleep(E_PULSE)
GPIO.output(TRIGGER_PORT, False)

#for i in range(CHECK_TIMES):
#	echo_cache.append(GPIO.input(ECHO_PORT))
#
#
#high_count = 0
#
#for i in echo_cache:
#	if i:
#		high_count += 1
#		sys.stdout.write('1')
#	else:
#		sys.stdout.write('0')
#
#print
#
#distance = (high_count * CHECK_INTERVAL) * 340 / 2

start_time = 0
end_time = 0

for i in range(CHECK_TIMES):
	if GPIO.input(ECHO_PORT):
		start_time = time.time()
		break
	time.sleep(CHECK_INTERVAL)

for i in range(CHECK_TIMES):
	if not GPIO.input(ECHO_PORT):
		end_time = time.time()
		break
	time.sleep(CHECK_INTERVAL)

distance = (end_time - start_time) * 340 / 2

print "Start time: %0.6f" % start_time
print "End time: %0.6f" % end_time
print "Distance: %0.4f" % distance
