import pandas as pd
from typing import List, Tuple, Union
from .search import search_ts
from .common import get_series_codes


def metadata(ts_code: Union[int, List, Tuple, pd.DataFrame, pd.Series], language: str = "en") -> List:
    """Request metadata about a time serie or all time series in a pandas dataframe.

    :param ts_code: time serie code or pandas dataframe with time series as columns.
    :param language: language of the returned metadata.

    :return: List of dicts containing time series metadata.
    :rtype: list_

    Usage::

        >>> CDI = 12
        >>> INCC = 192  #  National Index of Building Costs
        >>> df = sgs.dataframe([CDI, INCC], start='02/01/2018', end='31/12/2018')
        >>> sgs.metadata(df)
        [{'code': 12, 'name': 'Interest rate - CDI', 'unit': '% p.d.', 'frequency': 'D',
        'first_value': Timestamp('1986-03-06 00:00:00'), 'last_value': Timestamp('2019-06-27 00:00:00'),
        'source': 'Cetip'}, {'code': 192, 'name': 'National Index of Building Costs (INCC)',
        'unit': 'Monthly % var.', 'frequency': 'M', 'first_value': Timestamp('1944-02-29 00:00:00'),
        'last_value': Timestamp('2019-05-01 00:00:00'), 'source': 'FGV'}]
    """
    info = []
    for ts in get_series_codes(ts_code):
        try:
            metadata = search_ts(ts, language)
            info.extend(metadata)
        except NameError:
            info.append(None)

    return info
