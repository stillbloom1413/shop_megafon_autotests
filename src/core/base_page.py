from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5, poll_frequency=0.5)

    def open(self, path=""):
        """Открытие страницы"""
        self.driver.get(f"{self.driver.base_url}{path}")

    def find(self, locator):
        """Поиск элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self,locator):
        """Клик по элементу"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self,locator,text):
        """Ввод текста"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)
    