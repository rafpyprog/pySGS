import pandas as pd
from typing import Union, Optional
from .common import to_datetime, get_series_codes


def constrain(data: Union[pd.DataFrame, pd.Series], start: str, end: Optional[str] = None) -> Union[pd.DataFrame, pd.Series]:

    """
    SGS API default behaviour returns the last stored value when selected date range have no data.

    This function enforces the date range selected by user.

    :param data: time_serie or dataframe to be filtered.
    :param start: start date (DD/MM/YYYY).
    :param end: end date (DD/MM/YYYY).

    :return: time_serie or dataframe
    :rtype: pd.Series or pd.DataFrame
    """
    
    if end is None:
        end = start

    try:
        enforce_start = to_datetime(start, "pt")
        enforce_end = to_datetime(end, "pt")
        strict_data = data[data.index.to_series().between(enforce_start, enforce_end)]
        if strict_data.empty or data.empty:
            RuntimeError
    except ValueError:
        strict_data = data.drop(data.index)
        print("ERROR: Please, use 'DD/MM/YYYY' format for date strings.")
    except RuntimeError:
        series = ','.join(str(code) for code in get_series_codes(data))
        print("WARNING: Serie(s) %s - There is no data for the requested period." % series)

    return strict_data
