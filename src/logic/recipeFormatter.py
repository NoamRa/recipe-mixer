#!/usr/bin/env python
# -*- coding: utf-8 -*-


def format_ingredients(ingredient):
    formatted_ingredient = "{} {} {}".format(
        ingredient["quantity"], ingredient["measure"], ingredient["name"]
    )

    return formatted_ingredient


def format_recipe(recipe):
    formatted_recipe = dict(recipe)

    formatted_recipe["ingredients"] = [
        format_ingredients(ing) for ing in formatted_recipe["ingredients"]
    ]

    return formatted_recipe
