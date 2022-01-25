from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.info import InfoRepository, Info
from src.menu import Menu, data_for_testing_endpoint


def test_should_return_info_in_database():
    info_repository = InfoRepository(temp_file())
    app = create_app(repositories={"info": info_repository})
    client = app.test_client()

    info_repository.save(
        Info(
            app_name="test application",
        )
    )

    response = client.get("/api/info")
    assert response.json == {
        "app_name": "test application",
    }

def test_should_return_menu():
    primeros='ensalada mixta'
    segundos='lomo con patatas'
    postres='flan de huevo'
    menu_of_the_day=str(Menu(primeros,segundos,postres))
    expected='Primeros: ensalada mixta, Segundos: lomo con patatas, Postres: flan de huevo'

    assert menu_of_the_day == expected
  

