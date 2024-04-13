import requests
import json

HOST = "https://worldfood.guide"
# https://worldfood.guide/api/cuisines/
# - results
#   - name
#   - description
#   - uri
#   - dishes_count
#     - looks like there are 20 dishes per page

def main():
    with open("cuisines.json", "w", encoding="utf-8") as cuisines_file: # name, description, uri, dishes_count
        cuisines = []
        next_page = f"{HOST}/api/cuisines/"
        while next_page:
            response = requests.get(next_page).json()
            results = response["results"]
            for cuisine in results:
                cuisines.append({"name": cuisine["name"], "description": cuisine["description"], "uri": cuisine["uri"], "dishes_count": cuisine["dishes_count"]})

            next_page = response["next"]

        json.dump(cuisines, cuisines_file, indent=4)

if __name__ == "__main__":
    main()