from playwright.sync_api import Playwright, Page, expect
import pytest

import conftest


@pytest.mark.regression
@pytest.mark.parametrize("game_to_search", ["Grand Theft Auto", "The Witcher"])
def test_game_can_be_searched(set_up, game_to_search):
        home_page = conftest.home_page
        home_page.search_component.input_search_field(game_to_search)

        # Assert
        expect(home_page.table_component.Get_CardsTitles()).to_contain_text([game_to_search])
