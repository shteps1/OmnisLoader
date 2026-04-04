from abc import ABC, abstractmethod


class BaseDownloader(ABC):
    @abstractmethod
    def download(self):
        pass
        
        
    def get_download_path(self, os_name: str) -> str:
        if os_name == "Windows":
            return "C:/Users/shteps/Downloads/OmniLoader/"
        elif os_name == "Linux" or "macOS":
            return "~/Downloads/OmniLoader/"
        else:
            raise ValueError("Unsupported OS")
