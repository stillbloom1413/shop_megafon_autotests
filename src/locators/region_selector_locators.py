from selenium.webdriver.common.by import By


class RegionsLocators:
    """Локаторы попапа выбора региона"""

    region_search = (
        By.XPATH,
        "//label[contains(text(), 'Поиск региона')]/following-sibling::input",
    )

    region = (By.XPATH, "//p[contains(text(), '{region}')]")

    first_region_in_search = (By.CSS_SELECTOR, "[role='option']:first-child")
