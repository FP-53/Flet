import flet as ft 
import random

def main(page : ft.Page): 
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "App de Tabs con Flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text('Ejemplo de Tabs con Flet', size= 24, color= ft.colors.WHITE)


    # Todos los objetos en la Tab de tareas
    def generar_tareas():
        tareas = ['Hacer la compra', 'Llamar al medico', 'Estudiar para el examen', 'Hacer Ejercicio', 'Leer un libro', 'Hacer la cena']

        return random.sample(tareas,4)
    
    lista_tareas = ft.ListView(spacing= 10, padding= 20)

    def actualizar_tareas():
        lista_tareas.controls.clear()
        for tarea in generar_tareas(): 
            lista_tareas.controls.append(ft.Text(tarea, color= ft.colors.WHITE))
        page.update()

    actualizar_tareas()
    boton_actualizar = ft.ElevatedButton("Actualizar Tareas", on_click= lambda _: actualizar_tareas())
    contenido_tareas = ft.Column([lista_tareas, boton_actualizar])


    #Contenido de la Tab Perfil
    campo_nombre = ft.TextField(label= 'Nombre', bgcolor= ft.colors.BLUE_GREY_700)
    campo_email = ft.TextField(label='Email', bgcolor= ft.colors.BLUE_GREY_700)
    boton_guardar = ft.ElevatedButton('Guardar Perfil')
    contenido_perfil = ft.Column([campo_nombre,campo_email,boton_guardar])


    #Contenido configuracion
    switch_notificaciones = ft.Switch(label= 'Notificaciones', value= True)
    slider_volumen = ft.Slider(min=0, max=100, divisions=10, label='Volumen')
    contenido_config = ft.Column([switch_notificaciones,slider_volumen])

    tabs = ft.Tabs(

        # pestaña en la que se inicia la aplicacion
        selected_index=0, 

        # Duracion de la animacion para el cambio de pestañas, es en milisegundos 
        animation_duration= 300,

        #cada una de las pestanas y su respectivo icono
        tabs= [
            ft.Tab(text="Tareas", icon= ft.icons.LIST_ALT, content= contenido_tareas),
            ft.Tab(text="Perfil", icon= ft.icons.PERSON, content= contenido_perfil),
            ft.Tab(text="Coniguracion", icon= ft.icons.SETTINGS, content=contenido_config),
        ],
        expand= 1
    )

    page.add(titulo, tabs)




ft.app(target=main)