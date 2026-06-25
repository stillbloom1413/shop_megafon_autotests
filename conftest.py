import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

pytest_plugins = ["src.fixtures.page_drivers"]


@pytest.fixture(scope="session")
def driver(request):
    region = request.config.getoption("--region")
    base_url = f"https://{region}.shop.megafon.ru"

    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"
    driver = WebDriver(options=options)

    driver.base_url = base_url

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--region", action="store", default="moscow", help="Specify the region"
    )
