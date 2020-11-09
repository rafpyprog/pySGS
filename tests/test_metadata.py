import pytest

from sgs.metadata import *
from sgs import dataframe, time_serie


@pytest.mark.metadata
def test_metadata_returns_list_with_int_as_parameter():
    assert isinstance(metadata(4), list)


@pytest.mark.metadata
def test_metadata_returns_list_with_df_as_parameter():
    ts_codes = [12, 433]
    df = dataframe(ts_codes, start="02/01/2018", end="31/01/2018")
    meta = metadata(df)
    assert isinstance(meta, list)
    assert len(meta) == len(ts_codes)


@pytest.mark.metadata
def test_metadata_returns_list_with_ts_as_parameter():
    ts_code = 12
    ts = time_serie(ts_code, start="02/01/2018", end="31/01/2018")
    meta = metadata(ts)
    assert isinstance(meta, list)
    assert len(meta) == 1
