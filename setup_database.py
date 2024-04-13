import sqlite3
import json

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('food_data.db')

cur = conn.cursor()

# create ingredients table
cur.execute("DROP TABLE IF EXISTS ingredients")
cur.execute("create table ingredients (id INTEGER PRIMARY KEY, name TEXT)")

# insert ingredients
with open("WorldFood/ingredients.json", "r", encoding="utf-8") as ingredients_file:
    ingredients = json.load(ingredients_file)
    for ingredient in ingredients:
        cur.execute(f"insert into ingredients (name) values (?)", (ingredient,))

# create dishes table
cur.execute("DROP TABLE IF EXISTS dishes")
cur.execute("create table dishes (id INTEGER PRIMARY KEY, name TEXT, description TEXT, uri TEXT, image_url TEXT, cuisine_type TEXT)")

# insert dishes
with open("WorldFood/dishes.json", "r", encoding="utf-8") as dishes_file:
    dishes = json.load(dishes_file)
    for dish in dishes:
        dish_data = dishes[dish]
        cur.execute(f"insert into dishes (name, description, uri, image_url, cuisine_type) values (?, ?, ?, ?, ?)", (dish, dish_data["description"], dish_data["uri"], dish_data["image_url"], dish_data["cuisine_type"]))

# create dish_ingredients table
cur.execute("DROP TABLE IF EXISTS dish_ingredients")
cur.execute("create table dish_ingredients (id INTEGER PRIMARY KEY, dish_id INTEGER, ingredient_id INTEGER)")

# insert dish_ingredients data
with open("WorldFood/dishes.json", "r", encoding="utf-8") as dishes_file:
    dishes = json.load(dishes_file)
    for dish in dishes:
        cur.execute(f"select id from dishes where name = ?", (dish, ))
        dish_id = cur.fetchone()[0]

        dish_ingredients = dishes[dish]["ingredients"].replace(" or ", ", ").replace(".", "").replace(" and ", ", ").split(", ")
        for ingredient in dish_ingredients:
            if ingredient == "":
                continue

            cur.execute(f"select id from ingredients where name = ?", (ingredient, ))
            ingredient_id = cur.fetchone()[0]

            cur.execute(f"insert into dish_ingredients (dish_id, ingredient_id) values (?, ?)", (dish_id, ingredient_id))

cur.close()
conn.commit()
conn.close()
