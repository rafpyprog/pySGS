"""
Dataframe
"""
from typing import Dict, List, Tuple, Union

import pandas as pd

from . import api
from . import search
from .ts import time_serie


def dataframe(
    ts_codes: Union[int, List, Tuple], start: str, end: str
) -> pd.DataFrame:
    if isinstance(ts_codes, int):
        ts_codes = [ts_codes]
    series = [time_serie(i, start, end) for i in ts_codes]
    df = pd.concat(series, axis=1)
    return df
