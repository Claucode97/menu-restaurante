from flask import Flask, jsonify, request
from flask_cors import CORS
from src.lib.utils import object_to_json
from src.domain.Menu import Menu


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def home():
        return "Bienvenido/a"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/menus", methods=["GET"])
    def show_menu():
        menu = repositories["menu"].get_all()
        return object_to_json(menu)

    @app.route("/api/menus", methods=["POST"])
    def add_menu():
        body = request.json
        added_menu = Menu(**body)
        menu = repositories["menu"].save(added_menu)
        return ''

    @app.route("/api/menus/by-date/<date>", methods=["GET"])
    def show_menu_by_date(date):
        menu = repositories["menu"].get_by_date(date)
        return object_to_json(menu)

    @app.route("/api/menu_dia", methods=["GET"])
    def show_menu_by_id():
        id = "MM"
        menu = repositories["menu"].get_by_id(id)
        return object_to_json(menu)

    return app
