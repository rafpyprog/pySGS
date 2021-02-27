
import pytest
import pandas as pd
from sgs.strict import constrain
from sgs.dataframe import dataframe
from sgs.ts import time_serie

@pytest.mark.common
def test_constrain_on_df():
    df = dataframe(12, '01/01/2020', '01/05/2020')
    strict_df = constrain(df, '01/01/2020', '01/04/2020')
    expected = 63
    assert len(strict_df) == expected
    assert isinstance(strict_df, pd.DataFrame)

@pytest.mark.common
def test_constrain_on_ts():
    ts = time_serie(12, '01/01/2020', '01/05/2020')
    strict_ts = constrain(ts, '01/01/2020', '01/04/2020')
    expected = 63
    assert len(strict_ts) == expected
    assert isinstance(strict_ts, pd.Series)
