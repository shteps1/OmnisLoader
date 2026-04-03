import os

from core.base_download_config import BaseDownloadConfig
from core.base_downloader import BaseDownloader


class YandexSingleTrackDownloader(BaseDownloader):
    def download(self, tracks: list) -> None:
        print("РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: C:/Users/shteps/Downloads/OmniLoader/")

        # Создаем папку downloaded_music, если её нет
        os.makedirs("C:/Users/shteps/Downloads/OmniLoader/", exist_ok=True)

        # for i, track in enumerate(tracks):
        #     # Берем название и артиста из самого объекта трека
        #     title = BaseDownloadConfig.sanitize_filename(track.title)
        #     artist = BaseDownloadConfig.sanitize_filename(
        #         (track.artists[0].name if track.artists else "Unknown Artist")
        #     )

        #     # Формируем имя файла: Артист - Название.mp3
        #     # Это предотвратит перезапись файлов, если названия треков совпадают
        #     filename = f"C:/Users/shteps/Downloads/OmniLoader/{artist} - {title}.mp3"

        #     try:
        #         # print(f"Downloading {i + 1}/{len(tracks)}: {artist} - {title}...")
        #         track.download(filename)
        #         print(f"✅ Finished: {filename}")
        #     except Exception as e:
        #         print(f"❌ Error downloading {title}: {e}")
        for i, track in enumerate(tracks):
            # Берем название и артиста из самого объекта трека
            title = BaseDownloadConfig.sanitize_filename(track.title)
            artist = BaseDownloadConfig.sanitize_filename(
                (track.artists[0].name if track.artists else "Unknown Artist")
            )

            # Формируем имя файла: Артист - Название.mp3
            # Это предотвратит перезапись файлов, если названия треков совпадают
            filename = f"C:/Users/shteps/Downloads/OmniLoader/{artist} - {title}.mp3"

            try:
                # print(f"Downloading {i + 1}/{len(tracks)}: {artist} - {title}...")
                track.download(filename)
                print(f"✅ Finished: {filename}")

            except Exception as e:
                print(f"❌ Error downloading {title}: {e}")

        # for track in tracks:
        #     title = BaseDownloadConfig.sanitize_filename(track.title)
        #     artist = BaseDownloadConfig.sanitize_filename(
        #         (track.artists[0].name if track.artists else "Unknown Artist")
        #     )
        #     # Формируем имя файла: Артист - Название.mp3
        #     # Это предотвратит перезапись файлов, если названия треков совпадают
        #     filename = f"C:/Users/shteps/Downloads/OmniLoader/{artist} - {title}.mp3"
        #     try:
        #         # print(f"Downloading {i + 1}/{len(tracks)}: {artist} - {title}...")
        #         track.download(filename)
        #         print(f"✅ Finished: {filename}")
        #     except Exception as e:
        #         print(f"❌ Error downloading {title}: {e}")
