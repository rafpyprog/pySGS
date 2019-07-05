import pytest
from sgs.dataframe import dataframe


@pytest.mark.dataframe
def test_dataframe_one_ts():
    df = dataframe(4, start="02/01/2018", end="31/01/2018")
    assert df.shape == (20, 1)


@pytest.mark.dataframe
def test_dataframe_multiple_ts():
    ts_codes = [12, 433]
    df = dataframe(ts_codes, start="02/01/2018", end="31/01/2018")
    assert df.shape == (23, 2)
