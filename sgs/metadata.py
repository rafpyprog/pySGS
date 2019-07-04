from typing import Optional, Dict, List, Union

import pandas as pd

from .search import search_ts


def metadata(
    ts_code: Union[int, pd.DataFrame], language: str="en"
) -> Optional[List]:
    """Request metadata about time series present in a pandas dataframe.

    :param ts_code: time serie code or pandas dataframe with time series as columns.
    :param language: language of the returned metadata.

    :return: List of dicts containing time series metadata.
    :rtype: list_

    Usage::

        >>> time_series = [12, 192]
        >>> df = sgs.dataframe(time_series, start='02/01/2018', end='31/12/2018')

        >>> results = sgs.search_ts("gold", language="en")
        >>> len(results)
        29
        >>> results[0]
        {'code': 4, 'name': 'BM&F Gold - gramme', 'unit': 'c.m.u.',
        'frequency': 'D', 'first_value': Timestamp('1989-12-29 00:00:00'),
        'last_value': Timestamp('2019-06-27 00:00:00'),
        'source': 'BM&FBOVESPA'}
    """
    info = []
    if isinstance(ts_code, pd.core.frame.DataFrame):
        for col in ts_code.columns:
            col_info = search_ts(col, language)
            if col_info is not None:
                info.append(col_info[0])
            else:
                info.append(None)
    else:
        col_info = search_ts(ts_code, language)
        info.append(col_info)
    return info
