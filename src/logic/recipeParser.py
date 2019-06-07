#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ingredient shape
{
  quantity: number,
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


def parse_ingredient():
    ingredient = {}
    return ingredient


def parse_ingredients(recipe):
    ingredients = []
    return ingredients


def parse_instructions(recipe):
    instructions = []
    return instructions


def parse_recipe(recipe):
    parsed_recipe = {
        "ingredients": parse_ingredients(recipe),
        "instructions": parse_instructions(recipe),
    }

    return parsed_recipe

