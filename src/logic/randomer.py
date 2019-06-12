#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import uniform


def randomise(value):
    rand = uniform(-1, 1)
    if value:
        return value + value * rand
    else:
        return rand


def randomise_ingredient(ingredient):
    randomised = dict(ingredient)
    randomised["quantity"] = randomise(randomised["quantity"])
    return randomised


def randomise_ingredients(ingredients):
    randomise_ingredients = [
        randomise_ingredient(ingredient) for ingredient in ingredients
    ]
    return randomise_ingredients
