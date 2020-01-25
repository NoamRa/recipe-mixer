#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import RPi.GPIO as GPIO
from board import *
import neopixel
from time import sleep


num_pixels = 1
PIN = D18
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    PIN, num_pixels, brightness=0.01, auto_write=False #, pixel_order=ORDER
)
pixels[0] = (255,255,255)
pixels.show()


sleep(2)



# import RPi.GPIO as GPIO

# P_LED = 18 # adapt to your wiring
# fPWM = 50  # Hz (not higher with software PWM)
# GPIO.setmode(GPIO.BOARD)
# def setup():
#     global pwm
#     GPIO.setup(P_LED, GPIO.OUT)
#     pwm = GPIO.PWM(P_LED, fPWM)
#     pwm.start(0)
    
# print("starting")
# setup()
# duty = 0
# isIncreasing = True
# while True:
#     pwm.ChangeDutyCycle(duty)
#     print("D =", duty, "%")
#     if isIncreasing:
#         duty += 10
#     else:
#         duty -= 10
#     if duty == 100:
#         isIncreasing = False
#     if duty == 0:
#         isIncreasing = True
#     sleep(1)
