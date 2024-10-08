import yt_dlp, os, io
import ffmpeg
import tempfile
from django.core.files.uploadedfile import UploadedFile


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

        # print('Descarga completa en el buffer.')
        return buffer, f'{video_title}.mp4'  # Devolver buffer y el nombre del archivo

    except Exception as e:
        print(f'Error: {str(e)}')
        return None, None  # Retornar None en caso de error


def convert_video(video=UploadedFile):
    try:
        # Guardar el archivo subido temporalmente en el sistema de archivos
        with tempfile.NamedTemporaryFile(delete=False, suffix=video.name) as temp_file:
            for chunk in video.chunks():
                temp_file.write(chunk)
        
        # Obtener la ruta del archivo temporal
        ruta_temporal = temp_file.name

        # Ruta del archivo de salida con extensión mp4
        output_video = video.name.rsplit('.', 1)[0] + '.mp4'
            
        # Ejecutar el comando de FFmpeg para la conversión
        ffmpeg.input(ruta_temporal).output(output_video, preset='fast').run()

        # Eliminar el archivo original si fue convertido
        os.remove(ruta_temporal)

        # Cargar video convertido a mp4 al buffer
        buffer = io.BytesIO()
        with open(output_video, 'rb') as f:
            buffer.write(f.read())

        # Eliminar el archivo original tras la conversión
        os.remove(output_video)

        # Posicionar el buffer al inicio
        buffer.seek(0)

        # print(f'Convertido: {video} -> {output_video}')
        return buffer, f'{video.name.rsplit(".", 1)[0]}.mp4'
    except Exception as e:
        print(f'Error en la conversión de {video}: {str(e)}')