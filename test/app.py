# libreria para convertir py a apk
# https://flet.dev/docs/getting-started/flet-controls
# https://gemini.google.com/app/af7853210759b27a

# pip install netifaces
# la libreria netifaces require un complemento para compilares

# complemento
# https://visualstudio.microsoft.com/es/visual-cpp-build-tools/

# import subprocess

# ifconfig = subprocess.run('ipconfig',stdout=subprocess.PIPE)
# data_decode = ifconfig.stdout.decode('cp1252')
# count_data = len(data_decode.split())
# raw_data = data_decode.split()
# print(raw_data[count_data-1])

import Lib.site_packages

import flet
# from flet.types import ThemeMode
from datetime import datetime

def main(page: ft.Page):
    page.title = "Photo Viewer"
    # page.theme_mode = ThemeMode.DARK

    def create_header():
        global state, photo_count
        host = ft.Text("Host: Guizado")
        state = ft.Switch(value="OFF", label="State", on_change=toggle_state, bgcolor=ft.colors.RED)
        photo_count = ft.Text("Photos: 10")
        return ft.Row([host, state, photo_count])

    def create_date_display():
        return ft.Text(f"Date: {datetime.now().strftime('%d/%m/%y')}")

    def create_image_view():
        return ft.Container(
            content=ft.Image(src="placeholder.png"),
            border=ft.border.all(2, ft.colors.WHITE),
            border_radius=ft.border_radius.all(10),
            padding=10,
        )

    def create_controls():
        return ft.Row([
            ft.ElevatedButton("Iniciar", on_click=toggle_state),
            ft.ElevatedButton("Buscar", on_click=search_photos)
        ])

    def toggle_state(e):
        if state.value == "OFF":
            state.value = "ON"
            state.bgcolor = ft.colors.GREEN
            # Add server function here
        else:
            state.value = "OFF"
            state.bgcolor = ft.colors.RED
        page.update()

    def search_photos(e):
        # Implement photo search logic here
        pass

    def update_photo_count():
        # Update photo count based on current date
        pass

    def update_wifi_zone():
        # Update WiFi zone name if applicable
        pass

    # Assemble the layout
    header = create_header()
    date_display = create_date_display()
    image_view = create_image_view()
    controls = create_controls()

    page.add(
        ft.Column([
            header,
            date_display,
            image_view,
            controls
        ])
    )

ft.app(target=main)