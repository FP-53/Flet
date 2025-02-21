import flet as ft 

def main(page: ft.Page): 
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "class 2"
    texto1 = ft.Text("texto1", size = 24, color = ft.colors.WHITE)
    texto2 = ft.Text("texto2", size = 24, color = ft.colors.WHITE)
    texto3 = ft.Text("texto3", size = 24, color = ft.colors.WHITE)
    
    fila_textos = ft.Row(
        controls=[texto1,texto2,texto3],
        alignment= ft.MainAxisAlignment.CENTER,
        spacing= 50
    )


    boton1= ft.FilledButton(text='Boton1')
    boton2= ft.FilledButton(text='Boton2')
    boton3= ft.FilledButton(text='Boton3')

    fila_botones = ft.Row(
        controls= [boton1,boton2,boton3],
        alignment= ft.MainAxisAlignment.CENTER,
        spacing= 100
    )


    page.add(fila_textos,fila_botones)


ft.app(target=main)