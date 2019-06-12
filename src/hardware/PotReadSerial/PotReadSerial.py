#!/usr/bin/env python

import serial
import RPi.GPIO as GPIO
import time

ser = serial.Serial("/dev/ttyACM1", 9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate = 9600
GPIO.setmode(GPIO.BOARD)

# ReadPotValue = DeviceReadBuffer[serial]
    # read_ser = ser.readline().strip()
    # print("ser " + read_ser)

print("starting")

# for idx in xrange(10):
while True:
	read_ser = ser.readline().strip()
	print("ser " + read_ser)
	time.sleep(0.01)

# GPIO.cleanup()