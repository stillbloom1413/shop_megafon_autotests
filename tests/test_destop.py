import time
from dataclasses import asdict

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
        ids=lambda data: data.group if hasattr(data, "group") else str(data),
    )
    def test_catalog_filters(self, page_factory, filter_data, url):
        filter_dict = asdict(filter_data)
        page = page_factory(CatalogPage, url=url)
        filter_type, group_name, value, boundary = (
            filter_dict.get("filter_type"),
            filter_dict.get("group"),
            filter_dict.get("value"),
            filter_dict.get("boundary"),
        )
        final_value = value[0] if isinstance(value, list) else value
        final_boundary = boundary[0] if isinstance(boundary, list) else boundary

        page.click_filter(
            filter_type=filter_type,
            group_name=group_name,
            value=final_value,
            boundary=final_boundary,
        ).apply_or_discard_filter(value="Применить фильтры").select_first_product()
        time.sleep(2)
