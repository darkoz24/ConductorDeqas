import flet as ft
import requests, env, time, json

class Ordenes:
    def __init__(self, page):
        self.page = page
        self.address = ft.TextField(label = "Dirección",
                                    height = 40,
                                    content_padding = 4,
                                    border_color = "#2B3A71",
                                    border_radius = 6,)
        self.table = ""
        self.alert = ft.AlertDialog()
    
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
                ft.DataColumn(label = ft.Text(value = "Acción", font_family = "Lato-Bold",
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
        self.load_table()
    
    def load_table(self):
    
        # COnsultar al servidor
        cookie = {"session": self.page.session.get("server")}

        try: 
            get_order = requests.get(url = env.URL_DEQAS+"listOrderByDriver",
                                    cookies = cookie)
            get_order = get_order.json()
            json_data = json.loads(get_order["data"][0][1])
        
            rows_table = list()
            count = 0
            for order in json_data:
        
                rows_table.append(
                    ft.DataRow(
                        cells = [
                            ft.DataCell(ft.Text(order["codigo"],
                                                size = 13),
                                                ),
                            ft.DataCell(ft.Text(order["cliente"],
                                                size = 13)),
                            ft.DataCell(ft.Text(order["direccion"],
                                                size = 13)),
                            ft.DataCell(ft.IconButton(icon = ft.icons.CHECK_BOX,
                                                      icon_color = ft.colors.BLACK,
                                                      on_click = lambda e: self.form_close_order(order["id"]))
                                                      ),
                        ],
                    )
                )
                count = count + 1
            
            self.table.rows = rows_table
        except Exception as e:
            print(e)
            self.alert.content = ft.Column(
                controls = [
                    ft.Icon(name = ft.icons.CLOUD_OFF,
                            color = ft.colors.RED,
                            size = 40),
                    ft.Text(value = env.ERROR_500,
                            font_family = 'Lato-Bold')
                ],
                height = 60,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                alignment = ft.MainAxisAlignment.CENTER
            
            )
            self.alert.open = True
            self.alert.modal = True
            self.page.overlay.append(self.alert)
            self.page.update()

            time.sleep(2)
            self.alert.open = False
            self.page.update()

        self.page.update()
    
    def form_close_order(self, id_order):
        self.status = ft.Dropdown(label = "Estatus",
                                  options = [
                                    ft.dropdown.Option(key = "Rechazado",
                                                        text = "Rechazado"),
                                    ft.dropdown.Option(key = "Parcial",
                                                        text = "Parcial"),
                                    ft.dropdown.Option(key = "Aprobado",
                                                        text = "Aprobado"),
                                ],
                                height = 45,
                                content_padding = 4,
                                border_color = "#2B3A71",
                                border_radius = 6,
                            )
        
        self.razon =  ft.Dropdown(label = "Razon",
                                  options = [
                                        ft.dropdown.Option(key = "Entrega Realizada",
                                                         text = "Entrega Realizada"),
                                        ft.dropdown.Option(key = "Entrega realizada paga en efectivo",
                                                         text = "Entrega realizada paga en efectivo"),
                                        ft.dropdown.Option(key = "Entrega realizada paga en transferencia",
                                                         text = "Entrega realizada paga en transferencia"),
                                  ],
                                  height = 45,
                                  content_padding = 4,
                                  border_color = "#2B3A71",
                                  border_radius = 6,)
        
        self.comentario = ft.TextField(label = "Comentario",
                                       multiline = True,
                                       height = 60,
                                       content_padding = 4,
                                       border_color = "#2B3A71",
                                       border_radius = 6,)
        
        def close_modal(e):
            self.page.overlay.pop()
            self.page.update()

        modal_view = ft.ResponsiveRow(
            controls = [
                ft.Container(
                    col = 12,
                    bgcolor = "#eeeff2",
                    content = ft.ResponsiveRow(
                        controls = [
                            ft.Column(
                                col = 12,
                                controls = [
                                    ft.Text(value = "Cerrar Orden",
                                            font_family = "Lato-Bold",
                                            size = 22)
                                ],
                                horizontal_alignment = ft.CrossAxisAlignment.CENTER
                            ),

                            ft.Column(
                                col = 12,
                                controls = [
                                    self.status
                                ]
                            ),

                            ft.Column(
                                col = 12,
                                controls = [
                                    self.razon
                                ]
                            ),

                            ft.Column(
                                col = 12,
                                controls = [ 
                                    self.comentario
                                ]
                            ),

                            ft.ElevatedButton(text = "Foto",
                                                icon = ft.icons.CAMERA,
                                                bgcolor = "#2B3A71",
                                                color = "white",
                                                col = 6
                                            ),
                            
                            ft.ElevatedButton(text = "Cerrar",
                                                icon = ft.icons.SAVE,
                                                bgcolor = "#2B3A71",
                                                color = "white",
                                                col = 12
                                            ),
                            
                            ft.ElevatedButton(text = "Cancelar",
                                                icon = ft.icons.CANCEL,
                                                bgcolor = ft.colors.RED,
                                                color = "white",
                                                col = 12,
                                                on_click = close_modal
                                            ),
                            
                        ]
                    ),
                    padding = 10,
                )
            ],
        )

        self.page.overlay.append(modal_view)
        self.page.update()