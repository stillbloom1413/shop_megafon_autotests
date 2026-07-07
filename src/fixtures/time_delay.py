import time
import pytest

@pytest.fixture(autouse=True)
def delay_between_tests():
    """Добавляет задержку в 5 секунд после каждого теста"""
    yield
    time.sleep(5)