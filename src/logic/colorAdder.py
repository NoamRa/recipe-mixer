#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

AVAILABLE_COLORS = {
    "y": "yellow",
    "b": "blue",
    "g": "green",
}

# If the received color is one of the available colors,
# this function will return a recipe with color ingrediant
# and apropriate instructions. Otherwise, the unchanged recipe will be returned.
def add_color(recipe, color):
    colored_recipe = deepcopy(recipe)
    if color.lower() in AVAILABLE_COLORS:
        color_ingredient = {
            "name": "%s food coloring" % AVAILABLE_COLORS[color.lower()],
            "quantity": 3,
            "measure": "teaspoons",
            "properties": ["liquid"],
        }
        instructions = colored_recipe["instructions"]

        colored_recipe["ingredients"].append(color_ingredient)
        instructions.insert(len(instructions) - 1, "Add the food coloring.")
    return colored_recipe

