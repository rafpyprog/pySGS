import numpy as np
import pytest

from sgs.ts import time_serie


@pytest.mark.ts
def test_time_serie():
    ts = time_serie(4, "02/01/2018", "31/01/2018")
    assert len(ts) == 20
    assert ts.dtype == np.float
