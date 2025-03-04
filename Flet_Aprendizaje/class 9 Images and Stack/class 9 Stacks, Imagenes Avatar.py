import flet as ft 

def main(page : ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = 'Stack, Image y Avatar'
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.ALWAYS

    titulo = ft.Text('Demostracion', size=30 ,weight= ft.FontWeight.BOLD, color=ft.colors.BLUE_200)

    def create_exampel (title, description, content):
        return ft.Container(
            content= ft.Column([
                ft.Text(title, size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                ft.Text(description, color= ft.colors.GREY_300),
                ft.Container(content=content, padding=10, border=ft.border.all(1, ft.colors.BLUE_GREY_400))
            ]),
            margin= ft.margin.only(bottom=20),
        )
    
    #un stack permite superponer objetos uno encima del otro
    stack_ejemplo = ft.Stack([
        ft.Container(width=200, height=200, bgcolor= ft.colors.BLUE_900),
        ft.Container(width=150, height=150, bgcolor= ft.colors.BLUE_700, left=25, top=25),
        ft.Container(width=100, height=100, bgcolor= ft.colors.BLUE_500, left=50, top=50),
        ft.Text('Stack demo', color= ft.colors.WHITE, size=12, left=70, top= 90)
    ], width=200, height=200)

    stack_example = create_exampel('Stack', 'Stack permite superponer objetos uno sobre otro', stack_ejemplo)


    imagen_internet = ft.Image(src='https://picsum.photos/200/200', width=200)
    imagen_local = ft.Image(src='assets/producto.png', width=200)
    columna_imagenes = ft.Column([
        imagen_internet, 
        ft.Text('Imagen desde URL', size=24, color=ft.colors.GREY_300),
        imagen_local,
        ft.Text('Imagen desde local (si esta disponible)', size=24, color=ft.colors.GREY_300)
        ])

    image_example= create_exampel('Imagenes', 'Imagenes traidas desde local y desde internet', columna_imagenes)

    #asi creamos una foto de avatar buscando una imagen desde internet
    imagen_internet_avatar = ft.CircleAvatar(
        foreground_image_src= 'https://avatars.githubusercontent.com/u/5479691',
        radius= 50
    )

    text_avatar = ft.CircleAvatar(
        content= ft.Text('AB', color= ft.colors.BLUE_GREY_800),
        radius=50, 
        bgcolor= ft.colors.BLUE_200
    )

    avatares = ft.Row([imagen_internet_avatar,text_avatar])

    avatares_example = create_exampel('Avatares', 'Distintas formas de mostrar avatares', avatares)

    page.add(titulo, stack_example, image_example, avatares_example)

ft.app(target= main)