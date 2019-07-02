import functools
from typing import Union, List, Dict

import pandas as pd
import requests
from retrying import retry

from .common import LRU_CACHE_SIZE, MAX_ATTEMPT_NUMBER


@retry(stop_max_attempt_number=MAX_ATTEMPT_NUMBER)
@functools.lru_cache(maxsize=LRU_CACHE_SIZE)
def get_data(ts_code: int, begin: str, end: str) -> List:
    """
    Requests time series data from the SGS API in json format.
    """

    url = (
        "http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}"
        "/dados?formato=json&dataInicial={}&dataFinal={}"
    )
    request_url = url.format(ts_code, begin, end)
    response = requests.get(request_url)
    return response.json()
