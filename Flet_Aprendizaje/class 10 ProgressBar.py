import flet as ft 
import time

def main(page:ft.Page):

    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Progress Bar"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text('Simulador de descarga de Arcivos', size=24, color=ft.colors.WHITE, weight= ft.FontWeight.BOLD)

    archivos = ft.Text('Selecciona los arcivos a descargar', size=16, color= ft.colors.WHITE70)

    
    progress_bar= ft.ProgressBar(width=400, color= ft.colors.AMBER, bgcolor= '#263238', value=0)

    progress_ring= ft.ProgressRing(stroke_cap=5, color= ft.colors.AMBER,  value=0)

    file_list = ft.Column({
        ft.Checkbox(label='Documento.pdf (2.5 MB)', value= False),
        ft.Checkbox(label='Imagen.jpg (5 MB)', value= False),
        ft.Checkbox(label='Video.mp4 (50 MB)', value= False),
        ft.Checkbox(label='Archivo.zip (100 MB)', value= False),
    })

    def simular_descarga(e):
        #va a revisar cada checkbox en mi lista de archivos y si esta seleccionado se guarda en la lista
        archivos_seleccionados= [checkbox for checkbox in file_list.controls if checkbox.value]
        if not archivos_seleccionados: 
            status_text.value = 'Por favor, selecciona al menos un archivo.'
            page.update()
            return

       
        progress_bar.value = 0 
        progress_ring.value = 0
        page.update()

        #elige todos los elementos del Label dentro de parentesis, para despues sumarlos, hacemos esto con cada archivo que tenemos seleccionado 
        total_size = sum([float(archivo.label.split("(")[1].split(" MB")[0]) for archivo in archivos_seleccionados])
        
        dowloaded = 0 

        for archivo in archivos_seleccionados: 
            file_size = float(archivo.label.split('(')[1].split(' MB')[0])
            status_text.value = f'Descargando {archivo.label}...'

            for _ in range(10): 
                time.sleep(0.3)
                dowloaded += file_size / 10 
                progress = min(dowloaded / total_size, 1)
                progress_bar.value = progress
                progress_ring.value = progress
                page.update()

        progress_bar.value = 1
        progress_ring.value = 1 
        status_text.value = 'Descarga Completa!'
        page.update

        time.sleep(1)
        progress_bar.value = 0
        progress_ring.value = 0 
        status_text.value= ''
        for checkbox in file_list.controls:
            checkbox.value = False
        page.update()


        


    contenedor = ft.Container( content= file_list, padding=20)


    fila = ft.Row([progress_bar,progress_ring], alignment= ft.MainAxisAlignment.CENTER)

    status_text = ft.Text('', color= ft.colors.WHITE)

    descargar_btn = ft.ElevatedButton('Descargar', on_click= simular_descarga, bgcolor= ft.colors.AMBER, color=ft.colors.BLACK)

    page.add(titulo, archivos, contenedor, fila, status_text, descargar_btn)

ft.app(target=main)