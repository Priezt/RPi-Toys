#!/bin/bash

./lcd.py clear
./lcd.py print "clockwise"
./motor.py 1 5 3000
./lcd.py print "counter clockwise"
./motor.py 0 5 3000
