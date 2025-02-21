import flet as ft 

def main(page: ft.Page):

    #funcion para agregar tareas
    def agregar_tarea(e):
        if campo_tarea.value: 
            tarea = ft.ListTile(title=ft.Text(campo_tarea.value),
                                leading= ft.Checkbox(on_change=seleccionar_tarea))
            tareas.append(tarea)
            campo_tarea.value = ''
            actualizar_lista()

    #funcion para selecionar las tareas
    def seleccionar_tarea(e):
        seleccionadas = [t.title.value for t in tareas if t.leading.value]
        tareas_seleccionadas.value = "Tareas Seleccionadas: " + ', '.join(seleccionadas)
        page.update()

    #funcion para actualizar la lista
    def actualizar_lista():
        lista_tareas.controls.clear()
        lista_tareas.controls.extend(tareas)
        page.update()


    #coolor del odo
    page.bgcolor = ft.colors.BLUE_GREY_800

    #titulo
    page.title = 'Lista de tareas' 

    #alineacion
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    #titulo de la pagina
    titulo = ft.Text('Mi lista con flet', size = 30, weight= ft.FontWeight.BOLD, color= ft.colors.WHITE)
    campo_tarea = ft.TextField(hint_text='Escribe una nueva Tarea')

    boton_agregar = ft.FilledButton(text="Agregar Tareas", on_click=agregar_tarea)

    lista_tareas = ft.ListView(expand=1, spacing= 3)

    tareas = []
    tareas_seleccionadas = ft.Text("", size = 20, weight=ft.FontWeight.BOLD, color= ft.colors.WHITE)

    page.add(titulo,campo_tarea,boton_agregar, lista_tareas,tareas_seleccionadas)



ft.app(target=main)