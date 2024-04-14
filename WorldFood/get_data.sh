echo "getting cuisines..."
python get_cuisines.py
echo "getting dishes..."
python get_dishes.py
echo "getting dish images..."
python get_dish_images.py
echo "scraping for dish territory of origins..."
python scrape_territory.py
echo "getting ingredients..."
python get_ingredients.py
echo "cleaning dish data..."
python clean_dish_data.py
echo "cleaning ingredient data..."
python clean_ingredient_data.py
