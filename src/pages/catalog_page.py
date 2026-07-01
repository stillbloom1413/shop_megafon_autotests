import re

from core.base_page import BasePage
from locators.catalog_page_locators import CatalogPageLocators


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_mobile(self) -> CatalogPage:
        """
        Открытие каталога смартфонов страницы
        :return:
        """
        self.open("/mobile")
        return self

    def click_filter(
        self, type: str, group_name: str, value=None, boundary=None
    ) -> CatalogPage:
        """
        Заполняет один выбранный фильтр
        :param type: тип элемента
        :param group_name: наименование группы
        :param value: значение фильтра
        :param boundary: граница
        :return:
        """
        if type.startswith("accordion"):
            self.click(CatalogPageLocators.accordion_locator(group_name))

        if re.search(type, "input"):
            self.input_text(
                CatalogPageLocators.range_input_in_group(group_name, boundary), value
            )
            return self

        if re.search(type, "checkbox"):
            self.click(CatalogPageLocators.exact_value_in_group(group_name, value))
            return self

        else:
            self.click(CatalogPageLocators.standalone_switch(group_name))
            return self

    def apply_or_discard_filter(self, value) -> CatalogPage:
        """
        Применяет фильтры
        :param value: надпись на кнопке
        :return:
        """
        self.click(CatalogPageLocators.button_locator(value))
        return self
