# https://docs.google.com/forms/d/e/1FAIpQLScl9GppEl6eY8sri9rZ8qOoQWRVj0-0m0G-Z2Gc7wehFGIVww/viewform

import time
import socket
import telebot
import flet as ft
import libFrontend as lb


def informacion():

    btn = ft.Switch(active_color=ft.colors.WHITE)
    data = ft.TextField(label='IpServerPc', color=ft.colors.WHITE)
    
    return data,btn,ft.Card(
        content=ft.Container(
            content=ft.Column([    
                ft.Row([ft.Icon(ft.icons.COMPUTER, color=ft.colors.WHITE),data], alignment=ft.MainAxisAlignment.START),
                ft.Row([ft.Icon(ft.icons.WIFI_TETHERING, color=ft.colors.WHITE), ft.Text('Suministro:', color=ft.colors.WHITE),btn], alignment=ft.MainAxisAlignment.START),
                # ft.Row([ft.Icon(ft.icons.FOLDER, color=ft.colors.WHITE), ft.Text('Fotos: 63', color=ft.colors.WHITE)], alignment=ft.MainAxisAlignment.START),
            ]),
            width="100%",
            padding=20,
        ),  
        # color=ft.colors.colors_list(),
        color = ft.colors.with_opacity(0.7, '#ff97e3ad '),
        margin=ft.margin.only(top=10, left=10, right=10,bottom=20)
    )

def main(page:ft.Page):
    data,btn,inf = informacion()
    page.add(inf)

    while True:
        try:
            print(data.value)
            print(btn.value)
            time.sleep(2)
        except KeyboardInterrupt:
            break

ft.app(target=main)