from conftest import authentication_key


def get_all_genres(api_request_context, assert_response_code=True):
    headers_local = authentication_key
    response = api_request_context.get("genres", params=headers_local)
    if assert_response_code:
        assert response.ok
    result = response.json()

    return result


def get_genre(api_request_context, genre_name: str):
    all_genres = get_all_genres(api_request_context)["results"]
    result = None

    for genre in all_genres:
        if genre['name'] == genre_name:
            result = genre

    return result
