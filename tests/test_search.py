import pytest
import requests

from sgs.search import *


@pytest.mark.parametrize("language", ["en", "pt"])
def test_init_search_session(language):
    session = init_search_session(language)
    assert isinstance(session, requests.Session)


@pytest.mark.parametrize(
    "query,language,expected",
    [
        (4, "pt", {"name": "Ouro BM&F - grama"}),
        (4, "en", {"name": "BM&F Gold - gramme"})
    ],
)
def test_search_by_code(query, language, expected):
    results = search_serie(query, language)
    assert isinstance(results, list)
    assert results[0]["frequency"] == "D"
    assert results[0]["name"] == expected["name"]
    first_value = pd.to_datetime('29/12/1989', dayfirst=True)
    assert results[0]["first_value"] == first_value
