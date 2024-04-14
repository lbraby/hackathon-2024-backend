# hackathon-2024-backend
## Setup Instructions
- create and activate venv using requirements.txt
- run get_data.sh in ~/WorldFood/ to load data into json files
- run setup_databases.py to load data into sqlite database
## REST API
### GET Methods
- GET /ingredients/search/`search`/`count` : get `count` entries of ingredients whose names are similar to `search`
  - use underscores in lieu of spaces for `search`
  - returns list of dictionaries with keys `id` and `name`
- GET /dishes/search/`search`/`count` : get `count` entries of dishes whose names are similar to `search`
  - use underscores in lieu of spaces for `search`
  - return list of dictionaries with keys `id`, `name`, `description`, `uri`, `image_url`, and `cuisine_type`
- GET /dishes/cuisine_type/`cuisine_type` : get all dishes with entered `cuisine_type` (e.g. Lebanese)
  - returns list of dictionaries with keys `id`, `name`, `description`, `ingredients`, `uri`, `image_url`, and `cuisine_type`
    - `ingredients` maps to dictionary with keys `id` and `ingredient`
- GET /dishes/your_menu : get dishes for weekly menu
  - returns list of dictionaries with keys `id`, `name`, `description`, `ingredients`, `uri`, `image_url`, and `cuisine_type`
    - `ingredients` maps to dictionary with keys `id` and `ingredient`
- GET /ingredients/liked/`username` : get all ingredients a user likes (includes those from dishes they like)
  - returns list of dictionaries with keys `id` and `name`
### POST Methods
- POST /dishes/like/`username`/`dish_id` : add ingredients from specified dish to `username`'s liked ingredients
- POST /ingredients/like/`username`/`dish_id` : add ingredients to `username`'s liked ingredients