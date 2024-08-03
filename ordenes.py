import flet as ft

class Ordenes:
    def __init__(self, page):
        self.page = page
        self.address = ft.TextField(label = "Dirección",
                                    height = 40)
        self.table = ""
    
    def template(self):
        # Agregamos la tabla en una variable para poder hacer accesible desde su atributo
        self.table = ft.DataTable(
            width = 800,
            columns = [
                ft.DataColumn(label = ft.Text(value = "Código", 
                                              font_family = "Lato-Bold",
                                              size = 13,
                                              text_align = ft.TextAlign.CENTER)),
                ft.DataColumn(label = ft.Text(value = "Cliente", 
                                              font_family = "Lato-Bold",
                                              size = 13,
                                              text_align = ft.TextAlign.CENTER)),
                ft.DataColumn(label = ft.Text(value = "Dirección", font_family = "Lato-Bold",
                                              size = 13,
                                              text_align = ft.TextAlign.CENTER)),
            ],
            heading_row_color = "#BED3EE",
            data_row_color = "#dbdbdb",
            
        )

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
                                    font_family = "Lato-Bold"),
                            ft.Text("De Ordenes",
                                    color = "black",
                                    size = 20,
                                    font_family = "Lato-Bold")
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
                ),
                
                ft.Column(
                    col = 12,
                    controls = [
                        ft.Row(
                            controls = [
                                self.table
                            ],
                            scroll = True,
                        )
                    ],
                    scroll = True
                ),
           
            ]
        )

        self.page.add(view)
        self.page.update()

        # Cargamos la data de la tabla
        import time
        time.sleep(3)
        self.load_table()
    
    def load_table(self):
        self.table.rows = [
            ft.DataRow(
                cells = [
                    ft.DataCell(ft.Text("24440",
                                        size = 13),
                                        ),
                    ft.DataCell(ft.Text("Kevin De La Hoz",
                                         size = 13)),
                    ft.DataCell(ft.Text("Av Tricentenario Charallave Miranda",
                                         size = 13))
                ]
            )
        ]

        self.page.update()