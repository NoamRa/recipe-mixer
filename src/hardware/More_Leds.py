 #!/usr/bin/env python

import serial
import RPi.GPIO as GPIO
import time

ser = serial.Serial("/dev/ttyACM0", 9600) 

# ser.write('3')
# time.sleep(0.5)
# ser.write('5')
# time.sleep(0.5)
# ser.write('6')
