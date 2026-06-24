import time

from locators.header_locators import HeaderLocators
from pages.main_page import MainPage


class HeaderComponent:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @property
    def locate_logo(self):
        return self.driver.find_element(*HeaderLocators.logo)

    def click_logo(self):
        self.locate_logo.click()
        return MainPage(self.driver)
