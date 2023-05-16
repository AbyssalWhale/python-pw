import pytest
from playwright.sync_api import expect

from Models.API.Routes.games_routes import get_games
from Models.API.Routes.genre_routes import get_all_genres, get_genre


@pytest.mark.regression
@pytest.mark.parametrize("game_genre_name", ["Action"])
def test_game_category_can_be_selected(set_up, api_request_context, game_genre_name):
    home_page = set_up

    # Arrange Gather Genre Info
    test_genre = get_genre(api_request_context=api_request_context, genre_name=game_genre_name)
    genre_games_api = get_games(api_request_context=api_request_context, genre_id=test_genre['id'])["results"]

    # Act - Sort on UI
    with home_page.p_Page.expect_response(f"**/api/games**&genres=**") as response_info:
            home_page.genre_component.click_genre_button(genreName=test_genre['name'])
    assert response_info.value.ok
    genre_games = response_info.value.json()

    # Assert
    for game in genre_games_api:
        expect(home_page.table_component.get_game_cards_amount(card_title=game['name'])).to_have_count(1)
