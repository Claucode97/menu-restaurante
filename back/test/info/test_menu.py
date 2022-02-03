from src.lib.utils import temp_file
from src.webserver import create_app
import json

from src.domain.class_menu import Menu, MenuRepository

def test_should_return_empty_list():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()
    response = client.get("/api/menus")
    assert response.json == []

#----------------------------------------------------------------

def test_should_return_list_of_plates():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    plate_01 = Menu(
        id="001",date="2020-01-05", desc=json.dumps({"primeros":[
        {"id_dish":"01","name_dish":"ensalada mixta", "desc_dish":"ensalada con cebolla"}]})
    )
    plate_02 = Menu(
        id="002",date="2022-04-20", desc=json.dumps({"primeros":[
        {"id_dish":"01","name_dish":"ensalada mixta", "desc_dish":"ensalada con cebolla"}]})
    )
    plate_03 = Menu(
        id="003",date="2012-11-10", desc=json.dumps({"primeros":[
        {"id_dish":"01","name_dish":"ensalada mixta", "desc_dish":"ensalada con cebolla"}]})
    )

    menu_repository.save(plate_01)
    menu_repository.save(plate_02)
    menu_repository.save(plate_03)

    # ACT (when)
    response = client.get("/api/menus")

    # ASSERT (then)
    assert response.json == [
        {
            "id": "002",
            "date":"2022-04-20",
            "desc":{"primeros":[{"id_dish":"01","name_dish":"ensalada mixta", "desc_dish":"ensalada con cebolla"}]}
        },
        {
            "id": "001",
            "date":"2020-01-05",
            "desc":{"primeros":[{"id_dish":"01","name_dish":"ensalada mixta", "desc_dish":"ensalada con cebolla"}]}
        },
        {
            "id": "003",
            "date":"2012-11-10",
            "desc":{"primeros":[{"id_dish":"01","name_dish":"ensalada mixta", "desc_dish":"ensalada con cebolla"}]}
        }

    ]

    