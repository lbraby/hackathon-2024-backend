import requests
import json

def main():
    with open("dishes.json", "r", encoding="utf-8") as dishes_file:
        dishes = json.load(dishes_file)
        ingredients = set()

        for dish in dishes:
            dish_ingredients = dishes[dish]["ingredients"]
            if dish_ingredients == "":
                continue
            dish_ingredients = dish_ingredients.replace(" or ", ", ").replace(".", "").replace(" and ", ", ")
            
            ingredients.update(dish_ingredients.split(", "))

        ingredients.remove("")

    with open("ingredients.json", "w", encoding="utf-8") as ingredients_file:
        json.dump(list(ingredients), ingredients_file, indent=4)

if __name__ == "__main__":
    main()