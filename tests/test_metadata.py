import pytest

from sgs.metadata import *
from sgs import dataframe


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
