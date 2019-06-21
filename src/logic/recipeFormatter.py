#!/usr/bin/env python
# -*- coding: utf-8 -*-


from logic import utils

def format_ingredients(ingredient):
    quantity = utils.round_fraction(ingredient["quantity"])
    if not quantity: return
    
    formatted_ingredient = "{} {} {}".format(
        quantity, ingredient["measure"], ingredient["name"]
    )

    return formatted_ingredient


def format_recipe(recipe):
    formatted_recipe = dict(recipe)

    ingredients = [
        format_ingredients(ing) for ing in formatted_recipe["ingredients"]
    ]
    
    formatted_recipe["ingredients"] = list(filter(None, ingredients))
    
    return formatted_recipe
