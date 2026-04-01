import yt_dlp

from core.base import Base

class WebDownloader(Base):
    def __init__(self, download_config: dict, user_input: str):
        self.download_config = download_config
        self.user_input = user_input

    def load(self):
        print("РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: C/Users/shteps/Downloads/OmniLoader/")

        urls = [url.strip() for url in self.user_input.split(",") if url.strip()]

        with yt_dlp.YoutubeDL(self.download_config) as ydl:
            ydl.download(urls)
