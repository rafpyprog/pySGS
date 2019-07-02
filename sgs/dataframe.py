"""
Dataframe
"""
import time
from typing import Dict, List, Tuple, Union

import pandas as pd

from . import api
from . import search
from .ts import time_serie


def dataframe(
    ts_codes: Union[int, List, Tuple], start: str, end: str
) -> pd.DataFrame:
    """
    Creates a dataframe
    """
    if isinstance(ts_codes, int):
        ts_codes = [ts_codes]

    series = []
    for code in ts_codes:
        time.sleep(0.1)
        ts = time_serie(code, start, end)
        series.append(ts)

    df = pd.concat(series, axis=1)
    return df
