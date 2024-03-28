import conftest


def get_all_genres(assert_response_code=True):
    headers_local = conftest.test_run_config
    response = conftest.api_request_context.get("genres", params=headers_local)
    if assert_response_code:
        assert response.ok
    result = response.json()

    return result


def get_genre(genre_name: str):
    all_genres = get_all_genres()["results"]
    result = None

    for genre in all_genres:
        if genre['name'] == genre_name:
            result = genre

    return result
