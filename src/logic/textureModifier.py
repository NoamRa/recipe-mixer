#!/usr/bin/env python
# -*- coding: utf-8 -*-


def modify_texture(ingredient, amount):
    transformed = dict(ingredient)
    # print(transformed)
    name = transformed.get("name")
    props = transformed.get("properties")
    undividable = "undividable" in props
    is_liquid = "liquid" in props
    orig_quantity = transformed["quantity"]
    if is_liquid:
        new_quantity = orig_quantity + orig_quantity * amount
        print(
            "{} is liquid. updating from {} to {}".format(
                name, orig_quantity, new_quantity
            )
        )
        transformed["quantity"] = new_quantity
    else:
        new_quantity = orig_quantity + orig_quantity * -amount
        print(
            "{} isn't liquid. updating from {} to {}".format(
                name, orig_quantity, new_quantity
            )
        )
        transformed["quantity"] = new_quantity

    if undividable:
        rounded = float(round(transformed["quantity"]))
        print(
            "{} is undividable. rounding from {} to {}".format(
                name, transformed["quantity"], rounded
            )
        )
        transformed["quantity"] = rounded

    return transformed


def texture_modifier(ingredients, amount):
    """
    ingredients: ingredient[]
    amount: -1 ~ 1 
    values lower than 0 increase solids and decrease liquids
    values higher than 0 increase liquids and decreases solids
    """
    print("got amount {}".format(amount))
    modified_ingredients = [
        modify_texture(ingredient, amount) for ingredient in ingredients
    ]

    return modified_ingredients
