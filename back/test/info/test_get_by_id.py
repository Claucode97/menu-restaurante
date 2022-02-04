from src.lib.utils import temp_file
from src.webserver import create_app
import json
from src.domain.Menu import Menu, MenuRepository


def test_should_return_one_menu_by_id():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    plate_01 = Menu(
        id="ML", date="2020-01-10", desc="Pollo con patatas"
    )
    plate_02 = Menu(id="MM", date="2022-10-15", desc=json.dumps({"firsts": [
        {"id_dish": "01", "name_dish": "ensalada mixta", "desc_dish": "ensalada con cebolla"}]}))
    menu_repository.save(plate_01)
    menu_repository.save(plate_02)

    response = client.get("/api/menu_dia")
    print('respuesta JSON: ', response.json)

    assert response.json == {"id": "MM", "date": "2022-10-15", "desc": {"firsts": [
        {"id_dish": "01", "name_dish": "ensalada mixta", "desc_dish": "ensalada con cebolla"}]}}
