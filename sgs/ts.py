"""
Time Serie manipulation
"""
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from . import api
from . import search
from .common import to_datetime


def time_serie(ts_code: int, start: str, end: str, strict: bool = False) -> pd.Series:
    """
    Request a time serie data.

    :param ts_code: time serie code.
    :param start: start date (DD/MM/YYYY).
    :param end: end date (DD/MM/YYYY).
    :param strict: boolean to enforce a strict date range.

    :return: Time serie values as pandas Series indexed by date.
    :rtype: pandas.Series_

    Usage::

        >>> CDI = 12
        >>> ts = sgs.time_serie(CDI, start='02/01/2018', end='31/12/2018')
        >>> ts.head()
        2018-01-02    0.026444
        2018-01-03    0.026444
        2018-01-04    0.026444
        2018-01-05    0.026444
        2018-01-08    0.026444
    """

    if strict:
        ts_data = api.get_data_with_strict_range(ts_code, start, end)
    else:
        ts_data = api.get_data(ts_code, start, end)

    values = []
    index = []
    for i in ts_data:
        values.append(i["valor"])
        index.append(to_datetime(i["data"], "pt"))

    # Transform empty strings in null values
    values = [np.nan if value == "" else value for value in values]
    return pd.Series(values, index, name=ts_code, dtype=np.float64)  # type: ignore
