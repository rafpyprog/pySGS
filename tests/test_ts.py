import numpy as np
import pytest

from sgs.ts import time_serie


@pytest.mark.ts
def test_time_serie():
    ts = time_serie(4, "02/01/2018", "31/01/2018")
    assert len(ts) == 20
    assert ts.dtype == np.float64

@pytest.mark.ts
def test_ts_with_null_values():
    # Issue #28
    ts = time_serie(21554, start="31/12/1992", end="01/06/2019")
    data = ts.loc['1994-04-01']
    assert np.isnan(data) == True

@pytest.mark.ts
def test_ts_with_strict_as_false():
    ts = time_serie(20577, "17/08/2019", "18/08/2019")
    assert len(ts) == 1
    assert ts.dtype == np.float64

@pytest.mark.ts
def test_ts_with_strict_as_true():
    ts = time_serie(20577, "17/08/2019", "18/08/2019", True)
    assert len(ts) == 0
    assert ts.dtype == np.float64
