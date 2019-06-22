#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join

from logic import recipeParser

def list_recipe_files(script_dir, recipes_dir):
    path_to_recipes_dir = join(script_dir, *recipes_dir)
    recipes_files = [
        f for f in listdir(path_to_recipes_dir) if isfile(join(path_to_recipes_dir, f))
    ]
    print("found recipes:")
    for recipe in recipes_files:
        print(recipe)
    return recipes_files


def resolve_recipe_full_path(script_dir, recipes_dir, recipes_file_name):
    return join(script_dir, *recipes_dir, recipes_file_name)


def read_recipe_content(file_path):
    recipe = ""
    with open(file_path, "r") as reader:
        recipe = reader.read()
    return recipe


def read_all_recipes(script_dir, recipes_dir):
    """
    {
       name: recipe name string
       path: string
       recipe: parsed recipe
    }
    """

    out = []
    recipes_files = list_recipe_files(script_dir, recipes_dir)
    for recipe in recipes_files:
        file_path = resolve_recipe_full_path(script_dir, recipes_dir, recipe)
        file_content = read_recipe_content(file_path)
        recipe = recipeParser.parse_recipe(file_content)
        name = recipe.get("name")

        recipe_obj = {"name": name, "path": file_path, "recipe": recipe}
        out.append(recipe_obj)

    return out
