"""
Time Serie manipulation
"""
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from . import api
from . import search
from .common import to_datetime


def time_serie(ts_code: int, start: str, end: str) -> pd.Series:
    """
    Time serie

    """
    ts_data = {"values": [], "index": []}  # type: Dict[str, List]
    values = []
    index = []
    for i in api.get_data(ts_code, start, end):
        values.append(i["valor"])
        index.append(to_datetime(i["data"], 'pt'))

    return pd.Series(values, index, name=ts_code, dtype=np.float)
