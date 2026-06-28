import time
import pytest

from utils.config_loader import ConfigLoader


def _authorize_driver(driver):
    cookies = ConfigLoader.get_auth_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)

    time.sleep(1)
    driver.refresh()


@pytest.fixture(scope="function")
def page_factory(driver):

    def _create_page(page_class, url="", authorized=False):

        if authorized:
            driver.get(driver.base_url)
            _authorize_driver(driver)

        page = page_class(driver)

        page.open(url)

        return page

    return _create_page
