import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"

    driver = WebDriver(options=options)

    yield driver

    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--region", action="store", default="moscow", help="Specify the region")

@pytest.fixture(scope="session")
def url(request):
    region = request.config.getoption("--region")
    return f"https://{region}.shop.megafon.ru"