from core.base_page import BasePage


class MainPage(BasePage):

    def navigate(self):
        self.open()
        return self
