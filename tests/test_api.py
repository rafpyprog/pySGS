import pytest

from sgs import api
import pandas as pd


@pytest.mark.api
def test_get_data():
    NUMBER_OF_LINES = 20
    data = api.get_data(4, "02/01/2018", "31/01/2018")
    assert isinstance(data, list)
    assert len(data) == NUMBER_OF_LINES
