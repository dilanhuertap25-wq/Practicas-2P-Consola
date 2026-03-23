import flet as ft

def main(page: ft.Page):
    page.title = "Bienvenido al Cetis 146" 
    page.bgcolor = "black"
    page.update()
    # In Flet, horizontal_alignment expects CrossAxisAlignment and vertical_alignment expects MainAxisAlignment
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # BOTONES
                  
    def boton(texto, accion):
        return ft.ElevatedButton(
            texto, 
            width=150,
            height=50,
            style=ft.ButtonStyle(bgcolor="white", color="black", overlay_color="blue"),  # Color cuando se presiona el botón
           on_click=accion
        )
    
    # PANTALLA DE INICIO 

    def inicio(e=None):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido al Cetis 146", size=30, color="white"),
                    ft.ElevatedButton(
                    "Entrar",
                    style=ft.ButtonStyle(
                        bgcolor="white",
                        color="black",
                        overlay_color="blue"
                    ),
                    on_click=Menu
                )
                ],
 horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # MENU PRINCIPAL

    def Menu(e):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Elige la opcion que deseas ejecutar",
                            size=25, color="white"),
                    ft.Row(
                        [
                            boton("Saludo", saludo),
                            boton("Persona", persona)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            boton("Op.Mat", matematicas),
                            boton("Fig.Geo", figuras)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

        # PANTALLAS DE LAS OPCIONES

    def saludo(e):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Hola mundo programacion en clases", size=30, color="white"),
                    boton("Volver al menú", Menu)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )   
        )
        page.update()

    def persona(e):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Datos de la persona", size=30, color="white"),
                    boton("Volver al menú", Menu)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )   
        )
        page.update()

    def matematicas(e): 
        page.controls.clear()
        page.add(
            ft.Column(
                [
                   ft.Text("Operaciones matematicas", size=30, color="white"),
                   boton("Volver al menú", Menu)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )   
        )
        page.update()

    def figuras(e):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                   ft.Text("Figuras Geometricas", size=30, color="white"),
                   boton("Volver al menú", Menu)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )  
        )
        page.update()

    inicio()

ft.app(target=main)