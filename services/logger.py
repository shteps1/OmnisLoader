import os


class Logger:
    def log(self, d: dict) -> None:
        if d["status"] == "downloading":
            percent = d.get("_percent_str", "?")
            speed = d.get("_speed_str", "?")
            eta = d.get("_eta_str", "?")
            print(f"\r⬇️  {percent}  |  Скорость: {speed}  |  Осталось: {eta}", end="")

        elif d["status"] == "finished":
            print(f"\n✅ Скачано: {d['filename']}")
            os.startfile("C:/Users/shteps/Downloads/OmniLoader/")

        elif d["status"] == "error":
            print("\n❌ Ошибка при загрузке")
