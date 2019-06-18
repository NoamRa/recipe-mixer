#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import gevent and patch
from gevent import monkey

monkey.patch_all()

# site packages
import datetime
import json
import os
import logging
from threading import Thread
import serial

# external packages
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

# local imports
from logic import recipeParser, textureModifier, recipeFormatter, randomer, utils
from hardware import serialFinder
from config import config

config = config.getConf()

do_random = False  # TODO remove when there's random from serial

# region app, socketio and serial

script_dir = os.path.dirname(__file__)
template_folder = os.path.abspath(os.path.join(script_dir, *config.get("templatesDir")))
static_folder = os.path.abspath(os.path.join(script_dir, *config.get("staticDir")))

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.config["SECRET_KEY"] = "mixit!"

socketio = SocketIO(app, async_mode="gevent")

serial_port = serialFinder.scan(config["serial_devices"], 5)
serial_conf = serial.Serial(serial_port, 9600, timeout=0.1)

serial_data_dict = { "serial_message": "512" }

@socketio.on("my event", namespace="/serial")
def handle_my_custom_event(json):
    print("received json: " + str(json))


def handle_serial(data):
    print("serial message: " + data)
    payload = {"serial_message": str(data)}
    global serial_data_dict
    serial_data_dict = payload
    socketio.emit("serial_message", payload, namespace="/serial")


connected_to_serial = False

def read_serial(ser):
    global connected_to_serial
    while not connected_to_serial:
        connected_to_serial = True
        while True:
            data = ser.readline()
            if data:
                data = data.decode().strip()
            if len(data) > 0:
                handle_serial(data)

        print("closing serial")
        ser.close()


read_serial_thread = Thread(
    target=read_serial, args=(serial_conf,), name="serial_thread"
)
print("starting serial thread")
read_serial_thread.start()

# endregion


def mix_recipe():
    with open(os.path.join(script_dir, *config.get("recipesDir")), "r") as reader:
        recipe = reader.read()
    parsed_recepie = recipeParser.parse_recipe(recipe)
    # print(json.dumps(parsed_recepie, indent=2))

    mixed_recipe = dict(parsed_recepie)
    if do_random:
        # print("doing random!")
        mixed_recipe["ingredients"] = randomer.randomise_ingredients(
            parsed_recepie["ingredients"]
        )
    else:
        # print("not doing random")
        texture_value = serial_data_dict.get("serial_message")
        mixed_recipe["ingredients"] = textureModifier.texture_modifier(
            parsed_recepie["ingredients"], utils.translatePot(float(texture_value))
        )

    formatted_recipe = recipeFormatter.format_recipe(mixed_recipe)

    return formatted_recipe


# region routes


@app.route("/")
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    mixed_recipe = mix_recipe()
    templateData = {
        "time": timeString,
        "name": mixed_recipe["name"],
        "ingredients": mixed_recipe["ingredients"],
        "instructions": mixed_recipe["instructions"],
    }
    return render_template("index.html", **templateData)


# endregion routes

if __name__ == "__main__":
    print("Starting Recipe Mixer server...")
    socketio.run(app, host=config["host"], port=config["port"], debug=config["debug"])

