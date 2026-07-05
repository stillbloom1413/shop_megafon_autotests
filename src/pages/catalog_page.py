import re

from core.base_page import BasePage
from locators.catalog_page_locators import CatalogPageLocators
from pages.product_page import ProductPage


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
        self, filter_type: str, group_name: str, value=None, boundary=None
    ) -> CatalogPage:
        """
        Заполняет один выбранный фильтр
        :param filter_type: тип элемента
        :param group_name: наименование группы
        :param value: значение фильтра
        :param boundary: граница
        :return:
        """
        if filter_type.startswith("accordion"):
            accordion_locator = CatalogPageLocators.accordion_locator(group_name)
            self.scroll_to_element(accordion_locator)
            self.click(accordion_locator)

        if "input" in filter_type:
            input_locator = CatalogPageLocators.range_input_in_group(
                group_name, boundary
            )
            self.scroll_to_element(input_locator)
            self.input_text(input_locator, value)

        elif "checkbox" in filter_type:
            checkbox_locator = CatalogPageLocators.exact_value_in_group(
                group_name, value
            )
            self.scroll_to_element(checkbox_locator)
            self.click(checkbox_locator)

        else:
            switch_locator = CatalogPageLocators.standalone_switch(group_name)
            self.scroll_to_element(switch_locator)
            self.click(switch_locator)

        return self

    def apply_or_discard_filter(self, value) -> CatalogPage:
        """
        Применяет фильтры
        :param value: надпись на кнопке
        :return:
        """
        locator = CatalogPageLocators.button_locator(value)
        self.click(locator)
        return self

    def select_first_product(self):
        """
        Клик по первому товару из списка
        :return:
        """
        self.find(CatalogPageLocators.FIRST_PRODUCT).click()
        return ProductPage(self.driver)
