#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
from sys import exit

def scan(device, up_to):
    avaliable = []
    for i in range(up_to):
        try:
            ser = serial.Serial("{}{}".format(device, i))
            avaliable.append(ser.portstr)
            ser.close()
        except serial.SerialException:
            pass

    len_avaliable = len(avaliable)
    if len_avaliable == 1 :
        print("found one serial connection: {}".format(avaliable[0]))
        return avaliable[0]

    elif len_avaliable == 0:
        print("failed to find any serial connections with {}".format(device))
        exit(1)

    elif len_avaliable > 1:
        print("found sevral avaliable serial devices:")
        for s in avaliable:
            print(s)
        print("using the first")
        return avaliable[0]

scan("/dev/ttyACM", 3)
