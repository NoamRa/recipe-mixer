#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import gevent and patch
from gevent import monkey

monkey.patch_all()

# site packages
import datetime
import json
from os.path import abspath, join, dirname
import logging
from threading import Thread
import serial
from unittest.mock import Mock
from time import sleep

# external packages
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

# local imports
from logic import (
    recipeParser,
    textureModifier,
    recipeFormatter,
    colorAdder,
    randomer,
    utils,
    fileWrapper,
    recipePrinter,
)
from hardware import serialFinder
from config import config

config = config.getConf()

# region app, socketio and serial

script_dir = dirname(__file__)
all_recipes = fileWrapper.read_all_recipes(script_dir, config.get("recipesDir"))

template_folder = abspath(join(script_dir, *config.get("templatesDir")))
static_folder = abspath(join(script_dir, *config.get("staticDir")))

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.config["SECRET_KEY"] = "mixit!"

socketio = SocketIO(app, async_mode="gevent")

if config["mock_serial"]:
    print("SERIAL IS MOCKED!")
    ser = Mock()
    ser.readline = utils.mocked_readLine
else:
    serial_port = serialFinder.scan(config["serial_devices"], 3)
    ser = serial.Serial(
        serial_port, config["serial_baud"], timeout=config["serial_timeout"]
    )

serial_data_dict = {
    "random": False,
    "pot_value": 512,
    "color": None,
    "up": False,
    "down": False,
}

state = {
    "selected_recipe": all_recipes[0].get("name"),
    "mixed_recipe": None,
}


@socketio.on("idle for 5 seconds", namespace="/serial")
def handle_my_custom_event(json):
    print("Client was idle for 5 seconds. It's printing time!")
    recipePrinter.print_recipe(state["mixed_recipe"])


def handleUpOrDown():
    global state
    global serial_data_dict
    recipe_names = list(map(lambda recipe_obj: recipe_obj.get("name"), all_recipes))
    idx = recipe_names.index(state["selected_recipe"])
    length = len(recipe_names)

    # print("recipe_names: " + str(recipe_names), " length: " + str(length))
    # print("currently selected " + state["selected_recipe"] + " in idx " + str(idx))

    if serial_data_dict.get("up") and idx > 0:
        state["selected_recipe"] = recipe_names[idx - 1]
    elif serial_data_dict.get("down") and idx + 1 < length:
        state["selected_recipe"] = recipe_names[idx + 1]


def handle_serial(data):
    global serial_data_dict
    serial_data_dict = utils.serial_parser(data)
    global state
    state["mixed_recipe"] = mix_recipe()
    print("serial message: " + json.dumps(serial_data_dict))
    handleUpOrDown()
    socketio.emit("serial_message", serial_data_dict, namespace="/serial")


connected_to_serial = False


def read_serial(ser):
    global connected_to_serial
    while not connected_to_serial:
        connected_to_serial = True
        while True:
            sleep(config["serial_timeout"]) if not config["mock_serial"] else sleep(10)
            data = ser.readline()
            if data:
                data = data.decode("ascii").strip()
            if len(data) > 0:
                handle_serial(data)

        print("closing serial")
        ser.close()


read_serial_thread = Thread(target=read_serial, args=(ser,), name="serial_thread")
print("starting serial thread")
read_serial_thread.start()

# endregion


def mix_recipe():
    selected_recipe_obj = [
        recipe_obj
        for recipe_obj in all_recipes
        if recipe_obj["name"] == state.get("selected_recipe")
    ]
    parsed_recipe = selected_recipe_obj[0].get("recipe")
    # print(json.dumps(parsed_recipe, indent=2))

    mixed_recipe = dict(parsed_recipe)
    do_random = serial_data_dict.get("random")
    if do_random:
        # print("doing random!")
        mixed_recipe["ingredients"] = randomer.randomise_ingredients(
            parsed_recipe["ingredients"]
        )
    else:
        # print("not doing random")
        texture_value = serial_data_dict.get("pot_value")
        mixed_recipe["ingredients"] = textureModifier.texture_modifier(
            parsed_recipe["ingredients"], utils.translatePot(float(texture_value))
        )
        food_coloring = serial_data_dict.get("color")
        if food_coloring:
            mixed_recipe = colorAdder.add_color(mixed_recipe, food_coloring)

    formatted_recipe = recipeFormatter.format_recipe(mixed_recipe)
    return formatted_recipe


# region routes


@app.route("/recipe")
def recipe():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    global state
    mixed_recipe = state["mixed_recipe"]
    templateData = {
        "time": timeString,
        "name": mixed_recipe["name"],
        "ingredients": mixed_recipe["ingredients"],
        "instructions": mixed_recipe["instructions"],
    }
    return render_template("recipe.html", **templateData)


@app.route("/selection")
def selection():
    recipe_names = list(map(lambda recipe_obj: recipe_obj.get("name"), all_recipes))
    selected_recipe = state["selected_recipe"]
    templateData = {"recipe_names": recipe_names, "selected_recipe": selected_recipe}
    return render_template("selection.html", **templateData)


@app.route("/")
def index():
    return "go to /selection or /recipe"


# endregion routes

if __name__ == "__main__":
    print("Starting Recipe Mixer server...")
    socketio.run(app, host=config["host"], port=config["port"], debug=config["debug"])

