import requests
import json
import math
from bs4 import BeautifulSoup

def main():
    with open("cuisines.json", "r", encoding="utf-8") as cuisines_file, open("dishes.json", "r+", encoding="utf-8") as dishes_file:
        cuisines = json.load(cuisines_file)
        dishes = json.load(dishes_file)

        for cuisine in cuisines:
            cuisine_type = cuisine["name"].strip("-")
            num_pages = math.ceil(cuisine["dishes_count"] / 20)
            if num_pages == 0:
                continue

            url = cuisine["uri"]
            url = url.split("/")
            url[-3] = "cuisinedishes"
            url = "/".join(url)

            for page_num in range(1, num_pages+1):
                response = requests.get(f"{url}{page_num}")

                soup = BeautifulSoup(response.content, "html.parser")

                elements = soup.find_all(class_="title3 color2")
                for element in elements:
                    link_text = element.find("a").text

                    if link_text in dishes:
                        dishes[link_text]["cuisine_type"] = cuisine_type

    with open("dishes.json", "w", encoding="utf-8") as dishes_file:
        json.dump(dishes, dishes_file, indent=4)

if __name__ == "__main__":
    main()