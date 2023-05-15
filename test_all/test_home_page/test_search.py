from playwright.sync_api import Playwright, Page, expect
import pytest
from Models.POM.HomePage import HomePage
import pytest


@pytest.mark.regression
@pytest.mark.parametrize("game_to_search", ["Grand Theft Auto", "The Witcher"])
def test_game_can_be_searched(set_up, game_to_search):
    home_page = set_up
    home_page.search_component.Input_Search_Field(game_to_search)

    # Assert
    expect(home_page.table_component.Get_CardsTitles()).to_contain_text([game_to_search])
