import re
from abc import ABC


class BaseDownloadingConfig(ABC):
    def sanitize_filename(name: str) -> str:
        # Удаляет символы, которые нельзя использовать в именах файлов (Windows/Linux)
        return re.sub(r'[<>:"/\\|?*]', "", name).strip()

    def get_download_paths(os_name: str) -> str:
        # Возвращает путь к папке загрузок в зависимости от операционной системы
        if os_name == "Windows":
            return "C:/Users/Имя_Пользователя/Downloads/OmniLoader/"

        else:
            return "~/Downloads/OmniLoader/"
