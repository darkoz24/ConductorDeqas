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
            page.clean()

            Navigation(page).nav()
            Escaner(page).template()
            page.update()

        elif route == "/ordenes":
            from ordenes import Ordenes
            page.clean()
            Ordenes(page).template()
      