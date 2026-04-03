import yt_dlp

from core.base_downloader import BaseDownloader

class WebDownloader(BaseDownloader):
    def download(self, download_config: dict, user_input: str):
        print("РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: C:/Users/Имя_Пользователя/Downloads/OmniLoader/")

        urls = [url.strip() for url in user_input.split(",") if url.strip()]

        with yt_dlp.YoutubeDL(download_config) as ydl:
            ydl.download(urls)
