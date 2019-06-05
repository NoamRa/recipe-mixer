import recipeParser
import json
import os

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "..", "recipes", "brownies.txt"), "r") as reader:
        recipe = reader.read()
    parsed_recepie = recipeParser.parse_recipe(recipe)
    print(json.dumps(parsed_recepie, indent=2))
