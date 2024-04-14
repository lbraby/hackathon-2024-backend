import requests
import json

def main():
    with open("ingredients.json", "r", encoding="utf-8") as ingredients_file:
        ingredients = json.load(ingredients_file)
        ingredients_to_remove = []

        for ingredient in ingredients:
            if any(char.isdigit() for char in ingredient):
                ingredients_to_remove.append(ingredient)

        for ingredient in ingredients_to_remove:
            ingredients.remove(ingredient)

    with open("ingredients.json", "w", encoding="utf-8") as ingredients_file:
        json.dump(ingredients, ingredients_file, indent=4)

if __name__ == "__main__":
    main()