import sys

sys.path.insert(0, "")


from src.domain.class_menu import MenuRepository, Menu
from src.menu import menu_ejemplo

database_path = "data/database.db"

menu_repository = MenuRepository(database_path)

menu_repository.save(Menu(id=1,desc=str(menu_ejemplo)))
