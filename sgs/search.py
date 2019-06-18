from enum import Enum, unique
from typing import Union, Optional

import requests
import pandas as pd

from .common import to_datetime


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
    Starts a session on SGS requesting the initial page.

    Parameters
    ----------
    language: str, "en" or "pt"
        Language used for search and results.
    """
    session = requests.Session()
    search_url = SearchURL[language].value
    session.get(search_url)
    return session


def parse_search_response(response, language: str) -> Optional[list]:
    HTML = response.text
    cols = Columns[language].value
    START = cols["start"]
    LAST = cols["last"]

    try:
        df = pd.read_html(HTML, attrs={"id": "tabelaSeries"}, flavor='lxml')[0]
        print(df.columns)
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
    except IndexError:
        return None
    else:
        return df.to_dict(orient="records")


def search_serie(query: Union[int, str], language: str) -> Optional[list]:
    """
    Search for time series on SGS and return metadata about it.

    Parameters
    ----------
    query: int or str
        Time serie code or name for search.
    language: str, "en" or "pt"
        Language used for search and results.
    """

    session = init_search_session(language)
    URL = ("https://www3.bcb.gov.br/sgspub/localizarseries/"
           "localizarSeries.do?method={}")

    if isinstance(query, int):
        search_method = SearchMethod.code
    elif isinstance(query, str):
        search_method = SearchMethod.text
    else:
        raise ValueError('query must be an int or str: ({})'.format(query))

    url = URL.format(search_method.value)

    params = {
        "periodicidade": 0,
        "codigo": "",
        "fonte": 341,
        "texto": "",
        "hdFiltro": "",
        "hdOidGrupoSelecionado": "",
        "hdSeqGrupoSelecionado": "",
        "hdNomeGrupoSelecionado": "",
        "hdTipoPesquisa": 4,
        "hdTipoOrdenacao": 0,
        "hdNumPagina": "",
        "hdPeriodicidade": "Todas",
        "hdSeriesMarcadas": "",
        "hdMarcarTodos": "",
        "hdFonte": "",
        "hdOidSerieMetadados": "",
        "hdNumeracao": "",
        "hdOidSeriesLocalizadas": "",
        "linkRetorno":
            "/sgspub/consultarvalores/telaCvsSelecionarSeries.paint",
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
    return results
