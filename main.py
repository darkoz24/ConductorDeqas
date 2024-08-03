import flet as ft
from route import Route

class Main:
    def app(self, page: ft.Page):
        # Cargamos las fuente de la app
        page.fonts = {
            'Lato-Regular': "./fonts/Lato-Regular.ttf",
            'Lato-Bold': "./fonts/Lato-Bold.ttf",
        }
        page.theme = ft.Theme(font_family = "Lato-Regular")
        
        Route().list_route(page)

ft.app(Main().app)