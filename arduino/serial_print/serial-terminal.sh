#!/bin/bash

stty -F /dev/ttyACM0 cs8 9600 ignbrk -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echok -echoctl -echoke noflsh -ixon -crtscts

screen /dev/ttyACM0 9600

kill `screen -ls | grep Detach | sed 's/\..*//'`

