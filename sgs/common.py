"""
Shared functions.
"""
import functools
import locale
import os
import re
from datetime import datetime
from typing import Union


LRU_CACHE_SIZE = 32
MAX_ATTEMPT_NUMBER = 5


@functools.lru_cache(maxsize=365)
def to_datetime(date_string: str, language: str) -> Union[datetime, str]:
    """ Converts a date string to a datetime object """

    yyyy = "[0-9]{4}"
    mmm_yyyy = r"[a-z]{3}/[0-9]{4}"

    if re.match(yyyy, date_string):
        date = datetime(int(date_string), 12, 31)
    elif re.match(mmm_yyyy, date_string):
        month_text, year_text = date_string.split("/")
        months = [
            ("jan", "jan"), ("fev", "feb"), ("mar", "mar"),
            ("abr", "apr"), ("mai", "may"), ("jun", "jun"),
            ("jul", "jul"), ("ago", "aug"), ("set", "sep"),
            ("out", "oct"), ("nov", "nov"), ("dez", "dec")
        ]
        for n, month_names in enumerate(months, 1):
            if month_text in month_names:
                month_number = n
                break
        date = datetime(int(year_text), month_number, 1)
    else:
        try:
            day, month, year = [int(date_part) for date_part in date_string.split("/")]
            date = datetime(year, month, day)
        except ValueError:
            # return the original value if we cant parse it
            return date_string
    return date
