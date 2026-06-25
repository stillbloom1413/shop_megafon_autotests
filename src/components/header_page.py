from components.region_selector import RegionSelector
from core.base_page import BasePage
from locators.header_locators import HeaderLocators


class HeaderComponent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.region_selector = RegionSelector(driver)

    def click_region(self):
        """
        Клик по региону справа сверху
        :return:
        """
        self.click(HeaderLocators.regions)
        return self

    def current_region(self):
        """
        :return: текущий регион
        """
        return self.find(HeaderLocators.regions).text
