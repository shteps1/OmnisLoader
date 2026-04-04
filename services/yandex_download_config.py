import os
import re

from core.base_downloading_config import BaseDownloadingConfig


class YandexDownloadingConfig(BaseDownloadingConfig):
    def __init__(self, client, user_input: str, os_name: str) -> None:
        self.client = client
        self.user_input = user_input
        self.os_name = os_name

    def get_playlist_tracks(self, kind: int) -> list:
        playlist = self.client.users_playlists(kind=kind)
        tracks_info = playlist.fetch_tracks_async()
        tracks = []
        for track_short in tracks_info:
            # Получаем полную информацию о треке
            track = track_short.fetch_track_async()
            tracks.append(track)

        os.makedirs(f"{self.get_download_paths(self.os_name)}", exist_ok=True)
        return tracks

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

        os.makedirs(f"{self.get_download_paths(self.os_name)}", exist_ok=True)
        return tracks
