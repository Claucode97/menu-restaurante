import sqlite3


class Menu:
    def __init__(self, primeros, segundos, postres, id):
        self.primeros = primeros
        self.segundos = segundos
        self.postres = postres
        self.id = id

    def to_dict(self):
        return {"primeros": self.primeros, "segundos": self.segundos, "postres": self.postres}


class MenuRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists menu_dia (
                nombre_plato varchar,
                descripcion varchar,
                id varchar
                
            )
        """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from menu_dia"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        dict_menu = []
        for item in data:
            menu_class = Menu(
                nombre_plato= item["nombre_plato"], descripcion=item["descripcion"], id= item["id"]
            )
            dict_menu.append(menu_class)



        return dict_menu

    def save(self, info):
        sql = """insert into info (app_name) values (
            :app_name
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, info.to_dict())
        conn.commit()
