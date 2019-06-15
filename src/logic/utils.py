#!/usr/bin/env python
# -*- coding: utf-8 -*-

# translate value from one range to another range
def translate(value, fromMin, fromMax, toMin, toMax):
    fromRange = fromMax - fromMin
    toRange = toMax - toMin
    valueScaled = float(value - fromMin) / float(fromRange)
    return toMin + (valueScaled * toRange)

# translate potentiomenter
def translatePot(value):
    return translate(value, 0, 1023, -1, 1)