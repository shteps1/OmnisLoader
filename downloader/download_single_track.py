import os
import re

from dotenv import load_dotenv
from yandex_music import Client


# Функция для очистки имени файла от запрещенных символов
def sanitize_filename(name):
    # Удаляем символы, которые нельзя использовать в именах файлов (Windows/Linux)
    return re.sub(r'[<>:"/\\|?*]', "", name).strip()


def download_yandex_track():
    load_dotenv()
    token = os.getenv("token")
    client = Client(token).init()
    # token = "y0__xDRoJLwBhje-AYg0uGb4BaJqu1Jv8zkgOQyvwObkn1l8AiNig"
    url = input("Введите ссылку на трек: ")
    print("Загрузка началась...")

    track = get_track(client, url)
    downloading(track)


def get_track(client, url):
    match = re.search(r"/album/(\d+)/track/(\d+)", url)
    if not match:
        raise ValueError("Неверный формат ссылки")

    album_id = match.group(1)
    track_id = match.group(2)
    track_key = f"{track_id}:{album_id}"

    track = client.tracks([track_key])[0]
    return track


def downloading(track) -> None:
    # Создаем папку downloaded_music, если её нет
    os.makedirs("C:/Users/shteps/Downloads/OmniLoader/", exist_ok=True)
    # Берем название и артиста из самого объекта трека
    title = sanitize_filename(track.title)
    artist = sanitize_filename(
        (track.artists[0].name if track.artists else "Unknown Artist")
    )
    # Формируем имя файла: Артист - Название.mp3
    # Это предотвратит перезапись файлов, если названия треков совпадают
    filename = f"C:/Users/shteps/Downloads/OmniLoader/{artist} - {title}.mp3"
    try:
        # print(f"Downloading {i + 1}/{len(tracks)}: {artist} - {title}...")
        track.download(filename)
        print(f"✅ Finished: {filename}")
    except Exception as e:
        print(f"❌ Error downloading {title}: {e}")


if __name__ == "__main__":
    try:
        download_yandex_track()
    except KeyboardInterrupt:
        print("Exit!")
