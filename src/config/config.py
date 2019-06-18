#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getConf():
    return {
        # debug flag
        "debug": False,
        # server config
        "host": "0.0.0.0",
        "port": 9090,
        "templatesDir": ["server", "templates"],
        "staticDir": ["server", "static"],
        # serial
        "serial_devices": "/dev/ttyACM",
        # recipe dir
        "recipesDir": ["..", "recipes", "cake.txt"],
    }