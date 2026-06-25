from core.base_page import BasePage
from locators.region_selector_locators import RegionsLocators


class RegionSelector(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def input_region_name(self, region_name):
        self.input_text(RegionsLocators.region_search, region_name)
        return self

    def click_region(self):
        self.click(RegionsLocators.first_region_in_search)
        from pages.main_page import MainPage

        return MainPage(self.driver)
