import os
import re

from core.base_downloading_config import BaseDownloadingConfig


class YandexDownloadingConfig(BaseDownloadingConfig):
    def __init__(self, client, os_name: str, username: str) -> None:
        self.client = client
        self.os_name = os_name
        self.username = username

    def create_downloading_folder(self) -> str:
        path = f"{self.get_download_paths(self.os_name, self.username)}"
        os.makedirs(path, exist_ok=True)
        return path

    def get_playlist_tracks(self, kind: int) -> list:
        playlist = self.client.users_playlists(kind=kind)
        tracks_info = playlist.fetch_tracks()
        tracks = []
        for track_short in tracks_info:
            # Получаем полную информацию о треке
            track = track_short.fetch_track()
            tracks.append(track)

        return tracks, self.create_downloading_folder()

    def get_tracks(self, urls: list) -> list:
        tracks = []

        for url in urls:
            match = re.search(r"/album/(\d+)/track/(\d+)", url)
            if not match:
                raise ValueError("Неверный формат ссылки")

            album_id = match.group(1)
            track_id = match.group(2)
            track_key = f"{track_id}:{album_id}"

            track = self.client.tracks([track_key])[0]
            tracks.append(track)

        return tracks, self.create_downloading_folder()
