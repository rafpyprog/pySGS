from datetime import datetime

import pytest
from sgs.common import to_datetime, to_datetime_string, get_series_codes
from sgs.dataframe import dataframe
from sgs.ts import time_serie

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


@pytest.mark.common
def test_to_datetime_aaaaa():
    expected = datetime(day=31, month=12, year=2018)
    date_string = '2018'
    assert to_datetime(date_string, 'pt') == expected

@pytest.mark.common
@pytest.mark.parametrize(
    "input_str, expected", [("01/05/2020", "2020-05-01"),
    ("mai/2020", "2020-05-01"), ("2020", "2020-12-31")]
)
def test_to_datetime_string_pt(input_str, expected):
    assert to_datetime_string(input_str, 'pt') == expected

@pytest.mark.common
def test_to_datetime_string_en():
    expected = "2020-05-01"
    assert to_datetime_string('may/2020', 'en') == expected

@pytest.mark.common
def test_to_datetime_string_full_format():
    expected = "2020-12-31 00:00:00"
    assert to_datetime_string('31/12/2020', 'pt', "%Y-%m-%d %H:%M:%S") == expected

@pytest.mark.common
@pytest.mark.parametrize(
    "input_code", [12, [12], (12), dataframe(12, '01/01/2020', '01/02/2020'),
    time_serie(12, '01/01/2020', '01/02/2020')]
)
def test_get_series_codes(input_code):
    codes = get_series_codes(input_code)
    expected = [12]
    assert codes == expected
    assert isinstance(codes, list)