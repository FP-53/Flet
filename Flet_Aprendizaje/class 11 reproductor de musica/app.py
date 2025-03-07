import flet as ft 
import pygame 
import os 
import asyncio
from mutagen.mp3 import MP3

class Song: 
    def __init__(self, filename):
        self.filename = filename

        #esto se usa para poder mostrar en pantalla el nombre del archivo de la cancion
        self.title = os.path.splitext(filename)[0]

        self.duration = self.get_duracion()

    def get_duracion(self): 
        #vamos a entrar a la carpeta canciones y vamos a tomar el archivo por su filename
        audio = MP3(os.path.join('Flet_Aprendizaje/class 11 reproductor de musica/canciones', self.filename))

        #con audio.info.length sacamos la duracion de la cancion y la enviamos a la funcion principal con return
        return audio.info.length
        


#las  funciones async o asincronicas permiten que si se tarda en cargar algun archivo esto no detenga la  funcion del programa y se realice en segundo plano
async def main(page : ft.Page): 
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.theme_mode = ft.ThemeMode.DARK
    page.title = 'Reproductor de musica'
    page.padding = 20

    titulo = ft.Text('Reproductor de Musica', size=30, color=ft.colors.WHITE)

    #usamos el mixer de pygame y le damos inicio para que nos permita reproducir musica
    pygame.mixer.init()

    #iteramos por cada elemento en la carpeta canciones y lo usamos para el reproductor de musica solo si es un archivo .mp3
    playlist = [Song(f) for f in os.listdir("Flet_Aprendizaje/class 11 reproductor de musica/canciones") if f.endswith('.mp3')]

    def load_song():

        #usamos mixer parqa cargar la cancion, la buscamos con os.path y seleccionamos la que tenga el indice actual, para mover entre canciones el indice se va a ir actualizando
        pygame.mixer.music.load(os.path.join('Flet_Aprendizaje\class 11 reproductor de musica\canciones', playlist[current_song_index].filename))

    def play_pause(e): 
        #preuntamos si la cancion que estamos usando ahora mismo se esta reproduciedo con music.get_music()
        if pygame.mixer.music.get_busy(): 
            #ponemos en pausa la cancion y cambiamos el icono de play_btn
            pygame.mixer.music.pause()
            play_btn.icon = ft.icons.PLAY_ARROW
        else: 
            #music.get_pos() obtiene la posicion en milisegundos por lo cual si es -1 significa que no ha empezado la cancion
            if pygame.mixer.music.get_pos() == -1:
                #comenzamos la cancion
                load_song()
                pygame.mixer.music.play()
            else: 
                #si no es asi y la cancion estaba en pausa, vamos a reanudarla
                pygame.mixer.music.unpause()
            play_btn.icon = ft.icons.PAUSE
        page.update()

    def update_song_info(): 
        song = playlist[current_song_index]
        song_info.value = f'{song.title}'
        duration.value = format_time(song.duration)
        progress_bar.value = 0.0
        current_time_text.value = '00:00'
        page.update()


    #usamos un delta como variable que puede cambiar cuando retrocedamos o avancemos, asi podemos uasr la misma funcion para ambas cosas
    def change_song (delta): 
        #traemos la variable desde fuera
        nonlocal current_song_index
        #aqui entra en trabajo el delta, puede ser +1 o -1 depende de si retrocedemos o avanzamos y usamos % para asegurarnos de que este entre los limites validos de la cancion, es decir, si queremos avanzar estando en la ultima cancion de la playlist nos va a eniar a la primera y si estamos en la primera y retrocedemos nos va a enviar a la ultima 
        current_song_index = (current_song_index + delta) % len(playlist)
        load_song()
        pygame.mixer.music.play()
        update_song_info()
        play_btn.icon = ft.icons.PAUSE()
        page.update()


    #funcion para cambiar la duracion de la cancion, la cancion por defecto te la entregan en segundos asi que cambiamos el formato a minuto : segundo
    def format_time(seconds): 
        minutes, seconds = divmod(int(seconds), 60)

        # minutes/seconds : 02d se usa para que ambos valores lo regrese en 2 digitos
        return f'{minutes:02d}:{seconds:02d}'
    
    async def update_progress(): 
        while True: 
            if pygame.mixer.music.get_busy():
                #divido entre 1000 para que el valor que me de sea compatible y no rompa la progress_bar ya que sus valores necesitan ser entre 1 y 0
                current_time = pygame.mixer.music.get_pos() / 1000
                #despues dividimos entre la duracion de la cancion actual para que el progreso sea proporcional a la duracion de la cancion
                progress_bar.value = current_time / playlist[current_song_index].duration
                current_time_text.value = format_time(current_time)
                page.update()

            #await hace una espera de un segundo antes de seguir revisando si se esta reproduciendo o no la cancion para actualizar la barra cada 1 segundo, este valor puede cambiar a gusto
            await asyncio.sleep(1)
        



    #creamos un indice de las canciones que escuchamos actualmente
    current_song_index = 0
    
    #usamos esta variable para colocar en pantalla el nombre de la cancion
    song_info = ft.Text(size=20, color=ft.colors.WHITE)

    #usamos esto para l tiempo que lleva reproducido la cancion
    current_time_text = ft.Text('00:00', color=ft.colors.WHITE60)

    duration = ft.Text('00:00', color=ft.colors.WHITE60)

    #una progress bar para ver el avance de la cancion
    progress_bar = ft.ProgressBar(value=0.0, width=300, color=ft.colors.WHITE, bgcolor= ft.colors.BLUE_GREY_800)

    #creamos los botones para parar o cambiar la cancion
    play_btn = ft.IconButton(icon=ft.icons.PLAY_ARROW, icon_color=ft.colors.WHITE, on_click=play_pause)
    prev_btn = ft.IconButton(icon=ft.icons.SKIP_PREVIOUS, icon_color=ft.colors.WHITE, on_click= lambda _:change_song(-1))
    next_btn = ft.IconButton(icon=ft.icons.SKIP_NEXT, icon_color=ft.colors.WHITE, on_click= lambda _:change_song(1))
    controls = ft.Row(
        [ prev_btn,play_btn,next_btn], 
        alignment= ft.MainAxisAlignment.CENTER
    )

    fila_reproductor = ft.Row(
        [current_time_text, progress_bar, duration],
        alignment= ft.MainAxisAlignment.CENTER
    )

    columna = ft.Column(
        [song_info, fila_reproductor, controls], 
        alignment= ft.MainAxisAlignment.CENTER, 
        spacing=20
        )

    page.add(columna)

    if playlist:
        load_song()
        update_song_info()
        page.update()
        await update_progress()
    else:
        #esto se muestra si la playlist esta vacia, recordar que la playlist solo acepta formato mp3
        song_info.value = 'No se encontraron canciones en la carpeta canciones'
        page.update()

ft.app(target=main)