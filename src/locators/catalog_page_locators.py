from selenium.webdriver.common.by import By


class CatalogPageLocators:

    FIRST_PRODUCT = (
        By.XPATH,
        "//div[contains(@class, 'CardList_grid')]/div[1]/div/a[1]",
    )

    @classmethod
    def accordion_locator(cls, group_name: str) -> tuple:
        """
        Локатор групп фильтров
        :param group_name: группа фильтров
        :return: локатор
        """
        return By.XPATH, f"//div[contains(text(),'{group_name}')]"

    @classmethod
    def range_input_in_group(cls, group_name: str, boundary: str) -> tuple:
        """
        Локатор импутов "от" и "до"
        :param group_name: группа фильтров
        :param boundary: граница
        :return: локатор
        """
        xpath = (
            f"//div[contains(text(), '{group_name}')]"
            f"/ancestor::div[contains(@class, 'Accordion_wrapper')]"
            f"//input[@name='{boundary}']"
        )
        return By.XPATH, xpath

    @classmethod
    def exact_value_in_group(cls, group_name: str, value: str) -> tuple:
        """
        Локатор чекбоксов
        :param group_name: группа фильтров
        :param value: значение
        :return: локатор
        """
        xpath = (
            f"//div[contains(text(), '{group_name}')]"
            f"/ancestor::div[contains(@class, 'Accordion_wrapper')]"
            f"//span[text()='{value}']"
        )
        return By.XPATH, xpath

    @classmethod
    def standalone_switch(cls, group_name: str) -> tuple:
        """
        Локатор свича
        :param group_name: группа фильтров
        :return: локатор
        """
        xpath = (
            f"(//div[contains(text(), '{group_name}')]"
            f"/ancestor::div[contains(@class, 'ToggleFilter')]"
            f"//span)[2]"
        )
        return By.XPATH, xpath

    @classmethod
    def button_locator(cls, value: str) -> tuple:
        """
        Локатор кнопок
        :param value: наименование кнопки
        :return: локатор
        """
        xpath = f"//button[contains(text(),'{value}')]"
        return By.XPATH, xpath
