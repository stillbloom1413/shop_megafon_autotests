import time

import pytest

def test_simple(driver,url):
    driver.get(url)
    time.sleep(5)