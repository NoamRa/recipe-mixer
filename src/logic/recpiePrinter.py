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


def print_recipe(recipe):
    # convert recipe to text
    recipe_text = "name \n ingredients \n instructions"

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
