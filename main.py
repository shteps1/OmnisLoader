# библиотеки
import os

from dotenv import load_dotenv
from yandex_music import Client

# загрузчики
from downloader.web import WebDownloader
from downloader.yandex import YandexSingleTrackDownloader

# конфиги
from services.web_download_config import WebDownloadConfig
from services.yandex_download_config import YandexDownloadConfig

# def downloading_from_YandexMusic() -> None:
#     print("1[только один элемент]\n2[весь плейлист]")
#     choosen_items = input("Выберите: ")
#     print("РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: C/Users/shteps/Downloads/OmniLoader/")

#     if choosen_items == "1":
#         download_yandex_track()

#     elif choosen_items == "2":
#         download_yandex_playlist()


def find_playlists_kind(client) -> int:
    user_playlists = client.users_playlists_list()
    for playlist in user_playlists:
        print(f"kind={playlist.kind}  —  {playlist.title}")
    return int(input("Введите нужный kind: "))


def main():
    print(
        "ЧТОБЫ ВЫЙТИ CTRL + C\nПривет, я могу скачать все\nНапример: YouTube, Яндекс музыка, TikTok, SoundCloud, Twitch, instagram итд\n-------------------------------------------"
    )

    choosen_items = input("Выберите: 1[только один элемент] 2[весь плейлист]: ")
    source = input("Выберите источник: 1[YouTube & etc.] 2[Яндекс музыка]: ")
    user_inputted_url = input("Введите ссылки через запятую: ")
    if source == "1":
        yt_dlp_format = input(
            "Выберите формат 1[Лучшее качество видео и аудио] 2[Видео 1080p и лучшее аудио] 3[Только аудио]: "
        )
        web_download_config = WebDownloadConfig(
            choosen_items, yt_dlp_format
        ).get_options()
        web_downloader = WebDownloader()
        web_downloader.download(web_download_config, user_inputted_url)

    elif source == "2":
        # print(
        #     [
        #         user_inputted_url.strip()
        #         for url in user_inputted_url.split(",")
        #         if url.strip()
        #     ]
        # )

        load_dotenv()
        token = os.getenv("token")
        client = Client(token).init()
        # user_inputted_url = input("Введите ссылку на трек: ")
        playlist_kind = find_playlists_kind(client)
        yandex_download_config = YandexDownloadConfig(
            client, playlist_kind, user_inputted_url
        ).get_single_track(
            [url.strip() for url in user_inputted_url.split(",") if url.strip()]
        )
        yandex_single_track_downloader = YandexSingleTrackDownloader()
        yandex_single_track_downloader.download(
            yandex_download_config
        )
        print("Загрузка началась...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        print("Выход...")
