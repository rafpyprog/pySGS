import pandas as pd
from typing import Union
from .common import to_datetime, get_series_codes


def apply_strict_range(
    data: Union[pd.DataFrame, pd.Series], start: str, end: str
) -> Union[pd.DataFrame, pd.Series]:

    """
    SGS API default behaviour returns the last stored value when selected date range have no data.

    This function enforces the date range selected by user.

    :param data: time_serie or dataframe to be filtered.
    :param start: start date (DD/MM/YYYY).
    :param end: end date (DD/MM/YYYY).

    :return: time_serie or dataframe
    :rtype: pd.Series or pd.DataFrame
    """

    try:
        enforce_start = to_datetime(start, "pt")
        enforce_end = to_datetime(end, "pt")
        strict_data = data[data.index.to_series().between(enforce_start, enforce_end)]
    except ValueError:
        strict_data = data.drop(data.index)
        for ts_code in get_series_codes(data):
            print("ERROR: Serie %s - use 'DD/MM/YYYY' format for date strings." % ts_code)
   
    if not data.empty and strict_data.empty:
        for ts_code in get_series_codes(data):
            print("WARNING: Serie %s - There is no data for the requested period." % ts_code)

    return strict_data
