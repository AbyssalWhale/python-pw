import pytest
from playwright.sync_api import expect

import conftest
from models.API.Routes.games_routes import get_games
from models.API.Routes.genre_routes import get_genre

@pytest.mark.regression
@pytest.mark.parametrize("game_genre_name", ["Action", "Card"])
def test_game_category_can_be_selected(set_up, api_request_context, game_genre_name):
    home_page = conftest.home_page

    # Arrange Gather Genre Info
    test_genre = get_genre(genre_name=game_genre_name)
    genre_games_api = get_games(genre_id=test_genre['id'])["results"]

    # Act - Sort on UI
    home_page.genre_component.click_genre_button(genreName=test_genre['name'])

    # Assert
    for game in genre_games_api:
        expect(home_page.table_component.get_game_cards_amount(card_title=game['name'])).to_have_count(1)
