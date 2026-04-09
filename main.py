# библиотеки
import os
import platform

from dotenv import load_dotenv
from yandex_music import Client

# загрузчики
from downloader.web import WebDownloader
from downloader.yandex import YandexTracksDownloader

# конфиги
from services.web_download_config import WebDownloadingConfig
from services.yandex_download_config import YandexDownloadingConfig


def find_playlists_kind(client) -> int:
    user_playlists = client.users_playlists_list()
    for playlist in user_playlists:
        print(f"kind={playlist.kind}  —  {playlist.title}")
    return int(input("Введите нужный kind: "))


def choose_format():
    os_name = platform.system()  # показывает ОС пользователя
    username = input("Введите имя пользователя вашего пк: ").strip()
    username = "shteps"
    choosen_items = input("Выберите: 1[только один элемент] 2[весь плейлист]: ").strip()
    source = input("Выберите источник: 1[YouTube & etc.] 2[Яндекс музыка]: ").strip()
    user_inputted_url = input("Введите ссылки через запятую: ")
    urls = [url.strip() for url in user_inputted_url.split(",") if url.strip()]
    return os_name, username, choosen_items, source, urls


def main():
    # Приветствие
    print(
        "OmnisLoader\nЧТОБЫ ВЫЙТИ CTRL + C\nИсточники: YouTube, Яндекс музыка, TikTok, SoundCloud, Twitch, instagram итд\n-------------------------------------------"
    )

    # получаем данные от пользователя
    os_name, username, choosen_items, source, urls = choose_format()

    if source == "1":
        yt_dlp_format = input(
            "Выберите формат 1[Лучшее качество видео и аудио] 2[Видео 1080p и лучшее аудио] 3[Только аудио]: "
        )
        web_download_config = WebDownloadingConfig(
            choosen_items, yt_dlp_format, os_name, username
        ).get_options()
        web_downloader = WebDownloader()
        web_downloader.download(web_download_config, urls)

    elif source == "2":
        # токен для Яндекс Музыки и клиент для работы с API
        load_dotenv()
        token = os.getenv("token")
        client = Client(token).init()

        # конфиг для загрузки треков с Яндекс Музыки
        yandex_downloading_config = YandexDownloadingConfig(client, urls, os_name, username)
        yandex_downloading_config.create_downloading_folder()

        if choosen_items == "1":
            tracks = yandex_downloading_config.get_tracks(urls)

            # загрузчик для треков с Яндекс Музыки
            yandex_single_track_downloader = YandexTracksDownloader()
            yandex_single_track_downloader.download(tracks)

        elif choosen_items == "2":
            kind = find_playlists_kind(client)
            tracks = yandex_downloading_config.get_playlist_tracks(kind)
            # загрузчик для плейлиста с Яндекс Музыки
            # yandex_playlist_downloader = YandexPlaylistDownloader()
            # yandex_playlist_downloader.download(tracks)

    else:
        print("Неверный источник")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(" \nВыход...")
