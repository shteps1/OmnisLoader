# библиотеки
import os

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


def main():
    print(
        "OmnisLoader\nЧТОБЫ ВЫЙТИ CTRL + C\nИсточники: YouTube, Яндекс музыка, TikTok, SoundCloud, Twitch, instagram итд\n-------------------------------------------"
    )

    choosen_items = input("Выберите: 1[только один элемент] 2[весь плейлист]: ")
    source = input("Выберите источник: 1[YouTube & etc.] 2[Яндекс музыка]: ")
    user_inputted_url = input("Введите ссылки через запятую: ")

    if source == "1":
        yt_dlp_format = input(
            "Выберите формат 1[Лучшее качество видео и аудио] 2[Видео 1080p и лучшее аудио] 3[Только аудио]: "
        )
        web_download_config = WebDownloadingConfig(
            choosen_items, yt_dlp_format
        ).get_options()
        web_downloader = WebDownloader()
        web_downloader.download(web_download_config, user_inputted_url)

    elif source == "2":
        # токен для Яндекс Музыки и клиент для работы с API
        load_dotenv()
        token = os.getenv("token")
        client = Client(token).init()

        # конфиг для загрузки треков с Яндекс Музыки
        yandex_downloading_config = YandexDownloadingConfig(client, user_inputted_url)

        if choosen_items == "1":
            tracks = yandex_downloading_config.get_tracks(
                [url.strip() for url in user_inputted_url.split(",") if url.strip()]
            )

            # загрузчик для треков с Яндекс Музыки
            yandex_single_track_downloader = YandexTracksDownloader()
            yandex_single_track_downloader.download(tracks)

        elif choosen_items == "2":
            print("ok")

    else:
        print("Неверный источник")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(" \nВыход...")
