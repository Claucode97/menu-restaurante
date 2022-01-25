def data_for_testing_endpoint():
    menu_ejemplo={'primeros':[
        {'id':'01','nombre_plato':'ensalada mixta', 'descripcion':'ensalada con cebolla'},
        {'id':'02','nombre_plato':'Alubias con sus sacramentos', 'descripcion':'tocino, chorizo, morcilla'},
        {'id':'03','nombre_plato':'Spaguetti a la bolognesa', 'descripcion':'salsa de tomate'}
        
        ],
        'segundos':[
            {'id':'04','nombre_plato':'lomo con patatas', 'descripcion':'asado a las brasas'},
            {'id':'05','nombre_plato':'arroz cremoso de carne', 'descripcion':'verduras, curry'},
            {'id':'06','nombre_plato':'Muslo de pollo relleno', 'descripcion':'asado a las brasas, verduras salteadas'}
            
            ],
        'postres':[
            {'id':'07','nombre_plato':'flan horneado', 'descripcion':'alto contenido de huevo'},
            {'id':'08','nombre_plato':'helado', 'descripcion':'sin tacc'},
            {'id':'09','nombre_plato':'lemon pie', 'descripcion':'bizcocho'},
            {'id':'10','nombre_plato':'natilla de chocolate', 'descripcion':'derivado lacteo'}
        ]}
    return menu_ejemplo

class Menu():
    def __init__(self,primeros,segundos,postres):
        self.primeros=primeros
        self.segundos=segundos
        self.postres=postres

    def __str__(self):
        return f'Primeros: {self.primeros}, Segundos: {self.segundos}, Postres: {self.postres}'
    

# primeros=menu['primeros'][0]['nombre_plato']
# segundos=menu['segundos'][0]['nombre_plato']
# postres=menu['postres'][0]['nombre_plato']

# menu_dia=Menu(primeros,segundos,postres)
# print(menu_dia)
