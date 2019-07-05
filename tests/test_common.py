from datetime import datetime

import pytest
from sgs.common import to_datetime


@pytest.mark.common
@pytest.mark.parametrize("language", ["pt", "en"])
def test_to_datetime_dd_mm_aaaaa(language):
    date_string = "01/01/2018"
    expected = datetime(day=1, month=1, year=2018)
    assert to_datetime(date_string, language) == expected


@pytest.mark.common
@pytest.mark.parametrize(
    "date_string,language", [("mai/2018", "pt"), ("may/2018", "en")]
)
def test_to_datetime_mmm_aaaaa(date_string, language):
    expected = datetime(day=1, month=5, year=2018)
    assert to_datetime(date_string, language) == expected
