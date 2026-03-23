import flet as ft  # type: ignore

def main(page: ft.Page):
    page.title = "Mi primera app" 
    page.add(ft.Text("¡Hola, mundo!"))

ft.app(target=main)