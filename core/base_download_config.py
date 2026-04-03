import re
from abc import ABC


class BaseDownloadConfig(ABC):
    # Функция для очистки имени файла от запрещенных символов
    def sanitize_filename(name):
        # Удаляем символы, которые нельзя использовать в именах файлов (Windows/Linux)
        return re.sub(r'[<>:"/\\|?*]', "", name).strip()
