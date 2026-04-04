import os

from core.base_download_config import BaseDownloadConfig
from core.base_downloader import BaseDownloader


class YandexTracksDownloader(BaseDownloader):
    def download(self, tracks: list) -> None:
        print("РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: C:/Users/shteps/Downloads/OmniLoader/")

        # Создаем папку downloaded_music, если её нет
        os.makedirs("C:/Users/shteps/Downloads/OmniLoader/", exist_ok=True)

        for i, track in enumerate(tracks, start=1):
            # Берем название и артиста из самого объекта трека
            title = BaseDownloadConfig.sanitize_filename(track.title)
            artist = BaseDownloadConfig.sanitize_filename(
                (track.artists[0].name if track.artists else "НЕИЗВЕСТНЫЙ АРТИСТ")
            )

            # Формируем имя файла: Артист - Название.mp3
            # Это предотвратит перезапись файлов, если названия треков совпадают
            filename = f"C:/Users/shteps/Downloads/OmniLoader/{artist} - {title}.mp3"

            try:
                track.download(filename)
                print(f"✅ ЗАГРУЗКА ЗАВЕРШЕНА {i}/{len(tracks)}: {filename}")

            except Exception as e:
                print(f"❌ ОШИБКА ЗАГРУЗКИ {title}: {e}")

