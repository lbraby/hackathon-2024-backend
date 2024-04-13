import requests
import json

HOST = "https://worldfood.guide"
# https://worldfood.guide/api/photos/
# - results
#   - name
#   - location

def main():
    with open("dishes.json", "r+", encoding="utf-8") as dishes_file:
        dishes = json.load(dishes_file)
        next_page = f"{HOST}/api/photos/"
        while next_page:
            response = requests.get(next_page).json()
            results = response["results"]
            for dish in results:
                if dish["dish_name"] in dishes:
                    dishes[dish["dish_name"]]["image_url"] = dish["location"]

            next_page = response["next"]

    with open("dishes.json", "r+", encoding="utf-8") as dishes_file:
        json.dump(dishes, dishes_file, indent=4)

if __name__ == "__main__":
    main()