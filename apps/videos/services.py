import yt_dlp, os, io


def download_video(url):
    try:
        # Configuraciones de yt-dlp para obtener el título del video
        ydl_opts_info = {'quiet': True}  # Para evitar mucha salida de texto en consola
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            video_info = ydl.extract_info(url, download=False)  # Solo extraer la información
            video_title = video_info.get('title', 'video')  # Obtener el título del video

        # Usamos una carpeta temporal para descargar el archivo
        archivo_temporal = f'{video_title}.mp4'

        # Configuraciones de yt-dlp para descargar el video
        ydl_opts = {
            'outtmpl': archivo_temporal,  # Guardar temporalmente en el disco con el título del video
            'format': 'best',  # Mejor calidad disponible
        }

        # Descargar el video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Leer el archivo temporal en un buffer
        buffer = io.BytesIO()
        with open(archivo_temporal, 'rb') as f:
            buffer.write(f.read())

        # Borrar el archivo temporal después de leerlo
        os.remove(archivo_temporal)

        # Posicionar el buffer al inicio
        buffer.seek(0)

        print('Descarga completa en el buffer.')
        return buffer, f'{video_title}.mp4'  # Devolver buffer y el nombre del archivo

    except Exception as e:
        print(f'Error: {str(e)}')
        return None, None  # Retornar None en caso de error

