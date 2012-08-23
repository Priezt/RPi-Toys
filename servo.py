#!/usr/bin/env python

import serial
import sys
import time

test = serial.Serial('/dev/ttyUSB0', baudrate=38400, bytesize=8, parity='N', stopbits=1)

def send_cmd(cmd):
	test.open()
	test.write(cmd)
	test.close()

def read_msg():
	test.open()
	while True:
		print test.readline()
	test.close()

# cmd like 'D1000 #00A180#01A180T50!'
send_cmd(sys.argv[1])

