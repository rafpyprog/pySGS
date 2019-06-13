from collections import OrderedDict

import pandas as pd
import pytest

from sgs import SGS


def test_sgs_instance():
    sgs = SGS()
    assert isinstance(sgs, SGS)


def test_get_valor_serie():
    sgs = SGS()
    serie = 12
    df = sgs.get_valores_series(serie, '02/01/2018', '31/01/2018')
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == [serie]
    assert df.shape == (22, 1)


def test_get_valor_serie_inicio_fim():
    sgs = SGS()
    serie = 253
    df = sgs.get_valores_series(serie, '02/01/2018', '31/01/2018')
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == [serie]
    assert df.shape == (30, 1)


def test_get_valor_serie_multiple_series():
    sgs = SGS()
    series = [12, 253]
    df = sgs.get_valores_series(series, '02/01/2018', '31/01/2018')
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == series
    assert df.shape == (30, 2)
