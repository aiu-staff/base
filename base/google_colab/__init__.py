from IPython.display import HTML


def show_video(video_url, current_time=0):
     """
    Отображает HTML-код для воспроизведения видео в формате MP4 с возможностью указания начального времени воспроизведения.

    Args:
        video_url (str): URL видеофайла в формате MP4.
        current_time (float, optional): Начальное время воспроизведения видео в секундах. 
            По умолчанию равно 0.

    Returns:
        None: Функция не возвращает значения. Генерирует HTML для отображения видео в браузере.

    Note:
        HTML-код включает тег `<video>` с атрибутом `controls` для управления воспроизведением 
        и JavaScript для установки текущей позиции воспроизведения видео.
    """

     HTML(f'''
    <video id="video_player" width="800" controls>
    <source src="{video_url}" type="video/mp4">
    Ваш браузер не поддерживает видео.
    </video>
    <script>
    var video = document.getElementById('video_player');
    video.currentTime = {current_time} ;  
    </script>
    ''')