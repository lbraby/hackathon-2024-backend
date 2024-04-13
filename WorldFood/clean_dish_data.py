import requests
import json

def main():
    with open("dishes.json", "r", encoding="utf-8") as dishes_file:
        dishes = json.load(dishes_file)
        dishes_to_remove = []

        for dish in dishes:
            if "image_url" not in dishes[dish] or dishes[dish]["image_url"] == "" or "cuisine_type" not in dishes[dish] or dishes[dish]["cuisine_type"] == "":
                dishes_to_remove.append(dish)

        for dish in dishes_to_remove:
            dishes.pop(dish)

    with open("dishes.json", "w", encoding="utf-8") as dishes_file:
        json.dump(dishes, dishes_file, indent=4)

if __name__ == "__main__":
    main()