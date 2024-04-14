import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/ingredients/search/<search>/<int:count>", methods=["GET"])
def search_ingredients(search, count):
    search = search.replace("_", " ") # for spaces use underscores

    conn = sqlite3.connect('food_data.db')
    cur = conn.cursor()

    output = []

    cur.execute("select * from ingredients where name like ? limit ?", ("%" + search + "%", count))
    rows = cur.fetchall()
    for row in rows:
        output.append({"id": row[0], "name": row[1]})

    cur.close()
    conn.close()

    return jsonify(output)

@app.route("/dishes/search/<search>/<int:count>", methods=["GET"])
def search_dishes(search, count):
    search = search.replace("_", " ") # for spaces use underscores

    conn = sqlite3.connect('food_data.db')
    cur = conn.cursor()

    output = []

    cur.execute("select * from dishes where name like ? limit ?", ("%" + search + "%", count))
    rows = cur.fetchall()
    for row in rows:
        output.append({"id": row[0], "name": row[1], "description": row[2], "uri": row[3], "image_url": row[4], "cuisine_type": row[5]})

    cur.close()
    conn.close()

    return jsonify(output)

@app.route("/dishes/cuisine_type/<cuisine_type>", methods=["GET"])
def get_cuisine_dishes(cuisine_type):
    conn = sqlite3.connect('food_data.db')
    cur = conn.cursor()

    output = []

    cuisine_dishes = []
    cur.execute("select * from dishes where cuisine_type = ?", (cuisine_type, ))
    rows = cur.fetchall()
    for row in rows:
        cuisine_dishes.append(row)
    
    for dish in cuisine_dishes:
        ingredients = []

        cur.execute("select b.id, b.name from dish_ingredients a, ingredients b where a.ingredient_id = b.id and a.dish_id = ?", (dish[0], ))
        rows = cur.fetchall()
        for row in rows:
            ingredients.append({"id": row[0], "name": row[1]})

        output.append({"id": dish[0], "name": dish[1], "description": dish[2], "ingredients": ingredients, "uri": dish[3], "image_url": dish[4], "cuisine_type": dish[5]})

    cur.close()
    conn.close()

    return jsonify(output)

@app.route("/dishes/your_menu", methods=["GET"])
def get_menu():
    conn = sqlite3.connect('food_data.db')
    cur = conn.cursor()

    output = []

    your_menu = []
    cur.execute("select * from dishes where name = ? or name = ? or name = ?", ("Sfiha", "Mulukhiyah", "Shawarma"))
    rows = cur.fetchall()
    for row in rows:
        your_menu.append(row)
    
    for dish in your_menu:
        ingredients = []

        cur.execute("select b.id, b.name from dish_ingredients a, ingredients b where a.ingredient_id = b.id and a.dish_id = ?", (dish[0], ))
        rows = cur.fetchall()
        for row in rows:
            ingredients.append({"id": row[0], "name": row[1]})

        output.append({"id": dish[0], "name": dish[1], "description": dish[2], "ingredients": ingredients, "uri": dish[3], "image_url": dish[4], "cuisine_type": "Lebanese"})

    cur.close()
    conn.close()

    return jsonify(output)

@app.route("/dishes/like/<username>/<dish_id>", methods=["POST"])
def like_dish(username, dish_id):
    conn = sqlite3.connect('food_data.db')
    cur = conn.cursor()

    liked_ingredients = []
    cur.execute("select * from dish_ingredients where dish_id = ?", (dish_id, ))
    rows = cur.fetchall()
    for row in rows:
        liked_ingredients.append(row[2])

    for ingredient_id in liked_ingredients:
        cur.execute("insert into liked_ingredients (username, ingredient_id) values (?, ?)", (username, ingredient_id))

    cur.close()
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})

@app.route("/ingredients/like/<username>/<ingredient_id>", methods=["POST"])
def like_ingredient(username, ingredient_id):
    conn = sqlite3.connect('food_data.db')
    cur = conn.cursor()

    cur.execute("insert into liked_ingredients (username, ingredient_id) values (?, ?)", (username, ingredient_id))

    cur.close()
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})

@app.route("/ingredients/liked/<username>", methods=["GET"])
def get_liked_ingredients(username):
    conn = sqlite3.connect('food_data.db')
    cur = conn.cursor()

    output = []

    cur.execute("select b.id, b.name from liked_ingredients a, ingredients b where a.ingredient_id = b.id and a.username = ?", (username, ))
    rows = cur.fetchall()
    for row in rows:
        output.append({"id": row[0], "name": row[1]})


    cur.close()
    conn.close()

    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000) # host="0.0.0.0" makes Flask app accessible from external hosts