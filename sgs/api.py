import functools
from typing import Union, List, Dict

import pandas as pd
import requests
from retrying import retry

from .common import LRU_CACHE_SIZE, MAX_ATTEMPT_NUMBER, to_datetime



@retry(stop_max_attempt_number=MAX_ATTEMPT_NUMBER)
@functools.lru_cache(maxsize=LRU_CACHE_SIZE)
def get_data(ts_code: int, begin: str, end: str, strict: bool = False) -> List:
    """
    Requests time series data from the SGS API in json format.
    """

    url = (
        "http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}"
        "/dados?formato=json&dataInicial={}&dataFinal={}"
    )
    request_url = url.format(ts_code, begin, end)
    response = requests.get(request_url)
    
    if strict:
        data = enforce_integrity(response.json(), begin, end)
    else:
        data = response.json()
    
    return data
    
def enforce_integrity(data_from_sgs: list, start: str, end: str) -> List:
    """
    Enforce integrity
    
    SGS API default behaviour returns the last stored value when selected period have no data.

    It is possible to catch this behaviour when the first record date precedes the start date.
    
    This function enforces an empty data set when the first record date precedes the start date.
    
    :param data_from_sgs: List containing data from sgs.
    :param start: start date (DD/MM/YYYY).
    :param end: end date (DD/MM/YYYY).
  
    :return: List containing data from sgs or an empty list
    :rtype: list

    """

    first_record_date = to_datetime(data_from_sgs[0]["data"], "pt")
    period_start_date = to_datetime(start, 'pt')

    is_out_of_range =  first_record_date < period_start_date
    
    if is_out_of_range:
        ts_data = []
    else:
        ts_data = data_from_sgs
    
    return ts_data
