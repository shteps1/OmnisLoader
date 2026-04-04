import yt_dlp

from core.base_downloader import BaseDownloader

class WebDownloader(BaseDownloader):
    def download(self, web_download_config: dict, user_input: str) -> None:
        print(f"РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: {web_download_config['paths']}")

        urls = [url.strip() for url in user_input.split(",") if url.strip()]

        with yt_dlp.YoutubeDL(web_download_config) as ydl:
            ydl.download(urls)
