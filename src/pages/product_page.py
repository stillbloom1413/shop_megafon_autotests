from selenium.common import NoSuchElementException

from core.base_page import BasePage
from locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.get_text(ProductPageLocators.TITLE)

    def get_price(self):
        return self.get_text(ProductPageLocators.PRICE)

    def check_installment(self):
        return self.is_element_present(ProductPageLocators.INSTALLMENT)

