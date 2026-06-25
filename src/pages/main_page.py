from components.header_page import HeaderComponent
from core.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)

    def navigate(self):
        self.open()
        return self
