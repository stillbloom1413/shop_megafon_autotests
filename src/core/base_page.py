import time
from typing import Self

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class BasePage(object):
    """
    Каркас страницы для наследования
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5, poll_frequency=0.5)

    def open(self, path=""):
        """Открытие страницы"""
        self.driver.get(f"{self.driver.base_url}{path}")

    def find(self, locator):
        """Поиск элемента"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_element_present(self, locator):
        """Проверка наличия элемента на странице"""
        try:
            WebDriverWait(self.driver, 2, poll_frequency=0.5).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False


    def click(self, locator):
        """Клик по элементу с защитой от StaleElementReferenceException"""
        for attempt in range(3):
            try:
                self.wait.until(EC.element_to_be_clickable(locator)).click()
                return
            except StaleElementReferenceException:
                if (
                    attempt == 2
                ):
                    raise
                time.sleep(0.2)

    def input_text(self, locator, text):
        """Ввод текста"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator: tuple) -> Self:
        """Скроллит страницу до указанного элемента, чтобы он стал видимым"""
        for attempt in range(3):
            try:
                element = self.find(locator)
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                return self
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
                time.sleep(0.2)


    def get_text(self, locator):
        """Извлечение текста из элемента"""
        element = self.find(locator)
        return element.text