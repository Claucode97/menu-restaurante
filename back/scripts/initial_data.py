import sys
import json
from unicodedata import name

sys.path.insert(0, "")
from src.domain.Menu import MenuRepository, Menu
from src.example_menu import dict_menu, dict_menu_2, dict_menu_3
from src.domain.Restaurant import RestaurantRepository, Restaurant


database_path = "data/database.db"
restaurant_reposotory = RestaurantRepository(database_path)
menu_repository = MenuRepository(database_path)


menu_repository.save(
    Menu(id="MM", date="2022-01-03", desc=dict_menu, id_restaurant="01")
)


menu_repository.save(
    Menu(id="MT", date="2022-02-03", desc=dict_menu_2, id_restaurant="02")
)

restaurant_reposotory.save_restaurants(Restaurant(id_restaurant="01", name="Josu"))
restaurant_reposotory.save_restaurants(Restaurant(id_restaurant="02", name="Joseba"))
