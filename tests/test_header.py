from components.header_page import HeaderComponent
from pages.main_page import MainPage


class TestHeader:

    def test_1(self, driver, url):
        MainPage(driver, url).navigate()
        HeaderComponent(driver, url).click_logo()
