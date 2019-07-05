"""
Shared functions.
"""
from datetime import datetime
import locale
from typing import Union


LRU_CACHE_SIZE = 32
MAX_ATTEMPT_NUMBER = 5


def to_datetime(date_string: str, language: str) -> Union[datetime, str]:
    """ Converts a date string to a datetime object """
    locales = {"pt": "pt_BR.utf-8", "en": "en_US.utf-8"}

    locale.setlocale(locale.LC_TIME, locales[language])

    dd_mm_aaaa = "%d/%m/%Y"
    mmm_aaaa = "%b/%Y"
    try:
        date = datetime.strptime(date_string, dd_mm_aaaa)
    except ValueError:
        try:
            date = datetime.strptime(date_string, mmm_aaaa)
        except ValueError:
            return date_string  # ignore errors and return original value
    return date
