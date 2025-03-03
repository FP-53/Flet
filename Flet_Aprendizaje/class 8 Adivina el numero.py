import flet as ft
import random

def main(page: ft.Page): 
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = 'Adivina Numeros'
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    titulo = ft.Text('Cards, Divider y Vertical Divider', size=30, weight= ft.FontWeight.BOLD)

    numero_secreto = random.randint(1,10)
    intentos = 0 

    def verificar_intento(e):
        nonlocal intentos
        intento = int(input_numero.value)
        intentos += 1

        if intento == numero_secreto: 
            resultado.value = f'Correcto! Lo adivinaste en {intentos} intentos.'
            resultado.color = ft.colors.GREEN
            verificar_btn.disabled = True
        elif intento > numero_secreto: 
            resultado.value = 'Demasiado alto. Intenta de nuevo'
            resultado.color = ft.colors.ORANGE
        else: 
            resultado.value = 'Demasiado bajo. Intenta de nuevo'
            resultado.color = ft.colors.ORANGE

        intentos_text.value = f'Intentos: {intentos}'
        page.update()


    def reiniciar_juego(e): 
        nonlocal numero_secreto, intentos 
        numero_secreto = random.randint(1,10)
        intentos = 0 
        resultado.value = 'Adivina el numero entre el 1 y 10'
        resultado.color = ft.colors.WHITE
        intentos_text.value = f'Intentos: {intentos}'
        verificar_btn.disabled = False
        page.update()



    titulo_juego = ft.Text('Juego de Adivinanza', size= 20, weight= ft.FontWeight.BOLD)
    input_numero = ft.TextField(label= 'Tu Intento', width= 150)
    verificar_btn = ft.ElevatedButton('Verificar', on_click= verificar_intento)
    resultado = ft.Text('Adivina el numero entre el 1 y 10')
    intentos_text = ft.Text('Intentos: 0')
    reiniciar_btn = ft.ElevatedButton("Reiniciar Juego", on_click= reiniciar_juego)



    #las cards vienen funcionando como divs que modificar a gusto
    card_1 = ft.Card(
        content= ft.Container(
            content=  ft.Column([
                titulo_juego,
                input_numero, 
                verificar_btn, 
                resultado, 
                intentos_text,
                reiniciar_btn
            ], alignment= ft.MainAxisAlignment.CENTER,
            spacing= 20), 
            padding=10,
        ), 
        width= 300, 
        height= 400,
    )


    

    def cambiar_tema(e): 
        if page.theme_mode == ft.ThemeMode.DARK: 
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = ft.colors.BLUE_GREY_100
            tema_btn.text = 'Modo Oscuro'
        elif page.theme_mode == ft.ThemeMode.LIGHT: 
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = ft.colors.BLUE_GREY_800
            tema_btn.text = 'Modo Claro'
        page.update()

    titulo_tema = ft.Text("Cambiar Modo", size= 20, weight= ft.FontWeight.BOLD)
    tema_btn = ft.ElevatedButton("Modo claro", on_click= cambiar_tema)
    

    card_2 = ft.Card(
        content= ft.Container(
            content= ft.Column([titulo_tema, tema_btn],
                               alignment= ft.MainAxisAlignment.CENTER,
                               spacing= 20), 
            padding=10,
        ), 
        width= 200, 
        height= 150,
    )

    divider_simple = ft.Divider(height=1, color=ft.colors.BLUE_200)

    divider_vertical = ft.VerticalDivider(width=1, color=ft.colors.BLUE_200)
    
    layout = ft.Row([
        card_1,
        divider_vertical,
        card_2
        ], alignment= ft.MainAxisAlignment.CENTER)

    page.add(titulo,divider_simple,layout)

ft.app(target=main)