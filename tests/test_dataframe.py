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
    
@pytest.mark.dataframe
def test_dataframe_one_with_strict_as_false():
    df = dataframe(20577, start='17/08/2019', end='18/08/2019')
    assert df.shape == (1, 1)

@pytest.mark.dataframe
def test_dataframe_one_with_strict_as_true():
    df = dataframe(20577, start='17/08/2019', end='18/08/2019', strict=True)
    assert df.shape == (0, 1)

@pytest.mark.dataframe
def test_dataframe_multiple_with_strict_as_false():
    ts_codes = [20577,20669]
    df = dataframe(ts_codes, start='17/08/2019', end='18/08/2019')
    assert df.shape == (1, 2)

@pytest.mark.dataframe
def test_dataframe_multiple_with_strict_as_true():
    ts_codes = [20577,20669]
    df = dataframe(ts_codes, start='17/08/2019', end='18/08/2019', strict=True)
    assert df.shape == (0, 2)
