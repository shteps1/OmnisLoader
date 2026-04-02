from downloader.web import WebDownloader
from services.download_config import DownloadConfig

# def choose_source() -> str:


# def downloading_from_YandexMusic() -> None:
#     print("1[только один элемент]\n2[весь плейлист]")
#     choosen_items = input("Выберите: ")
#     print("РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: C/Users/shteps/Downloads/OmniLoader/")

#     if choosen_items == "1":
#         download_yandex_track()

#     elif choosen_items == "2":
#         download_yandex_playlist()


def main():
    print(
        "ЧТОБЫ ВЫЙТИ CTRL + C\nПривет, я могу скачать все\nНапример: YouTube, Яндекс музыка, TikTok, SoundCloud, Twitch, instagram итд\n-------------------------------------------"
    )

    choosen_items = input("Выберите: 1[только один элемент] 2[весь плейлист]: ")
    yt_dlp_format = input(
        "Выберите формат 1[Лучшее качество видео и аудио]2[Видео 1080p и лучшее аудио]\n3[Только аудио]: "
    )
    user_inputted_url = input("Введите ссылки через запятую: ")
    
    download_config = DownloadConfig(choosen_items, yt_dlp_format).get_options()
    web_downloader = WebDownloader()
    web_downloader.load(download_config, user_inputted_url)
    
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        print("Выход...")
