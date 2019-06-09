#!/usr/bin/env python
# -*- coding: utf-8 -*-

# site packages
import datetime
import json
import os
import logging

# external packages
from flask import Flask, render_template

# local imports
from logic import recipeParser, textureModifier, recipeFormatter


config = {
    "recipesDir": ["..", "recipes", "cake.txt"],
    "templatesDir": ["server", "templates"],
    "do_random": False,
}
do_random = config["do_random"]

script_dir = os.path.dirname(__file__)
template_folder = os.path.join(script_dir, *config.get("templatesDir"))
app = Flask(__name__, template_folder=template_folder)


def mix_recipe():
    with open(os.path.join(script_dir, *config.get("recipesDir")), "r") as reader:
        recipe = reader.read()
    parsed_recepie = recipeParser.parse_recipe(recipe)
    # print(json.dumps(parsed_recepie, indent=2))

    mixed_recipe = dict(parsed_recepie)
    if do_random:
        print("doing random!")
    else:
        print("not doing random")
        transformed = textureModifier.texture_modifier(
            parsed_recepie["ingredients"], 0.5
        )
        # print(json.dumps(transformed, indent=2))
        mixed_recipe["ingredients"] = transformed

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
    app.run(host="0.0.0.0", port=8080, debug=True)

