import pytest
from tests.data.load_data import load_data


class TestDesktop:

    @pytest.mark.parametrize(
        "name, result",
        load_data("regions").items(),
        ids=list(load_data("regions").keys()),
    )
    def test_region_change(self, main_page, name, result):
        page = (
            main_page.navigate()
            .header.click_first_region()
            .region_selector.input_region_name(region_name=name)
            .click_first_region()
        )
        assert result.lower() in page.header.current_region().lower()
