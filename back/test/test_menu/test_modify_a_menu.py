from email import header
from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.Menu import MenuRepository


def test_should_modify_a_menu():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    body = {
        "id": "01",
        "date": "2022-03-03",
        "desc": {
            "id_dish": "01",
            "name_dish": "Ensalada mixta",
            "desc_dish": "Ensalada con cebolla",
        },
        "id_restaurant": "11",
    }

    body2 = {
        "id": "01",
        "date": "2022-03-03",
        "desc": {
            "id_dish": "01",
            "name_dish": "Ensalada atunada",
            "desc_dish": "Ensalada con chichos",
        },
        "id_restaurant": "11",
    }

    headers = {"Authorization": "11"}
    client.post("/api/menus", json=body)
    response = client.put("/api/menus", headers=headers, json=body2)
    # ASSERT (then)
    assert response.status_code == 200
    response_get = client.get("/api/menus/01")

    assert response_get.json == {
        "id": "01",
        "date": "2022-03-03",
        "desc": {
            "id_dish": "01",
            "name_dish": "Ensalada atunada",
            "desc_dish": "Ensalada con chichos",
        },
        "id_restaurant": "11",
    }
