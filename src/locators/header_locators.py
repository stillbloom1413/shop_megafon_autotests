from selenium.webdriver.common.by import By


class HeaderLocators:
    """
    Локаторы хедера
    """

    # Локаторы справа от лого мегафона
    logo = (
        By.CSS_SELECTOR,
        "[data-sentry-component='BaseMenu'] > div > [data-sentry-element='Link']",
    )
    private_individuals = (
        By.XPATH,
        "//ul[contains(@class,  'BaseMenu')]/li/a/span[contains(text(),'Частным лицам')]",
    )
    internet_shop = (
        By.XPATH,
        "//ul[contains(@class,  'BaseMenu')]/li/a/span[contains(text(),'Интернет-магазин')]",
    )
    business = (
        By.XPATH,
        "//ul[contains(@class,  'BaseMen')]/li/a/span[contains(text(),'Бизнесу')]",
    )
    for_entrepreneurs = (
        By.XPATH,
        "//ul[contains(@class,  'BaseMen')]/li/a/span[contains(text(),'Предпринимателям')]",
    )
    for_government_customers = (
        By.XPATH,
        "//ul[contains(@class,  'BaseMen')]/li/a/span[contains(text(),'Госзаказчикам')]",
    )

    # Кнопка <Ещё>
    else_btn = (
        By.XPATH,
        "//ul[contains(@class,  'BaseMen')]/div/span[contains(text(),'Еще')]",
    )
    else_btn_telecom_operators = (
        By.XPATH,
        "//a[contains(@class, 'tooltip')]/span[contains(text(),'Операторам связи')]",
    )
    else_btn_about_company = (
        By.XPATH,
        "//a[contains(@class, 'tooltip')]/span[contains(text(),'О компании')]",
    )
    else_btn_work_in_megafon = (
        By.XPATH,
        "//a[contains(@class, 'tooltip')]/span[contains(text(),'Работа в МегаФоне')]",
    )

    # --
    support_icon = (By.CSS_SELECTOR, "div[class^='SupportChatIcon']")
    regions = (
        By.CSS_SELECTOR,
        "div[class*='BaseMenu'] > div[class*='RegionsChangeButton']",
    )
