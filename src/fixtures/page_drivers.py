import time
import pytest

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage

COOKIES = [
    
]

@pytest.fixture(scope="function")
def main_page(driver):
    page = MainPage(driver)
    page.navigate()
    return page


@pytest.fixture(scope="function")
def authorized_main_page(driver):
    page = MainPage(driver)
    page.navigate()

    page.driver.add_cookie(
        {
            "name": "_ejwt",
            "value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJtZnItZXNob3AiLCJhdWQiOiJiMmMiLCJpYXQiOjE3ODIzOTUyOTAuMTE2NTcsImV4cCI6MTc4MzYwNDg5MC4xMTY1NzMsImp0aSI6ImN1c3RvbWVyIiwicGQiOnsiY2xpZW50SWQiOjY4MzY2MzIsImF1dGhTdGF0dXMiOjIsImF1dGhUaW1lIjoxNzgyMzk1MjkwfX0.Tn-b6y0iui7sZblCRFLDhaQzp6i5AVnh89CfVAlDsYVNh32N5ttW83fbY3-wS0YQMlSLP5pNjZfhmpIVUgcu97T45kuO4sVp_KwdsY9NkU__Ui6G03wBElti-CkvJnGDgwFA46GJnGb4qHj52DWK0kw8OdmxtbpHzsDr-HNg3z6LigJcI17IGZX32bKLxtuOaYw2sRuqvQJW3J9L1qWrg0pM-G4HZDrBK88RYnUfaIsvMuGLfQ7eNNb60ejMW-uBuMSR-XmxDBJT85_O9RAuI4uHCU5gwmq95seZGM029gJX5fQX_PjtmIe9w3xT5ILg4Pqkj52D92SVzD_Vhe_Gjw",
        }
    )
    page.driver.add_cookie({"name": "PHPSESSID", "value": "m9ab5t3o7ee1hkm6o3jt5mgru7"})

    time.sleep(1)
    page.driver.refresh()

    return page


import time
import pytest

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from tests.data.load_data import load_data


def _authorize_driver(driver):
    """Приватный хелпер для подкладывания кук из конфигурационного файла JSON"""
    # Забираем чистый список кук из файла конфигурации
    cookies = load_data("auth_cookies")
    for cookie in cookies:
        driver.add_cookie(cookie)

    time.sleep(1)
    driver.refresh()


@pytest.fixture(scope="function")
def main_page_factory(driver):
    """Фабрика для Главной страницы (умеет возвращать гостя или авторизованного)"""

    def _create_main_page(authorized=False):
        page = MainPage(driver)
        page.navigate()
        if authorized:
            _authorize_driver(page.driver)
        return page

    return _create_main_page


@pytest.fixture(scope="function")
def catalog_factory(driver):
    """Фабрика для страниц Каталога (принимает любой URL-путь и статус авторизации)"""

    def _create_catalog_page(category="/mobile", authorized=False):
        page = CatalogPage(driver)

        # Надежный паттерн: авторизуемся через корень, затем прыгаем в категорию
        if authorized:
            page.open()  # открываем базовый URL
            _authorize_driver(page.driver)

        page.navigate(category)
        return page

    return _create_catalog_page