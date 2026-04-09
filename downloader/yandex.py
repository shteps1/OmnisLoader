from core.base_downloader import BaseDownloader
from core.base_downloading_config import BaseDownloadingConfig


class YandexTracksDownloader(BaseDownloader):
    def download(self, tracks: list, downloading_path: str):
        print(f"РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: {downloading_path}")

        for i, track in enumerate(tracks, start=1):
            # Берем название и артиста из самого объекта трека
            title = BaseDownloadingConfig.sanitize_filename(track.title)
            artist = BaseDownloadingConfig.sanitize_filename(
                (track.artists[0].name if track.artists else "НЕИЗВЕСТНЫЙ АРТИСТ")
            )

            # Формируем имя файла: Артист - Название.mp3
            # Это предотвратит перезапись файлов, если названия треков совпадают
            filename = f"{downloading_path}/{artist} - {title}.mp3"

            try:
                track.download(filename)
                print(f"✅ ЗАГРУЗКА ЗАВЕРШЕНА {i}/{len(tracks)}: {filename}")

            except Exception as e:
                print(f"❌ ОШИБКА ЗАГРУЗКИ {title}: {e}")


class YandexPlaylistDownloader(BaseDownloader):
    def download(self, tracks: list, downloading_path: str):
        print(f"РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: {downloading_path}")

        for i, track in enumerate(tracks, start=1):
            # Берем название и артиста из самого объекта трека
            title = BaseDownloadingConfig.sanitize_filename(track.title)
            artist = BaseDownloadingConfig.sanitize_filename(
                (track.artists[0].name if track.artists else "НЕИЗВЕСТНЫЙ АРТИСТ")
            )

            # Формируем имя файла: Артист - Название.mp3
            # Это предотвратит перезапись файлов, если названия треков совпадают
            filename = f"{downloading_path}/{artist} - {title}.mp3"

            try:
                track.download(filename)
                print(f"✅ ЗАГРУЗКА ЗАВЕРШЕНА {i}/{len(tracks)}: {filename}")

            except Exception as e:
                print(f"❌ ОШИБКА ЗАГРУЗКИ {title}: {e}")
