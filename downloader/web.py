import yt_dlp

from core.base_downloader import BaseDownloader


class WebDownloader(BaseDownloader):
    def download(self, web_download_config: dict, urls: list) -> None:
        print(f"РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: {web_download_config['paths']}")

        with yt_dlp.YoutubeDL(web_download_config) as ydl:
            ydl.download(urls)
