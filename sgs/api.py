import datetime
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


@retry(stop_max_attempt_number=MAX_ATTEMPT_NUMBER)
@functools.lru_cache(maxsize=LRU_CACHE_SIZE)
def get_data_olinda(resource: str, begin: str, end: Union[None, str]) -> List:
    """
    Requests data frames from the BCB Olinda API in json format.
    """
    # resource names
    names = {
        'monthly': 'ExpectativaMercadoMensais',
        'quarterly': 'ExpectativaMercadoTrimestrais',
        'yearly': 'ExpectativaMercadoAnuais',
        'infl12m': 'ExpectativasMercadoInflacao12Meses',
        'monthlytop5': 'ExpectativasMercadoTop5Mensais',
        'yearlytop5': 'ExpectativasMercadoTop5Anuais',
        'inst': 'ExpectativasMercadoInstituicoes'
        }

    # TODO: Olinda API expects ISO dates
    begin_iso = datetime.datetime.strptime(begin, '%d/%m/%Y').strftime('%Y-%m-%d')
    end_iso = datetime.datetime.strptime(end, '%d/%m/%Y').strftime('%Y-%m-%d')

    url = (
        "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/"
        "{}?$filter=Data%20ge%20'{}'%20and%20Data%20le%20'{}'&"
        "$orderby=Data%20asc&$format=json"
    )

    request_url = url.format(names[resource], begin_iso, end_iso)
    response = requests.get(request_url)
    return response.json()
