from typing import Optional, Dict, List, Union

import pandas as pd

from .search import search_ts


def metadata(
    ts_code: Union[int, pd.DataFrame], language: str="en"
) -> Optional[List]:
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
