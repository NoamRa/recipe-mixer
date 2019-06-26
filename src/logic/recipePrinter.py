#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cups
import os
import tempfile
from datetime import datetime
from config import config

config = config.getConf()


def gen_file_path():
    temp_dir = tempfile.gettempdir()
    now_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = "mixed-{}.txt".format(now_str)
    recipe_path = os.path.join(temp_dir, file_name)
    return recipe_path


def format_line(item):
    return "* {}\n".format(item)


def create_recipe_text(mixed_recipe):
    name = mixed_recipe.get("name")
    ingredients_lines = mixed_recipe.get("ingredients")
    instructions_lines = mixed_recipe.get("instructions")

    header = "\nYour mixed {} recipe:\n".format(name)
    ingredients = "\nIngredients:\n" + "".join(
        [format_line(l) for l in ingredients_lines]
    )
    instructions = "\nInstructions:\n" + "".join(
        [format_line(l) for l in instructions_lines]
    )
    footer = "\n\n\n"

    recipe_text = header + ingredients + instructions + footer

    return recipe_text


def print_recipe(mixed_recipe):
    print(mixed_recipe)
    if not mixed_recipe: return

    # convert recipe to text
    recipe_text = create_recipe_text(mixed_recipe)

    # write text to file
    recipe_path = gen_file_path()
    recipe_file = open(recipe_path, "w")
    recipe_file.write(recipe_text)
    recipe_file.close()

    # get printer
    conn = cups.Connection()

    # print file
    printer_name = config.get("printer_name")
    printer_opts = config.get("printer_opts")
    conn.printFile(printer_name, recipe_path, "recipe", printer_opts)
