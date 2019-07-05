from enum import Enum, unique
import functools
from typing import Union, Optional

import requests
from retrying import retry
import pandas as pd

from .common import LRU_CACHE_SIZE, MAX_ATTEMPT_NUMBER, to_datetime


@unique
class Language(Enum):
    pt = "pt"
    en = "en"


@unique
class SearchURL(Enum):
    pt = "https://www3.bcb.gov.br/sgspub/index.jsp?idIdioma=P"
    en = "https://www3.bcb.gov.br/sgspub/"


@unique
class SearchMethod(Enum):
    code = "localizarSeriesPorCodigo"
    text = "localizarSeriesPorTexto"


@unique
class Columns(Enum):
    pt = {
        "start": "Início  dd/MM/aaaa",
        "last": "Últ. valor",
        "code": "Cód.",
        "frequency": "Per.",
        "name": "Nome completo",
        "source": "Fonte",
        "unit": "Unid.",
    }

    en = {
        "start": "Start  dd/MM/yyyy",
        "last": "Last value",
        "code": "Code",
        "frequency": "Per.",
        "name": "Full name",
        "source": "Source",
        "unit": "Unit",
    }


def init_search_session(language: str) -> requests.Session:
    """
    Starts a session on SGS and get cookies requesting the initial page.

    Parameters

    language: str, "en" or "pt"
        Language used for search and results.
    """
    session = requests.Session()
    search_url = SearchURL[language].value
    session.get(search_url)
    return session


def parse_search_response(response, language: str) -> Optional[list]:
    HTML = response.text

    not_found_msgs = ("No series found", "Nenhuma série localizada")
    if any(msg in HTML for msg in not_found_msgs):
        return None

    cols = Columns[language].value
    START = cols["start"]
    LAST = cols["last"]

    try:
        df = pd.read_html(HTML, attrs={"id": "tabelaSeries"}, flavor="lxml")[0]
        df[START] = df[START].map(lambda x: to_datetime(x, language))
        df[LAST] = df[LAST].map(lambda x: to_datetime(x, language))
        col_names = {
            cols["code"]: "code",
            cols["name"]: "name",
            cols["frequency"]: "frequency",
            cols["unit"]: "unit",
            cols["start"]: "first_value",
            cols["last"]: "last_value",
            cols["source"]: "source",
        }
        df.rename(columns=col_names, inplace=True)
        cols = [
            "code",
            "name",
            "unit",
            "frequency",
            "first_value",
            "last_value",
            "source",
        ]
        df = df[cols]
    except (IndexError, KeyError):
        return None
    else:
        return df.to_dict(orient="records")


@retry(stop_max_attempt_number=MAX_ATTEMPT_NUMBER)
@functools.lru_cache(maxsize=32)
def search_ts(query: Union[int, str], language: str) -> Optional[list]:
    """Search for time series and return metadata about it.

    :param query: code(int) or name(str) used to search for a time serie.
    :param language: string (en or pt) used in query and return results.

    :return: List of results matching the search query.
    :rtype: list_

    Usage::

        >>> results = sgs.search_ts("gold", language="en")
        >>> len(results)
        29
        >>> results[0]
        {'code': 4, 'name': 'BM&F Gold - gramme', 'unit': 'c.m.u.',
        'frequency': 'D', 'first_value': Timestamp('1989-12-29 00:00:00'),
        'last_value': Timestamp('2019-06-27 00:00:00'), 'source': 'BM&FBOVESPA'}
    """

    session = init_search_session(language)
    URL = "https://www3.bcb.gov.br/sgspub/localizarseries/" "localizarSeries.do"

    if isinstance(query, int):
        search_method = SearchMethod.code
    elif isinstance(query, str):
        search_method = SearchMethod.text
    else:
        raise ValueError("query must be an int or str: ({})".format(query))

    url = URL.format(search_method.value)

    params = {
        "method": search_method.value,
        "periodicidade": 0,
        "codigo": None,
        "fonte": 341,
        "texto": None,
        "hdFiltro": None,
        "hdOidGrupoSelecionado": None,
        "hdSeqGrupoSelecionado": None,
        "hdNomeGrupoSelecionado": None,
        "hdTipoPesquisa": 4,
        "hdTipoOrdenacao": 0,
        "hdNumPagina": None,
        "hdPeriodicidade": "Todas",
        "hdSeriesMarcadas": None,
        "hdMarcarTodos": None,
        "hdFonte": None,
        "hdOidSerieMetadados": None,
        "hdNumeracao": None,
        "hdOidSeriesLocalizadas": None,
        "linkRetorno": "/sgspub/consultarvalores/telaCvsSelecionarSeries.paint",
        "linkCriarFiltros": "/sgspub/manterfiltros/telaMfsCriarFiltro.paint",
    }

    if search_method == SearchMethod.code:
        params["codigo"] = query
    else:
        params["texto"] = query
        params["hdTipoPesquisa"] = 6

    response = session.post(url, params=params, timeout=10)
    response.raise_for_status()

    results = parse_search_response(response, language)

    session.close()

    return results
