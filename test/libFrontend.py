import flet as ft

# *-------------COMPONENTES INICIO----------------------
def informacion():

    btn = ft.Switch(active_color=ft.colors.WHITE)
    
    return btn,ft.Card(
        content=ft.Container(
            content=ft.Column([    
                ft.Row([ft.Icon(ft.icons.COMPUTER, color=ft.colors.WHITE), ft.Text('Estado:', color=ft.colors.WHITE),btn], alignment=ft.MainAxisAlignment.START),
                ft.Row([ft.Icon(ft.icons.WIFI_TETHERING, color=ft.colors.WHITE), ft.Text('Suministro: Guizado', color=ft.colors.WHITE)], alignment=ft.MainAxisAlignment.START),
                ft.Row([ft.Icon(ft.icons.FOLDER, color=ft.colors.WHITE), ft.Text('Fotos: 63', color=ft.colors.WHITE)], alignment=ft.MainAxisAlignment.START),
            ]),
            width="100%",
            padding=20,
        ),  
        # color=ft.colors.colors_list(),
        color = ft.colors.with_opacity(0.7, '#ff97e3ad '),
        margin=ft.margin.only(top=10, left=10, right=10,bottom=20)
    )

def fecha():
    return ft.Row([
        ft.Container(
            width=60,
            height=40,
            bgcolor=ft.colors.with_opacity(0.7, '#ff97e3ad '),
            border_radius=10,
        ),
        ft.Container(
            content=ft.Row([ft.Icon(ft.icons.CALENDAR_TODAY), ft.Text('@1/@2/@3@3')], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.colors.with_opacity(0.7, '#ff97e3ad '),
            width=200,
            height=40,
            border_radius=10,
            margin=ft.margin.symmetric(horizontal=5),
        ),
        ft.Container(
            width=60,
            height=40,
            bgcolor=ft.colors.with_opacity(0.7, '#ff97e3ad'),
            border_radius=10,
        ),
    ], alignment=ft.MainAxisAlignment.CENTER)

def galeria():
    contenido = controles()
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Stack([   
                    ft.Container(

                        bgcolor=ft.colors.with_opacity(0.7, '#ff87c097'),
                        # width=900,
                        margin=5
                    ),


                    ft.Row([

                        ft.Stack([

                    ft.Container(
                        content=ft.Icon(ft.icons.NAVIGATE_BEFORE, color=ft.colors.WHITE),    
                        width=40, 
                        expand= True,
                        height=40,
                        bgcolor=ft.colors.with_opacity(1.0, '#ff60916e'), 
                        border_radius=5,
                        margin=ft.margin.only(top=240,right=250),
                        padding=10,
                        # alignment=ft.alignment.center_right
                        ),

                    ft.Container(
                        content=ft.Icon(ft.icons.NAVIGATE_NEXT, color=ft.colors.WHITE),
                        width=40,
                        height=40,
                        bgcolor=ft.colors.with_opacity(1.0, '#ff60916e'),
                        border_radius=5,
                        margin=ft.margin.only(top=240,left=250),
                        padding = 10,
                        # alignment=ft.alignment.center_left
                        ),

                        ])

                    ],alignment=ft.MainAxisAlignment.CENTER),
                
                ]),
                # aspect_ratio=47/20,  # Esto mantiene una relación de aspecto consistente
                width="100%",
                expand=True,
                # margin=ft.margin.only(bottom=10)
            ),
            ft.Container(
                content=contenido,
                padding=10,
            ),
        ]),
        
        width="100%",
        expand=True,
        margin=10,
        bgcolor=ft.colors.with_opacity(0.7, '#ff97e3ad'),
        border_radius=10,
    )

def controles():
    return ft.Row([
        ft.Container(
            content=ft.Icon(ft.icons.SEARCH, color=ft.colors.WHITE),
            bgcolor=ft.colors.GREEN_200,
            width=90,
            height=40,
            border_radius=5,
            margin=3
        ),
        
        ft.Container(
            content=ft.Icon(ft.icons.CAMERA_ALT, color=ft.colors.WHITE),
            bgcolor=ft.colors.GREEN_200,
            width=90,
            height=40,
            border_radius=5,
            margin=3
        ),

        ft.Container(
            content=ft.Icon(ft.icons.PLAY_ARROW, color=ft.colors.WHITE),
            bgcolor=ft.colors.GREEN_200,
            width=90,
            height=40,
            border_radius=5,
            margin = 3
            # margin=ft.margin.only(left=10),
        )
    ], 
    # width='100%',
    # expand=True,
    alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )
#*-----------------------------------------------------

# *-------------COMPONENTES BOT---------------------



#*-----------------------------------------------------


# *---------------------VENTANAS----------------------
def navegador(page):
    return ft.CupertinoNavigationBar(
        bgcolor=ft.colors.with_opacity(0.7, '#ff97e3ad '),
        inactive_color=ft.colors.WHITE,
        active_color=ft.colors.BLACK,

        on_change=lambda e: page.go(["/", "/second"][e.control.selected_index]),

        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.NEST_CAM_WIRED_STAND, label="Bot"),
        ]
    )

def Formulario(page):
    nav = navegador(page)
    return ft.View(
        controls = [
            ft.Text('Hola formulario'),
            nav,
        ]
    )
#*-----------------------------------------------------


# *----------CONTROL DE RUTAS Y NAVEGACION-------------
def Recolecciondatos(page):
    inf = informacion()
    fec = fecha()
    gal = galeria()
    # con = controles()
    nav = navegador(page)

    return ft.View(
        controls=[
            ft.Column([inf, fec, gal], spacing=10, expand=True),
            nav
        ]
    )

def ControladorPantalla(page):
    page.views.clear()
    
    if page.route == "/":
        page.views.append(Recolecciondatos(page))
    elif page.route == "/second":
        page.views.append(Formulario(page))
    page.update()
#*-----------------------------------------------------