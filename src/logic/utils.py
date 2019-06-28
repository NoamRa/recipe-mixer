#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint, getrandbits, choice
import re

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


def mocked_readLine():
    mocked_serial = ""

    if True: # mock up and down toggle
        message = choice(["up", "down"])
        mocked_serial = "|{}||".format(message)

    else:
        switch = randint(0, 2)
        if switch == 0:
            mocked_serial = "|random||"
        elif switch == 1:
            pot_value = randint(0, 1023)
            mocked_serial = "|{}||".format(pot_value)
        elif switch == 2:
            pot_value = randint(0, 1023)
            color = choice(["y", "b", "g"])
            mocked_serial = "|{}|{}||".format(pot_value, color)

    return mocked_serial.encode("ascii")


def serial_parser(serial_string):
    delimiter = "|"
    # print("serial string - " + serial_string)
    serial_data_dict = {
        "random": False, 
        "pot_value": 512, 
        "color": None, 
        "up": False, 
        "down": False,
    }
    if serial_string[0] != delimiter or serial_string[-2:] != delimiter + delimiter:
        return serial_data_dict

    splitted = serial_string[1:-2].split(delimiter)

    if "up" in splitted:
        serial_data_dict["up"] = True
        return serial_data_dict

    elif "down" in splitted:
        serial_data_dict["down"] = True
        return serial_data_dict

    if "random" in splitted:
        serial_data_dict["random"] = True

    if splitted[0].isdigit():
        serial_data_dict["pot_value"] = int(splitted[0])

    if len(splitted) == 2:
        serial_data_dict["color"] = splitted[1]

    return serial_data_dict
