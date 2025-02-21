import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = 'F app'
    text = ft.Text("MI primera app con Flet")
    text2 = ft.Text("Esto es mi primera prueba de flet")

    def cambiar_texto(e):
        if text2.value == "Esto es mi primera prueba de flet":
             text2.value = "prueba de boton"
        else: 
             text2.value = "Esto es mi primera prueba de flet"
        page.update()
       
    boton = ft.FilledButton(text="cambiar texto", on_click=cambiar_texto)
    page.add(text, text2, boton)



ft.app(target=main)