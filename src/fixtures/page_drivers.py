import pytest

from pages.main_page import MainPage


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)
