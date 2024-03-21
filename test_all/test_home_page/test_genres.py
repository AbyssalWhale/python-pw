import pytest
from playwright.sync_api import expect

import conftest
from Models.API.Routes.games_routes import get_games
from Models.API.Routes.genre_routes import get_genre

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


class TestGenresA(conftest.Fixtures):
    @pytest.mark.asyncio
    @pytest.mark.regression
    @pytest.mark.parametrize("genre_under_test", ["Action", "Card"])
    async def test_game_category_can_be_selected_async(self, set_up_home_page, set_up_api, genre_under_test):
        self.set_up_home_page = await set_up_home_page
        self.set_up_api = await set_up_api

        # gather genre info
        genres_response = await self.set_up_api.api_request_context.get("genres", params=self.set_up_api.api_headers)
        assert genres_response.ok
        genres_data = await genres_response.json()
        genres_data = genres_data["results"]
        genre_data = next((genre for genre in genres_data if genre['name'] == genre_under_test), None)

        # gather games info
        params = self.set_up_api.api_headers
        params.update({"genres": genre_data["id"]})
        games_response = await self.set_up_api.api_request_context.get("genres", params=params)
        assert games_response.ok
        games_data = await games_response.json()
        games_data = games_data["results"]

        # sort on UI
        await self.set_up_home_page.home_page.genre_component.click_genre_button(genre_name=genre_data["name"])

        # Assert
        for game in games_data:
            actual_game_cards = await self.set_up_home_page.home_page.table_component.get_game_cards_amount(
                card_title=game['name'])
            expect(actual_game_cards).to_have_count(1)
