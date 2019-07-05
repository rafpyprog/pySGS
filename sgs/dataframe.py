"""
Dataframe
"""
from typing import Dict, List, Tuple, Union

import pandas as pd

from . import api
from . import search
from .ts import time_serie


def dataframe(ts_codes: Union[int, List, Tuple], start: str, end: str) -> pd.DataFrame:
    """
    Creates a dataframe from a list of time serie codes.

    :param ts_codes: single code or list/tuple of time series codes.
    :param start: start date (DD/MM/YYYY).
    :param end: end date (DD/MM/YYYY).

    :return: Pandas dataframe.
    :rtype: pandas.DataFrame_

    Usage::

        >>> CDI = 12
        >>> INCC = 192  #  National Index of Building Costs
        >>> df = sgs.dataframe([CDI, INCC], start='02/01/2018', end='31/12/2018')
        >>> df.head()
                         12    192
        2018-01-01       NaN  0.31
        2018-01-02  0.026444   NaN
        2018-01-03  0.026444   NaN
        2018-01-04  0.026444   NaN
        2018-01-05  0.026444   NaN

    """
    if isinstance(ts_codes, int):
        ts_codes = [ts_codes]

    series = []
    for code in ts_codes:
        ts = time_serie(code, start, end)
        series.append(ts)

    df = pd.concat(series, axis=1)
    return df
