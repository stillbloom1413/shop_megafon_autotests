from core.base_page import BasePage
from locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_title_text(self):
        """Возвращает название"""
        return self.get_text(ProductPageLocators.TITLE)

    def get_price_text(self):
        """Возвращает цену"""
        return self.get_text(ProductPageLocators.PRICE)

    def check_installment(self):
        """Проверяет наличие рассрочки"""
        return self.is_element_present(ProductPageLocators.INSTALLMENT)

    def check_pickup_today(self):
        """Проверяет возможность самовывоза сегодня"""
        return self.is_element_present(ProductPageLocators.PICKUP_TODAY)

    def check_discounts(self):
        """Проверяет скидки"""
        return self.is_element_present(ProductPageLocators.DISCOUNTS_BLOCK)

    def get_colour_text(self, colour):
        """Возвращает цвет"""
        return self.get_text(ProductPageLocators.colour_locators(colour))

    def get_characteristic_text(self, characteristic):
        """Возвращает характеристику"""
        locator = ProductPageLocators.characteristics_locators(characteristic)
        self.scroll_to_element(locator)
        return self.get_text(locator)

    def select_section(self, section):
        """Выбирает секцию"""
        locator = ProductPageLocators.section_locators(section)
        self.scroll_to_element(locator)
        self.click(locator)