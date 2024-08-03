import flet as ft

class Escaner:
    def __init__(self, page):
        self.page = page
    
    def template(self):
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        view = ft.ResponsiveRow(
            controls = [
                ft.Container(
                    col = 12,
                    content = ft.Row(
                        controls = [
                            ft.Icon(
                                color = "black",
                                size = 30,
                                name = ft.icons.QR_CODE_2_ROUNDED
                            ),
                            ft.Text("Escaner",
                                    color = "black",
                                    size = 20,
                                    font_family = "Lato-Bold"),
                            ft.Text("QR",
                                    color = "#2B3A71",
                                    size = 20,
                                    font_family = "Lato-Bold")
                                    
                        ],
                        vertical_alignment = ft.CrossAxisAlignment.CENTER,
                        alignment = ft.MainAxisAlignment.CENTER
                    ),
                    margin = 20
                    
                )
            ]
        )

        self.page.add(view)
        self.page.update()