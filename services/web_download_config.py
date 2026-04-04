from core.base_downloading_config import BaseDownloadingConfig


class WebDownloadingConfig(BaseDownloadingConfig):
    def __init__(self, choosen_items: str, yt_dlp_format: str, os_name: str) -> None:
        self.choosen_items = choosen_items
        self.yt_dlp_format = yt_dlp_format
        self.os_name = os_name

    def get_options(self) -> dict:
        ydl_options = {
            "format": "",
            "outtmpl": "",
            "merge_output_format": "mp4",  # ffmpeg нужен
            "paths": {
                "home": f"{self.get_download_paths(self.os_name)}",
            },
            "restrictfilenames": True,
            "windowsfilenames": True,  # имена файлов совместимые с windows
            "geo_bypass": True,
            # глушим стандартный вывод и выводим свое
            "quiet": False,
            "no_warnings": True,
            # "progress_hooks": [logger],  Вывод только прогресс-бара и ошибок
            # Определяем список для добавления метаданных сразу — будем добавлять по условию ниже
            # Ретраи при обрыве соединения и время ожидания ответа от сервера
            "socket_timeout": 30,
            "retries": 10,
            "fragment_retries": 10,
            # Имитация браузера и Куки для Яндекс Музыки — выберите один вариант:
            "http_headers": {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                ),
                "Accept-Language": "ru-RU,ru;q=0.9",
            },
        }

        if self.choosen_items == "1":
            ydl_options["outtmpl"] = (
                "%(playlist_title)s/%(playlist_index)02d. %(title)s.%(ext)s"  # Сохранять каждый плейлист в отдельную папку
            )

        elif self.choosen_items == "2":
            ydl_options["outtmpl"] = "%(title)s.%(ext)s"
            ydl_options["noplaylist"] = (True,)  # скачивать только трек, а не плейлист

        if self.yt_dlp_format == "1":
            ydl_options["format"] = (
                "bestvideo+bestaudio/best"  # лучший готовый поток без склейки
            )
            ydl_options["postprocessors"] = [
                {"key": "FFmpegMetadata"},
                {"key": "EmbedThumbnail"},
            ]

        elif self.yt_dlp_format == "2":
            ydl_options["format"] = (
                "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]"  # до 1080p, готовый поток
            )
            ydl_options["postprocessors"] = [
                {"key": "FFmpegMetadata"},
                {"key": "EmbedThumbnail"},
            ]

        elif self.yt_dlp_format == "3":
            ydl_options["format"] = "bestaudio/best"  # только аудио — ffmpeg не нужен
            ydl_options["writethumbnail"] = True  # скачивает обложку
            # Конвертация должна идти ПЕРЕД метаданными и обложкой
            ydl_options["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                },
                {"key": "FFmpegMetadata"},
                {"key": "EmbedThumbnail"},
            ]

        return ydl_options
