#!/usr/bin/env python
# -*- coding: utf-8 -*-

# translate value from one range to another range
def translate(value, fromMin, fromMax, toMin, toMax):
    fromRange = fromMax - fromMin
    toRange = toMax - toMin
    valueScaled = float(value - fromMin) / float(fromRange)
    translated = toMin + (valueScaled * toRange)
    print("translated value {} to {}".format(str(value), str(translated)))
    return translated
    

# translate potentiomenter
def translatePot(value):
    return translate(value, 0, 1023, -1, 1)
    

def round_fraction(number):
    """
    rounds the number and to the closest 0, 0.25, 0.5, 0.75, 1, 1.25, etc'
    number: float
    return integer if there's no decimal value else float
    """
    PARTS = 4
    x = number * PARTS
    x = round(x)
    x = x / PARTS
    out = int(x) if x.is_integer() else x
    return out
