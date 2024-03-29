from playwright.sync_api import Playwright, Page, expect
import pytest

import conftest


@pytest.mark.regression
@pytest.mark.parametrize("game_to_search", ["The Witcher", "Destiny"])
def test_game_can_be_searched(set_up, game_to_search):
        home_page = conftest.home_page
        home_page.search_component.input_search_field(game_to_search)

        # Assert
        expect(home_page.table_component.get_cards_titles()).to_contain_text([game_to_search])
