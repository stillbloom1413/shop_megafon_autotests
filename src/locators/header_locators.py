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
        "//ul[contains(@class,  'BaseMenu')]/li/a/span[contains(text(),'Бизнесу')]",
    )
    for_entrepreneurs = (
        By.XPATH,
        "//ul[contains(@class,  'BaseMenu')]/li/a/span[contains(text(),'Предпринимателям')]",
    )
    for_government_customers = (
        By.XPATH,
        "//ul[contains(@class,  'BaseMenu')]/li/a/span[contains(text(),'Госзаказчикам')]",
    )

    # Кнопка <Ещё>
    upper_else_btn = (
        By.XPATH,
        "//ul[contains(@class,  'BaseMenu')]/div/span[contains(text(),'Еще')]",
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


    # Локаторы на уровне поиска
    catalog_btn = (
        By.CSS_SELECTOR,
        "button[class*='MainMenu_catalog']"
    )

    main_search = (
        By.XPATH,
        "//div[contains(@class, 'MainMenu')]//input"
    )

    compare_btn = (
        By.CSS_SELECTOR,
        "[href='/compare']"
    )

    checkout_btn = (
        By.CSS_SELECTOR,
        "[href='/checkout']"
    )

    authorization_btn = (
        By.XPATH,
        "//button[contains(text(),'Войти')]"
    )

    # самые нижние локаторы в хедере
    promos = (
        By.CSS_SELECTOR,
        "li > [href='/actions']"
    )

    new_items = (
        By.CSS_SELECTOR,
        "li > [href='/mobile/-new_goods']"
    )

    tariffs = (
        By.CSS_SELECTOR,
        "ul[class*='Navigation'] > li > [href='/connect/tariffs']"
    )

    beautiful_numbers = (
        By.CSS_SELECTOR,
        "ul[class*='Navigation'] > li > [href='/connect/chnumber/fullnumber']"
    )

    number_transfer = (
        By.XPATH,
        "//li//span[contains(text(),'Перенос номера')]"
    )

    esim = (
        By.CSS_SELECTOR,
        "li > [href='/connect/esim']"
    )

    modems_routers = (
        By.CSS_SELECTOR,
        "ul[class*='Navigation'] > li > [href='/modems_routers']"
    )

    credit_installments = (
        By.CSS_SELECTOR,
        "ul[class*='Navigation'] > li > [href='/credit-and-installments']"
    )

    # Кнопка <Ещё>

    lower_else_btn = (
        By.XPATH,
        "//ul[contains(@class,  'Header_navigationList')]/div/span[contains(text(),'Еще')]"
    )

    else_btn_digital_content = (
        By.CSS_SELECTOR,
        "ul[class*='Navigation_tooltip'] > li > [href='/digital_content']"
    )

    else_btn_insurance_products = (
        By.CSS_SELECTOR,
        "ul[class*='Navigation_tooltip'] > li > [href='/insurance_products ']"
    )