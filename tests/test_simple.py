import time

import pytest

from pages.main_page import MainPage


def test_simple(driver):
    MainPage(driver).navigate()
    time.sleep(5)
