from src.lib.utils import temp_file
from src.webserver import create_app
from src.example_menu import dict_menu
from src.domain.Menu import Menu, MenuRepository


def test_should_save_a_menu():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    body = {
        "id": "01",
        "date": "2022-03-03",
        "desc": dict_menu
    }

    response = client.post("/api/menus", json=body)


# ASSERT (then)
    assert response.status_code == 200
    response_get = client.get("api/menus/01")

    assert response_get.json == {
        "id": "01",
        "date": "2022-03-03",
        "desc": {"firsts": [
            {"id_dish": "01", "name_dish": "Ensalada mixta",
             "desc_dish": "Ensalada con cebolla"},
            {"id_dish": "02", "name_dish": "Alubias con sus sacramentos",
             "desc_dish": "Tocino, chorizo, morcilla"},
            {"id_dish": "03", "name_dish": "Spaguetti a la bolognesa",
             "desc_dish": "Salsa de tomate"}

        ],
            "seconds": [
            {"id_dish": "04", "name_dish": "Lomo con patatas",
             "desc_dish": "Asado a las brasas"},
            {"id_dish": "05", "name_dish": "Arroz cremoso de carne",
                "desc_dish": "Verduras, curry"},
            {"id_dish": "06", "name_dish": "Muslo de pollo relleno",
                "desc_dish": "Asado a las brasas, verduras salteadas"}

        ],
            "desserts": [
            {"id_dish": "07", "name_dish": "Flan horneado",
             "desc_dish": "Alto contenido de huevo"},
            {"id_dish": "08", "name_dish": "Helado", "desc_dish": "Sin tacc"},
            {"id_dish": "09", "name_dish": "Lemon pie", "desc_dish": "Bizcocho"},
            {"id_dish": "10", "name_dish": "Natilla de chocolate",
                "desc_dish": "Derivado lacteo"}
        ]}
    }
