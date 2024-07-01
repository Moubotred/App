import flet as ft
import libGui

def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.DARK

    def route_change(route):
        control = libGui.ControladorPantalla(page)
    
    page.on_route_change = route_change
    page.go(page.route) 


ft.app(target=main, view=ft.AppView.FLET_APP)
