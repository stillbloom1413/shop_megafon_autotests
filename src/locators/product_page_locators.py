from selenium.webdriver.common.by import By


class ProductPageLocators:

    ALL_CHARACTERISTICS = (By.XPATH, "//button[contains(text(), 'Все характеристики')]")
    TITLE = (By.XPATH, "//h1")
    PRICE = (By.XPATH, "//div[contains(@class, 'PriceAndCreditBlock')]"
                       "//div[contains(@class, 'Price_text')]"
                       "//span[contains(@role, 'presentation')]")
    INSTALLMENT = (By.XPATH, "//div[contains(@class, 'PriceAndCreditBlock')]"
                    "//div[contains(text(),'Рассрочка')]")
    PICKUP = (By.XPATH,"(//div[contains(@class, 'DeliveriesGroups')]"
                       "//div[contains(text(), 'Забрать сегодня')])[1]")
    NO_PICKUP = (By.XPATH, "(//div[contains(@class, 'DeliveriesGroups')]"
                           "//button[contains(text(),'в 0 салонаx')])[1]")
    DISCOUNTS_BLOCK = (By.XPATH,"//div[contains(@class, 'DiscountsBlock')]")

    @classmethod
    def characteristics_locators(cls, characteristic):
        xpath = (f"//p[contains(text(), '{characteristic}')]"
                 f"/ancestor::div[contains(@class, 'Specifications_name')]"
                 f"/following-sibling::div")
        return By.XPATH, xpath

    @classmethod
    def colour_locators(cls, value):
        xpath = f"(//div[contains(text(), '{value}')]/following-sibling::p)[1]"
        return By.XPATH, xpath

    @classmethod
    def section_locators(cls, value):
        xpath = (f"//a/div[contains(@data-testid, 'core-title') "
                 f"and contains(text(), '{value}')]")
        return By.XPATH, xpath