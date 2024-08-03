import flet as ft

class Route:
    def list_route(self, page):
        route = page.route
        
        if route == "/":
            from login import Login
            Login(page).template()
        elif route == "/home":
            from navigation import Navigation
            from escaner import Escaner
            page.controls.pop()

            Navigation(page).nav()
            Escaner(page).template()
    
        elif route == "/ordenes":
            from ordenes import Ordenes
            page.controls.pop()
            Ordenes(page).template()

        elif route == "/salir":
            from login import Login
            page.clean()
            page.appbar = None
            Login(page).close_session()
      