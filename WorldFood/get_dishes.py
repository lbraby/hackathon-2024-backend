import requests
import json

HOST = "https://worldfood.guide"
# https://worldfood.guide/api/dishes/
# - results
#   - name
#   - ingredients
#   - description
#   - uri

def main():
    with open("dishes.json", "w", encoding="utf-8") as dishes_file: # name, ingredients, description, uri
        dishes = {}
        next_page = f"{HOST}/api/dishes/"
        while next_page:
            response = requests.get(next_page).json()
            results = response["results"]
            for dish in results:
                dishes[dish["name"]] = {"ingredients": dish["ingredients"], "description": dish["description"], "uri": dish["uri"]}

            next_page = response["next"]

        json.dump(dishes, dishes_file, indent=4)

if __name__ == "__main__":
    main()