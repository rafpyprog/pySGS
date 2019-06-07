from collections import OrderedDict

import pandas as pd
import pytest

from sgs import SGS


def test_sgs_instance():
    sgs = SGS()
    assert isinstance(sgs, SGS)


def test_requests_wssgs():
    sgs = SGS()
    method = "getValoresSeriesXML"
    params = OrderedDict([
        ("codigosSeries",  12),
        ("dataInicio", "01/01/2018"),
        ("dataFim", "01/02/2018"),
    ])

    response = sgs.requests_wssgs(method=method, params=params)
    assert isinstance(response, bytes)
    assert response.startswith(b'<?xml')


def test_get_valor_serie():
    sgs = SGS()
    serie = 12
    df = sgs.get_valores_series(serie, '01/01/2018', '31/01/2018')
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == [serie]
    assert df.shape == (22, 1)
