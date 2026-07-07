import json
from pathlib import Path

from tests.data.filter import FilterDTO


class ConfigLoader:
    ROOT_DIR = Path(__file__).resolve().parents[2]

    FILE_MAP = {
        "auth": ROOT_DIR / "config" / "auth_cookies.json",
        "search": ROOT_DIR / "tests" / "data" / "test_data.json",
        "filters": ROOT_DIR / "tests" / "data" / "catalog_filters.json",
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

    @classmethod
    def get_catalog_test_data(cls, section_name: str = None):
        """Грузит фильтры каталога в парам тест"""
        data = cls._load_json("filters")
        test_data = []

        for section in data["catalog_sections"]:
            if section_name and section["section_name"] != section_name:
                continue

            url = section["url"]
            for item in section["filters"]:
                dto = FilterDTO(**item)
                test_data.append((url, dto))

        return test_data
