from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.Menu import MenuRepository


def test_should_save_a_menu():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    body = {
        "id": "01",
        "date": "2022-03-03",
        "desc": {"id_dish": "01", "name_dish": "Ensalada mixta",
                 "desc_dish": "Ensalada con cebolla"}
    }

    response = client.post("/api/menus", json=body)


# ASSERT (then)
    assert response.status_code == 200
    response_get = client.get("/api/menus/01")

    assert response_get.json == {
        "id": "01",
        "date": "2022-03-03",
        "desc": {"id_dish": "01", "name_dish": "Ensalada mixta",
                 "desc_dish": "Ensalada con cebolla"}
    }
