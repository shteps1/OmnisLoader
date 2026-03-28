import yt_dlp

from downloading.download_playlist import download_yandex_playlist
from downloading.download_single_track import download_yandex_track


def choose_source() -> str:
    print("1[Яндекс музыка]\n2[Другой]")
    return input("Выберите источник скачивания: ")


def choose_format() -> dict:
    print("1[только один элемент]\n2[весь плейлист]")
    choosen_items = int(input("Выберите: "))
    print(
        "1[Лучшее качество видео и аудио]\n2[Видео 1080p и лучшее аудио]\n3[Только аудио]"
    )
    yt_dlp_format = input("Выберите формат: ")

    ydl_options = {
        "format": "",
        "outtmpl": "",
        "merge_output_format": "mp4",  # ffmpeg нужен
        "proxy": "",
        "paths": {
            "home": "C:/Users/shteps/Downloads/OmniLoader/",
        },
        "restrictfilenames": True,
        "windowsfilenames": True,  # имена файлов совместимые с windows
        "geo_bypass": True,
        # глушим стандартный вывод и выводим свое
        "quiet": True,
        "no_warnings": True,
        "progress_hooks": [progress_bar],  # Вывод только прогресс-бара и ошибок
        # Определяем список для добавления метаданных сразу — будем добавлять по условию ниже
        # "writethumbnail": True,
        "postprocessors": [
            {"key": "FFmpegMetadata"},
            {"key": "EmbedThumbnail"},
        ],
        # Ретраи при обрыве соединения и время ожидания ответа от сервера
        "socket_timeout": 30,
        "retries": 10,
        "fragment_retries": 10,
        # Имитация браузера и Куки для Яндекс Музыки — выберите один вариант:
        "cookiesfrombrowser": ("firefox", None, None, None),
        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "ru-RU,ru;q=0.9",
        },
    }

    if choosen_items == 1:
        ydl_options["outtmpl"] = (
            "%(playlist_title)s/%(playlist_index)02d. %(title)s.%(ext)s"  # Сохранять каждый плейлист в отдельную папку
        )

    elif choosen_items == 2:
        ydl_options["outtmpl"] = "%(title)s.%(ext)s"
        ydl_options["noplaylist"] = (True,)  # скачивать только трек, а не плейлист

    if yt_dlp_format == "1":
        ydl_options["format"] = (
            "bestvideo+bestaudio/best"  # лучший готовый поток без склейки
        )

    elif yt_dlp_format == "2":
        ydl_options["format"] = (
            "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]"  # до 1080p, готовый поток
        )

    elif yt_dlp_format == "3":
        ydl_options["format"] = "bestaudio/best"  # только аудио — ffmpeg не нужен
        ydl_options["writethumbnail"] = True  # скачивает обложку
        # Конвертация должна идти ПЕРЕД метаданными и обложкой
        ydl_options["postprocessors"].insert(
            0,
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            },
        )

    return ydl_options


def progress_bar(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "?")
        speed = d.get("_speed_str", "?")
        eta = d.get("_eta_str", "?")
        print(f"\r⬇️  {percent}  |  Скорость: {speed}  |  Осталось: {eta}", end="")

    elif d["status"] == "finished":
        print(f"\n✅ Скачано: {d['filename']}")

    elif d["status"] == "error":
        print("\n❌ Ошибка при загрузке")


def downloading_from_YandexMusic() -> None:
    print("1[только один элемент]\n2[весь плейлист]")
    choosen_items = input("Выберите: ")
    print("РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: C/Users/shteps/Downloads/OmniLoader/")

    if choosen_items == "1":
        download_yandex_track()

    elif choosen_items == "2":
        download_yandex_playlist()


def downloading_from_web(options: dict) -> None:
    user_input = input("Введите ссылки через запятую: ")
    print("РАСПОЛОЖЕНИЕ СКАЧАННЫХ ФАЙЛОВ: C/Users/shteps/Downloads/OmniLoader/")
    urls = [url.strip() for url in user_input.split(",") if url.strip()]

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download(urls)


def main():
    print(
        "ЧТОБЫ ВЫЙТИ CTRL + C\nПривет, я могу скачать все\nНапример: YouTube, Яндекс музыка, TikTok, SoundCloud, Twitch, instagram итд\n-------------------------------------------"
    )
    source = choose_source()

    if source == "1":
        downloading_from_YandexMusic()

    elif source == "2":
        downloading_format = choose_format()
        downloading_from_web(downloading_format)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        print("Выход...")
