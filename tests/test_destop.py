import time

import pytest

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from utils.config_loader import ConfigLoader


class TestDesktop:

    @pytest.mark.parametrize(
        "name, result",
        ConfigLoader.get_regions().items(),
        ids=list(ConfigLoader.get_regions().keys()),
    )
    def test_region_change(self, page_factory, name, result):
        page = (
            page_factory(MainPage)
            .header.click_first_region()
            .region_selector.input_region_name(region_name=name)
            .click_first_region()
        )
        assert result.lower() in page.header.current_region().lower()

    @pytest.mark.parametrize(
        "url, filter_data",
        ConfigLoader.get_catalog_test_data(section_name="Смартфоны"),
        ids=lambda data: data.group if hasattr(data, 'group') else str(data)
    )
    def test_catalog_filters(self, page_factory, filter_data, url):
        page = page_factory(CatalogPage, url=url)
        time.sleep(4)

