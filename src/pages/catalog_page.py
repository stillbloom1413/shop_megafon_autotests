from core.base_page import BasePage


class CatalogPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def navigate_mobile(self):
        """
        Открытие каталога смартфонов страницы
        :return:
        """
        self.open("/mobile")
        return self