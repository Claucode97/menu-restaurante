def data_for_testing_endpoint():
    menu_ejemplo={'primeros':[
        {'nombre_plato':'ensalada mixta', 'descripcion':'ensalada con cebolla'},
        {'nombre_plato':'Alubias con sus sacramentos', 'descripcion':'tocino, chorizo, morcilla'},
        {'nombre_plato':'Spaguetti a la bolognesa', 'descripcion':'salsa de tomate'}
        
        ],
        'segundos':[
            {'nombre_plato':'lomo con patatas', 'descripcion':'asado a las brasas'},
            {'nombre_plato':'arroz cremoso de carne', 'descripcion':'verduras, curry'},
            {'nombre_plato':'Muslo de pollo relleno', 'descripcion':'asado a las brasas, verduras salteadas'}
            
            ],
        'postres':[
            {'nombre_plato':'flan horneado', 'descripcion':'alto contenido de huevo'},
            {'nombre_plato':'helado', 'descripcion':'sin tacc'},
            {'nombre_plato':'lemon pie', 'descripcion':'bizcocho'},
            {'nombre_plato':'natilla de chocolate', 'descripcion':'derivado lacteo'}
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
