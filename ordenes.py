import flet as ft

class Ordenes:
    def __init__(self, page):
        self.page = page
        self.address = ft.TextField(label = "Dirección",
                                    height = 40)
    
    def template(self):
        view = ft.ResponsiveRow(
            controls = [
                ft.Container(
                    col = 12,
                    content = ft.Row(
                        controls = [
                            ft.Icon(
                                color = "black",
                                size = 30,
                                name = ft.icons.MARKUNREAD_MAILBOX_ROUNDED
                            ),
                            ft.Text("Cierre ",
                                    color = "#2B3A71",
                                    size = 20,
                                    font_family = "Bold"),
                            ft.Text("De Ordenes",
                                    color = "black",
                                    size = 20,
                                    font_family = "Bold")
                        ],
                        vertical_alignment = ft.CrossAxisAlignment.CENTER,
                        alignment = ft.MainAxisAlignment.CENTER
                    ),
                    margin = 20
                ),

                ft.Container(
                    col = 12,
                    content = ft.Column(
                        controls = [
                            self.address
                        ],
                   
                    ),
                
                )
            ]
        )

        self.page.add(view)
        self.page.update()