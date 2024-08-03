import flet as ft
import requests, env

class Navigation:
    def __init__(self, page):
        self.page = page

    def nav(self):
        
        def nav_route(e):
            from route import Route
            option = e.control.selected_index
            if option == 0:
                self.page.route = "/home"
            elif option == 1:
                self.page.route = "/ordenes"
            elif option == 2:
                self.page.route = "/salir"

            Route().list_route(self.page)
          

        data = requests.get(url = env.URL_DEQAS+"getUserApp",
                            cookie = {
                                "session": self.page.session.get("server")
                            })
        data = data.json()

        self.page.appbar = ft.AppBar(
            leading = ft.IconButton(
                icon = ft.icons.DEHAZE_OUTLINED,
                on_click = lambda e: self.page.open(drawer)
            ),
            title = ft.Text(value = "Condutor Deqas",
                            font_family = "Lato-Bold",
                            size = 18),
            bgcolor = "#2B3A71",
            color = "white"
        )

        drawer = ft.NavigationDrawer(
            controls = [
                ft.Container(
                    content = ft.ResponsiveRow(
                        controls = [
                            ft.Column(
                                col = 2,
                                controls = [
                                    ft.Icon(
                                        name = ft.icons.ACCOUNT_CIRCLE,
                                        size = 24,
                                    )
                                ]
                            ),

                            ft.Column(
                                col = 10,
                                controls = [
                                    ft.Text(data["name"],
                                            font_family = "Lato-Bold"),
                                ]
                            )
                        ]
                    ),
                    margin = 40
                ),
                ft.NavigationDrawerDestination(
                    label = "Escaner QR",
                    icon = ft.icons.QR_CODE_2_ROUNDED,
                ),
          
                ft.NavigationDrawerDestination(
                    label = "Cierre De Orden",
                    icon = ft.icons.MARKUNREAD_MAILBOX_ROUNDED,
                ),
             
                ft.NavigationDrawerDestination(
                    label = "Salir",
                    icon = ft.icons.EXIT_TO_APP,
                ),
            ],
            on_change = nav_route
        )

    