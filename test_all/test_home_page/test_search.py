import re
from playwright.sync_api import Playwright, Page, expect
import pytest
from Models.POM.HomePage import HomePage
import pytest

@pytest.mark.regression
@pytest.mark.parametrize("gameToSearch", ["Grand Theft Auto", "The Witcher"])
def test_game_canbesearched(set_up, gameToSearch):
    home_Page = set_up
    home_Page.search_component.Input_Search_Field(gameToSearch)

    #Assert
    expect(home_Page.table_component.Get_CardsTitles()).to_contain_text([gameToSearch])