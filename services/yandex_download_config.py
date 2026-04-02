import re

from core.base_download_config import BaseDownloadConfig


class YandexDownloadConfig(BaseDownloadConfig):
    def __init__(self, client, kind: int, user_input: str) -> None:
        self.client = client
        # self.track_title = track_title
        self.kind = kind
        self.user_input = user_input

    def get_playlist_tracks(self) -> list:
        playlist = self.client.users_playlists(kind=self.kind)
        tracks_info = playlist.fetch_tracks_async()
        tracks = []

        for track_short in tracks_info:
            # Получаем полную информацию о треке
            track = track_short.fetch_track_async()
            tracks.append(track)

        return tracks

    def get_single_track(self):
        match = re.search(r"/album/(\d+)/track/(\d+)", self.user_input)
        if not match:
            raise ValueError("Неверный формат ссылки")

        album_id = match.group(1)
        track_id = match.group(2)
        track_key = f"{track_id}:{album_id}"

        track = self.client.tracks([track_key])[0]

        return track
