#!/usr/bin/env python

import serial
import RPi.GPIO as GPIO
import time

ser = serial.Serial("/dev/ttyACM0", 9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate = 9600
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

def blink(pin):
    GPIO.output(pin, GPIO.HIGH)  
    time.sleep(1)  
    GPIO.output(pin, GPIO.LOW)  
    time.sleep(1)  
    return



for idx in xrange(10):
    read_ser = ser.readline().strip()
    print("ser " + read_ser)
    if (read_ser == "Hello From Arduino!"):
        blink(11)
        # print("Hello From Arduino!")
    else:
        print("bad")


GPIO.cleanup()

