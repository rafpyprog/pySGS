"""
Shared functions.
"""
from datetime import datetime
from typing import Union, List, Tuple
import locale
import pandas as pd
import os


LRU_CACHE_SIZE = 32
MAX_ATTEMPT_NUMBER = 5


def to_datetime(date_string: str, language: str) -> datetime:

    """ correct problem with locale in Windows platform """
    if os.name == 'nt':
        locales = {"pt": "Portuguese_Brazil.1252", "en": "Portuguese_Brazil.1252"}
    else:
        locales = {"pt": "pt_BR.utf-8", "en": "en_US.utf-8"}

    locale.setlocale(locale.LC_TIME, locales[language])

    dd_mm_aaaa = "%d/%m/%Y"
    mmm_aaaa = "%b/%Y"
    aaaa = "%Y"

    formats = [dd_mm_aaaa, mmm_aaaa, aaaa]

    for fmt in formats:
        try:
            date = datetime.strptime(date_string, fmt)
            if fmt == aaaa:
                date = date.replace(day=31, month=12)
            break
        except ValueError:
            continue
    else:
        raise ValueError
    return date


def to_datetime_string(date_string: str, language: str, strformat: str = "%Y-%m-%d") -> str:

    try:
        date = to_datetime(date_string, language).strftime(strformat)
    except ValueError:
        date = date_string
    return date


def get_series_codes(code_input: Union[int, List, Tuple, pd.DataFrame, pd.Series]) -> List:

    if isinstance(code_input, int):
        codes = [code_input]
    elif isinstance(code_input, pd.Series):
        codes = [code_input.name]
    elif isinstance(code_input, pd.DataFrame):
        codes = list(code_input.columns)
    elif isinstance(code_input, tuple):
        codes = list(code_input)
    else:
        codes = code_input

    return codes
