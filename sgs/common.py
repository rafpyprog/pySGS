"""
Shared functions.
"""
from datetime import datetime
import locale
import re
from typing import Union


LRU_CACHE_SIZE = 32
MAX_ATTEMPT_NUMBER = 5


def to_datetime(date_string: str, language: str) -> Union[datetime, str]:
    """ Converts a date string to a datetime object """
    locales = {"pt": "pt_BR.utf-8", "en": "en_US.utf-8"}

    locale.setlocale(locale.LC_TIME, locales[language])

    dd_mm_aaaa = "%d/%m/%Y"
    mmm_aaaa = "%b/%Y"

    formats = [dd_mm_aaaa, mmm_aaaa]

    for fmt in formats:
        try:
            date = datetime.strptime(date_string, fmt)
            break
        except ValueError:
            continue
    else:
        yyyy = "[0-9]{4}"
        if re.match(yyyy, date_string):
            year = int(date_string)
            month = 12
            day = 31
            date = datetime(year, month, day)
        else:
            return date_string  # returns original value if cant parse

    return date
