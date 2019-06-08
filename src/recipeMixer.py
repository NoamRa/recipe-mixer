#!/usr/bin/env python
# -*- coding: utf-8 -*-

# site packages
import json
import os

# external packages
# import flask

# local imports
from logic import recipeParser, textureModifier


config = {"recipeDir": ["..", "recipes", "cake.txt"], "do_random": False}
do_random = config["do_random"]


def main():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, *config.get("recipeDir")), "r") as reader:
        recipe = reader.read()
    parsed_recepie = recipeParser.parse_recipe(recipe)
    # print(json.dumps(parsed_recepie, indent=2))

    if do_random:
        print("doing random!")
    else:
        print("not doing random")
        transformed = textureModifier.texture_modifier(
            parsed_recepie["ingredients"], 0.5
        )
        # print(json.dumps(transformed, indent=2))


if __name__ == "__main__":
    main()

