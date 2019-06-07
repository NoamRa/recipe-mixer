import recipeParser
import json
import os

config = {"recipeDir": ["..", "recipes", "brownies.txt"]}


def main():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, *config.get("recipeDir")), "r") as reader:
        recipe = reader.read()
    parsed_recepie = recipeParser.parse_recipe(recipe)
    print(json.dumps(parsed_recepie, indent=2))


if __name__ == "__main__":
    main()

