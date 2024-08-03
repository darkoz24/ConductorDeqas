import flet as ft
import requests, env,  time


class Login():
    def __init__(self, page):
        self.page = page
        self.email = ""
        self. contrasena = ""
    
    def template(self):
        # Estilo para la vista de login
        self.page.bgcolor = "#eeeff2"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        def prepare_data(e):
            self.email = input_email.value
            self.contrasena = input_pass.value
            self.send_data()
        input_email = ft.TextField(label = "Correo Electronico",
                                   height = 40,
                                   icon = ft.icons.EMAIL)
        input_pass = ft.TextField(label = "Contraseña",
                                  password = True,
                                  height = 40,
                                  icon = ft.icons.KEY)
        button_login = ft.ElevatedButton(text = "Entrar",
                                         color = "white",
                                         bgcolor = "#2B3A71",
                                         height = 40,
                                         icon = ft.icons.LOGIN,
                                         on_click = prepare_data)
        views = ft.ResponsiveRow(
            controls = [
                ft.Container(
                    col = 12,
                    content = ft.Column(
                        controls = [
                            ft.Image(src = "./images/logo.png",
                                     width = 160)
                        ],
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    ),
                    margin = 10
                ),
                ft.Container(
                    col = 12,
                    content = ft.Column(
                        controls = [
                            ft.Text(value = "Conductor DEQAS",
                                    font_family = "Lato-Bold",
                                    size = 22)
                        ],
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                    ),
                    margin = 10
                ),
                ft.Container(
                    col = 12,
                    content = ft.Column(
                        controls = [
                            input_email,
                            input_pass,
                        ]
                    )
                ),
                
                ft.Container(
                    col = 12,
                    content = ft.Column(
                        col = 12,
                        controls = [
                            button_login
                        ],
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                    ),
                ),

                ft.Container(
                    col = 12,
                    content = ft.Column(
                        controls = [
                            ft.Text(value = "DESARROLLADO POR KDLH SYSTEM",
                                    font_family = "Lato-Bold",
                                    size = 14)
                        ],
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                    ),
                    margin = 10
                ),
            ]
        )

        self.page.add(views)



    def send_data(self):
        modal = ft.AlertDialog(
            content = ft.Column(
                controls = [
                    ft.ProgressRing(),
                    ft.Text(value = "Cargando",
                            weight = "bold")
                ],
                height = 60,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                alignment = ft.MainAxisAlignment.CENTER
            ),
            open = True,
            modal = True,
        )
        self.page.overlay.append(modal)
        self.page.update()

        # Codigo para enviar el reuqest
        form = dict({
            "correo": self.email,
            "contrasena": self.contrasena
        })

        try:
            server = requests.post(url =  env.URL_DEQAS+"service-login",
                               data = form,
                               )
            response = server.json()
            if response["STR"] == 0:
                modal.content = ft.Column(
                    controls = [
                        ft.Icon(name = ft.icons.CHECKLIST_SHARP,
                                color = ft.colors.YELLOW,
                                size = 40),
                        ft.Text(value = env.FORM_EMPTY,
                                font_family = 'Lato-Bold')
                        ],
                        height = 60,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                        alignment = ft.MainAxisAlignment.CENTER
                )
                self.page.update()
                time.sleep(2)
                modal.open = False
                self.page.update()

            else:
                mensaje = ''
                icon = ''

                if response["response"]["STR"] == 0:
                    if "mensaje" in response["response"]:
                        icon = ft.icons.KEY
                        mensaje =  response["response"]['mensaje']
                    else:
                        icon = ft.icons.CHECKLIST_SHARP
                        mensaje = env.FORM_EMPTY

                    modal.content = ft.Column(
                    controls = [
                        ft.Icon(name = icon,
                                color = ft.colors.YELLOW,
                                size = 40),
                        ft.Text(value = mensaje,
                                font_family = 'Lato-Bold')
                        ],
                        height = 60,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                        alignment = ft.MainAxisAlignment.CENTER
                    )
                    self.page.update()
                    time.sleep(2)
                    modal.open = False
                    self.page.update()
                else:
                   
                    self.page.session.set("server", server.cookies.get('session'))
                    modal.open = False
                    self.page.update()

                    from route import Route
                    self.page.route = "/home"

                    Route().list_route(self.page)

        except Exception as e:
            modal.content = ft.Column(
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
            self.page.update()
            time.sleep(2)
            modal.open = False
            self.page.update()
