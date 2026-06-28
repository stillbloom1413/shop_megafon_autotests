import json
from pathlib import Path


class ConfigLoader:
    ROOT_DIR = Path(__file__).resolve().parents[2]

    FILE_MAP = {
        "search": ROOT_DIR / "tests" / "data" / "search_queries.json",
        "auth": ROOT_DIR / "config" / "auth_cookies.json",
    }

    @classmethod
    def _load_json(cls, file_key):
        """Внутренний метод: просто читает нужный файл по ключу"""
        path = cls.FILE_MAP.get(file_key)
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def get_regions(cls):
        """Возвращает словарь регионов для тестов"""
        data = cls._load_json("search")
        return data["regions"]

    @classmethod
    def get_auth_cookies(cls):
        """Возвращает куки авторизации для фикстур"""
        data = cls._load_json("auth")
        return data["cookies"]
