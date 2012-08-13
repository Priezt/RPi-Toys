#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import time

LCD_RS = 7
LCD_E = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18

LCD_WIDTH = 20
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x00
LCD_LINE_2 = 0x80
LCD_LINE_3 = 0x40
LCD_LINE_4 = 0xc0

E_PULSE = 0.00005
E_DELAY = 0.00005

def main():
	if len(sys.argv) < 2:
		print "lcd.py <clear|print>"
	elif sys.argv[1] == "clear":
		gpio_init()
		lcd_init()
	elif sys.argv[1] == "print":
		gpio_init()
		lcd_print(sys.argv[2])

def gpio_init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LCD_E, GPIO.OUT)
	GPIO.setup(LCD_RS, GPIO.OUT)
	GPIO.setup(LCD_D4, GPIO.OUT)
	GPIO.setup(LCD_D5, GPIO.OUT)
	GPIO.setup(LCD_D6, GPIO.OUT)
	GPIO.setup(LCD_D7, GPIO.OUT)

def lcd_init():
	lcd_byte(0x33, LCD_CMD) # don't know its meaning, but mendatory
	lcd_byte(0x32, LCD_CMD) # don't know its meaning, but mendatory
	lcd_byte(0x28, LCD_CMD) # function set, 4-bit, 2-line, 5x8 dots
	lcd_byte(0x0c, LCD_CMD) # display on, cursor off, blink off
	lcd_byte(0x06, LCD_CMD) # cursor increase, no shift
	lcd_byte(0x01, LCD_CMD) # clear screen
	lcd_byte(0x02, LCD_CMD) # go home

def toggle_enable():
	time.sleep(E_DELAY)
	GPIO.output(LCD_E, True)
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, False)
	time.sleep(E_DELAY)

def lcd_print(message):
	message = message.ljust(LCD_WIDTH, " ")
	for i in range(LCD_WIDTH):
		lcd_byte(ord(message[i]), LCD_CHR)

def lcd_byte(bits, mode):
	GPIO.output(LCD_RS, mode)
	# high bits
	GPIO.output(LCD_D4, False)
	GPIO.output(LCD_D5, False)
	GPIO.output(LCD_D6, False)
	GPIO.output(LCD_D7, False)
	if bits & 0x10 == 0x10:
		GPIO.output(LCD_D4, True)
	if bits & 0x20 == 0x20:
		GPIO.output(LCD_D5, True)
	if bits & 0x40 == 0x40:
		GPIO.output(LCD_D6, True)
	if bits & 0x80 == 0x80:
		GPIO.output(LCD_D7, True)
	toggle_enable()
	# low bits
	GPIO.output(LCD_D4, False)
	GPIO.output(LCD_D5, False)
	GPIO.output(LCD_D6, False)
	GPIO.output(LCD_D7, False)
	if bits & 0x01 == 0x01:
		GPIO.output(LCD_D4, True)
	if bits & 0x02 == 0x02:
		GPIO.output(LCD_D5, True)
	if bits & 0x04 == 0x04:
		GPIO.output(LCD_D6, True)
	if bits & 0x08 == 0x08:
		GPIO.output(LCD_D7, True)
	toggle_enable()

if __name__ == '__main__':
	main()
