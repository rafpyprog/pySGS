import functools
from typing import Union, List, Dict

import pandas as pd
import requests
from retrying import retry

from .common import LRU_CACHE_SIZE, MAX_ATTEMPT_NUMBER, to_datetime


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
    
def get_data_with_strict_range(ts_code: int, begin: str, end: str) -> List:

    """
    Request time series data from the SGS API considering a strict range of dates.
        
    SGS API default behaviour returns the last stored value when selected date range have no data.

    It is possible to catch this behaviour when the first record date precedes the start date.
    
    This function enforces an empty data set when the first record date precedes the start date, avoiding records out of selected range.
    
    :param ts_code: time serie code.
    :param begin: start date (DD/MM/YYYY).
    :param end: end date (DD/MM/YYYY).
  
    :return: Data in json format or an empty list
    :rtype: list

    """
    data = get_data(ts_code, begin, end)
    
    first_record_date = to_datetime(data[0]["data"], "pt")
    period_start_date = to_datetime(begin, 'pt')
    
    try:
        is_out_of_range =  first_record_date < period_start_date  #type: ignore
        if is_out_of_range:
            raise ValueError
    except TypeError:
        print("ERROR: Serie " + str(ts_code) + " - Please, use 'DD/MM/YYYY' format for date strings.")
        data = []
    except ValueError:
        print("WARNING: Serie " + str(ts_code) + " - There is no data for the requested period, but there's previous data.")
        data = []
    
    return data
