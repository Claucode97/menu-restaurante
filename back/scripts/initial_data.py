import sys
import json

sys.path.insert(0, "")
from src.domain.Menu import MenuRepository, Menu
from src.example_menu import dict_menu, dict_menu_2, dict_menu_3
from src.domain.Restaurant import RestaurantRepository, Restaurant


database_path = "data/database.db"

menu_repository = MenuRepository(database_path)

menu_repository.save(Menu(id="MM", date="2022-01-03", desc=dict_menu))

menu_repository.save(Menu(id="MT", date="2022-02-03", desc=dict_menu_2))

menu_repository.save(Menu(id="MX", date="2022-03-03", desc=dict_menu_3))

restaurant_reposotory = RestaurantRepository(database_path)

restaurant_reposotory.save_restaurants(Restaurant("restaurant_01", "Josu"))
restaurant_reposotory.save_restaurants(Restaurant("restaurant_02", "Joseba"))
