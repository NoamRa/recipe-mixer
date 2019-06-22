#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getConf():
    return {
        # debug flags
        "debug": False,
        "mock_serial": False,
        # server config
        "host": "0.0.0.0",
        "port": 9090,
        "templatesDir": ["server", "templates"],
        "staticDir": ["server", "static"],
        # serial
        "serial_devices": "/dev/ttyACM",
        "serial_baud": 9600,
        "serial_timeout": 0.01,
        # recipe dir
<<<<<<< HEAD
        "recipesDir": ["..", "recipes", "cake.txt"],
    }
=======
        "recipesDir": ["..", "recipes"],
    }
>>>>>>> f5581705a373b27952c08473936d1170b09b0e95
