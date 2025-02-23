import flet as ft
import os #usamos os para trabajar con archivos
import base64 #usamos base64 para transformar las imagenes al mismo formato

def crear_producto(nombre,precio,color,imagen_nombre): 

    #intentamos traer la imagen con OS a la  aplicacion
    imagen_path = os.path.join(os.path.dirname(__file__), 'assets', imagen_nombre)

    #tratamos de abrir la imagen con el image_path para convertirla con base64 y si no funciona alertar del error
    try:
        with open(imagen_path, 'rb') as image_file:
            imagen_bytes = base64.b64encode(image_file.read()).decode()
    except FileNotFoundError: 
        print(f'Advertencia: la imagen {imagen_nombre} no existe en {imagen_path}')
        imagen_bytes = None

    return ft.Container(
            content= ft.Column([
                ft.Image(
                    src_base64=imagen_bytes,
                    width=150,
                    height=150,
                    fit= ft.ImageFit.CONTAIN,
                    error_content= ft.Text("Imagen no encontrada"))
                    if imagen_bytes else ft.Text('Image no encontrada')
                    ,
                ft.Text(nombre,
                        size= 16,\
                        weight= ft.FontWeight.BOLD
                        ),
                ft.Text(
                    f"${precio}",
                    size= 14
                ),
                ft.ElevatedButton(
                    'Agregar al carrito',
                    color= ft.colors.WHITE
                ),
            ]), \
            bgcolor= color,
            border_radius= 10, 
            padding= 20,
            alignment= ft.alignment.center, 
        )
    

def main(page: ft.Page):
    
    #titulo de la ventana
    page.title = 'Galeria Responsive'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLUE_GREY_900


    productos = [
        crear_producto("Producto 1", 19.99, ft.colors.GREY_500,  "Producto 1.png"),
        crear_producto("Producto 2", 29.99, ft.colors.YELLOW_500, "Producto 2.png"),
        crear_producto("Producto 3", 39.99, ft.colors.RED_500, "Producto 3.png"),
        crear_producto("Producto 4", 49.99, ft.colors.BLUE_500, "Producto 4.png"),
        crear_producto("Producto 5", 49.99, ft.colors.LIGHT_GREEN_500, "Producto 5.png"),
        crear_producto("Producto 6", 49.99, ft.colors.ORANGE_500, "Producto 6.png"),
        crear_producto("Producto 7", 49.99, ft.colors.BLUE_GREY_500, "Producto 7.png"),
        crear_producto("Producto 8", 49.99, ft.colors.GREEN_500, "Producto 8.png")
    ]

    galeria = ft.ResponsiveRow(
        [
            #cambiamos la distribucion de elemetos por columna segun la capacidad de la pantalla sm= small md = medium lg= lare
            ft.Container(producto, col={'sm':12, 'md': 6, 'lg':3} )
            for producto in productos
        ],
        run_spacing= 20, 
        spacing= 20,
    )

    cotenido = ft.Column([
        ft.Text('Galeria de Productos', size= 32, weight= ft.FontWeight.BOLD),
        ft.Divider(height=20, color= ft.colors.WHITE24),
        galeria,   
    ], 
    scroll= ft.ScrollMode.AUTO, 
    expand= True
    )

    page.add(cotenido)
    

ft.app(target=main)