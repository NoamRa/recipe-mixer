#!/usr/bin/env python
# -*- coding: utf-8 -*-

# site packages
import datetime
import json
import os
import logging

# external packages
from flask import Flask, render_template
from flask_serial import Serial

# local imports
from logic import recipeParser, textureModifier, recipeFormatter, randomer


config = {
    "recipesDir": ["..", "recipes", "cake.txt"],
    "templatesDir": ["server", "templates"],
    "do_random": True,
}
do_random = config["do_random"]

script_dir = os.path.dirname(__file__)
template_folder = os.path.join(script_dir, *config.get("templatesDir"))
app = Flask(__name__, template_folder=template_folder)
app.config["SERIAL_TIMEOUT"] = 0.1
app.config["SERIAL_PORT"] = "COM2"
app.config["SERIAL_BAUDRATE"] = 9600
app.config["SERIAL_BYTESIZE"] = 8
app.config["SERIAL_PARITY"] = "N"
app.config["SERIAL_STOPBITS"] = 1

ser = Serial(app)

@ser.on_message()
def handle_message(msg):
    print("receive a message:", msg)
    # send a msg of str
    ser.on_send("send a str message!!!")
    # send a msg of bytes
    ser.on_send(b"send a bytes message!!!")


@ser.on_log()
def handle_logging(level, info):
    print(level, info)


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
        mixed_recipe["ingredients"] = textureModifier.texture_modifier(
            parsed_recepie["ingredients"], 0.5
        )

    formatted_recipe = recipeFormatter.format_recipe(mixed_recipe)

    return formatted_recipe


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

