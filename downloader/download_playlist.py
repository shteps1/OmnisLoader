import asyncio
import os
import re

from dotenv import load_dotenv
from yandex_music import Client


# Функция для очистки имени файла от запрещенных символов
def sanitize_filename(name):
    # Удаляем символы, которые нельзя использовать в именах файлов (Windows/Linux)
    return re.sub(r'[<>:"/\\|?*]', "", name).strip()


def find_playlists_kind(client) -> int:
    user_playlists = client.users_playlists_list()
    for playlist in user_playlists:
        print(f"kind={playlist.kind}  —  {playlist.title}")
    return int(input("Введите нужный kind: "))


def download_yandex_playlist():
    load_dotenv()
    token = os.getenv("token")
    # token = "y0__xDRoJLwBhje-AYg0uGb4BaJqu1Jv8zkgOQyvwObkn1l8AiNig"
    client = Client(token).init()
    kind = find_playlists_kind(client)
    tracks = get_tracks(client, kind)
    downloading(tracks)


def get_tracks(client, kind) -> list:
    playlist = client.users_playlists(kind=kind)
    tracks_info = playlist.fetch_tracks_async()
    tracks = []

    for track_short in tracks_info:
        # Получаем полную информацию о треке
        track = track_short.fetch_track_async()
        tracks.append(track)

    return tracks


def downloading(tracks) -> None:
    # Создаем папку downloaded_music, если её нет
    os.makedirs("C:/Users/shteps/Downloads/OmniLoader/", exist_ok=True)

    for i, track in enumerate(tracks):
        # Берем название и артиста из самого объекта трека
        title = sanitize_filename(track.title)
        artist = sanitize_filename(
            (track.artists[0].name if track.artists else "Unknown Artist")
        )

        # Формируем имя файла: Артист - Название.mp3
        # Это предотвратит перезапись файлов, если названия треков совпадают
        filename = f"OmniLoader/{artist} - {title}.mp3"

        try:
            # print(f"Downloading {i + 1}/{len(tracks)}: {artist} - {title}...")
            track.download_async(filename)
            print(f"✅ Finished: {filename}")
        except Exception as e:
            print(f"❌ Error downloading {title}: {e}")


if __name__ == "__main__":
    print("Downloading started...")
    try:
        download_yandex_playlist()
    except KeyboardInterrupt:
        print("Exit!")
