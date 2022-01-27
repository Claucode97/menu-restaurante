from src.lib.utils import temp_file
from src.webserver import create_app

from src.domain.class_menu import Menu, MenuRepository


def test_should_return_one_menu_by_id():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    plate_01 = Menu(
        id="ML", desc="Pollo con patatas"
    )
    plate_02 = Menu(
        id="MM", desc="Pollo con huevo"
    )
    menu_repository.save(plate_01)
    menu_repository.save(plate_02)
    # ACT (when)
    response = client.get("/api/menu_dia")
    print('respuesta JSON: ',response.json)
    # ASSERT (then)
    assert response.json =={
            "id":"ML",
            "desc": "Pollo con patatas"}