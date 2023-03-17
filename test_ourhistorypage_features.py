import re
from playwright.sync_api import Playwright, Page, expect
import pytest
from Models.POM.HomePage import HomePage
import pytest

def test_aboutuspage_canbeopened(set_up):
    home_Page = set_up
    aboutUsPage = home_Page.Click_MoreAboutUs_Button()
    

    #Assert
    expect(aboutUsPage.label_ourStory).to_be_visible()