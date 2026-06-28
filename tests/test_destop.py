import pytest

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
            page_factory(MainPage).header.click_first_region()
            .region_selector.input_region_name(region_name=name)
            .click_first_region()
        )
        assert result.lower() in page.header.current_region().lower()

    def test_catalog_filters(self):
        pass
