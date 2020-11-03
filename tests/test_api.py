import pytest

from sgs import api
import pandas as pd


@pytest.mark.api
def test_get_data():
    NUMBER_OF_LINES = 20
    data = api.get_data(4, "02/01/2018", "31/01/2018")
    assert isinstance(data, list)
    assert len(data) == NUMBER_OF_LINES
    
@pytest.mark.api
def test_enforce_integrity():
    data = api.get_data(20577, "17/08/2019", "18/08/2019", True)
    assert isinstance(data, list)
    assert len(data) == 0
