from conftest import authentication_key


def get_games(api_request_context, genre_id=None, assert_response_code=True):

    headers_local = authentication_key
    if genre_id is not None:
        headers_local.update({"genres": genre_id})

    response = api_request_context.get("games", params=headers_local)
    if assert_response_code:
        assert response.ok
    result = response.json()

    return result
