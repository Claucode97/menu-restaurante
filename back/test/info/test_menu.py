from src.lib.utils import temp_file
from src.webserver import create_app

from src.domain.class_menu import Menu, MenuRepository

def test_should_return_empty_list():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()
    response = client.get("/api/menu_dia")
    assert response.json == []

#----------------------------------------------------------------

def test_should_return_list_of_plates():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    plate_01 = Menu(
        id="001", desc="Pollo con patatas"
    )
    plate_02 = Menu(
        id="002", desc="Ensalada mixta"
    )

    menu_repository.save(plate_01)
    menu_repository.save(plate_02)

    # ACT (when)
    response = client.get("/api/menu_dia")

    # ASSERT (then)
    assert response.json == [
        {
            "id": "001",
            "desc": "Pollo con patatas"
        },
        {
            "id": "002",
            "desc": "Ensalada mixta"
        }
    ]