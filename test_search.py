import re
from playwright.sync_api import Playwright, Page, expect
import pytest
from Models.POM.HomePage import HomePage
import pytest


@pytest.mark.parametrize("gameToSearch", ["Grand Theft Auto", "The Witcher"])
def test_game_canbesearched(set_up, gameToSearch):
    home_Page = set_up
    home_Page.Input_SearchGame_Field(gameName=gameToSearch)

    #Assert
    expect(home_Page.Get_CardsTitles()).to_contain_text([gameToSearch])