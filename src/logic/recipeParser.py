#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logic import ingredientList

"""
ingredient shape
{
  quantity: float,
  measure: string,
  name: string,
  liquidOrSolid: string
}

parsed_recipe shape
{
  ingredients: ingredient[],
  instructions: string[]
}

"""


def clean_recipe(recipe):
    "break recipe text to list of lines, remove extra spaces and empty lines"
    splited_recipe = recipe.splitlines()
    cleaned = list(map(lambda x: x.strip(), splited_recipe))
    cleaned = list(filter(lambda x: x != "", cleaned))
    return cleaned


def parse_ingredient(raw_ingrediant, ingredients_data):
    splitted = raw_ingrediant.split()
    quantity = float(splitted[0])
    measure = splitted[1]
    name = " ".join(splitted[2:])

    properties = []
    for ing in ingredients_data:
        if ing["name"] == name:
            properties = ing["properties"]
    if len(properties) == 0:  # validate
        print("failed to find properties for {}".format(name))

    ingredient = {
        "name": name,
        "quantity": quantity,
        "measure": measure,
        "properties": properties,
    }

    return ingredient


def parse_ingredients(raw_ingredients):
    ingredients_data = ingredientList.ingredient_list()
    ingredients = list(
        map(lambda ingred: parse_ingredient(ingred, ingredients_data), raw_ingredients)
    )
    return ingredients


def parse_instructions(raw_instructions):
    return raw_instructions


def parse_recipe(recipe):
    cleaned_recipe = clean_recipe(recipe)
    ingredients_idx = cleaned_recipe.index("ingredients")
    instructions_idx = cleaned_recipe.index("instructions")
    ingredients_lines = cleaned_recipe[ingredients_idx + 1 : instructions_idx]
    instructions_lines = cleaned_recipe[instructions_idx + 1 :]

    parsed_recipe = {
        "ingredients": parse_ingredients(ingredients_lines),
        "instructions": parse_instructions(instructions_lines),
    }

    return parsed_recipe

