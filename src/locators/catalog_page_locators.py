from selenium.webdriver.common.by import By

class CatalogPageLocators:
    price_input = (By.XPATH, "//div[contains(text(), 'Цена')]/ancestor::div[contains(@class, 'Accordion_background')]/following-sibling::div//input")
    receipt_any = (By.XPATH,"//span[contains(text(),'Любой')]")
    receipt_today = (By.XPATH,"//span[contains(text(),'Сегодня')]")
    receipt_preorder = (By.XPATH, "//span[contains(text(),'Предзаказ')]")
    promotions_and_discounts = (By.XPATH, "//div[contains(text(),'Акции и скидки')]/following-sibling::label/input")
    pick_up = (By.XPATH, "//div[contains(@class, 'CheckboxListFilter')]//span[text()='Самовывоз']")
    delivery = (By.XPATH, "//div[contains(@class, 'CheckboxListFilter')]//span[text()='Доставка']")
    apple_check_box = (By.XPATH, "//div[contains(@class, 'CheckboxListFilter_values')]//span[text()='Apple']")
    colour_btn = (By.XPATH,"//div[contains(text(),'Цвет')]")
    internal_storage_capacity_btn = (By.XPATH, "//div[contains(text(),'Объем встроенной памяти')]")
    ram_btn = (By.XPATH, "//div[contains(text(),'Объем оперативной памяти (ГБ)')]")
    sim_btn = (By.XPATH, "//div[contains(text(),'Формат СИМ')]")
    esim_btn = (By.XPATH, "//div[contains(text(),'Поддержка еСИМ')]")
    battery_btn = (By.XPATH, "//div[contains(text(),'Емкость аккумуляторной батареи (мАч)')]")
    display_size_btn = (By.XPATH, "//div[contains(text(),'Диагональ дисплея (дюймов)')]")
    display_type_btn = (By.XPATH, "//div[contains(text(),'Тип дисплея')]")
    nfc_support_btn = (By.XPATH, "//div[contains(text(),'Наличие NFC')]")
    g_support_btn = (By.XPATH, "//div[contains(text(),'Поддержка 5G')]")
    camera_modules_btn = (By.XPATH, "//div[contains(text(),'Количество модулей основной камеры')]")
    camera_resolution_btn = (By.XPATH, "//div[contains(text(),'Максимальное разрешение основной камеры (Mpix)')]")
    fast_charging_btn = (By.XPATH, "//div[contains(text(),'Функция быстрой зарядки')]")
    Discounted_btn = (By.XPATH, "//div[contains(text(),'Уцененный товар')]")
    # TODO написать фабрику локаторов т.к. они почти все одинаковые
    # TODO нужен файл конфиг, оттуда будем тащить значения в параметризованный тест и вызывать соответствующий локатор