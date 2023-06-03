import conftest

def get_games(genre_id=None, assert_response_code=True):
    headers_local = conftest.test_run_config
    if genre_id is not None:
        headers_local.update({"genres": genre_id})

    response = conftest.api_request_context.get("games", params=headers_local)
    if assert_response_code:
        assert response.ok
    result = response.json()

    return result
