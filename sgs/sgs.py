from typing import List, Union

import pandas as pd


class SGS:
    """ Consulta séries temporais no SGS - Sistema Gerenciador de Séries
        Temporais do Banco Central do Brasil """

    def __init__(self) -> None:
        pass

    def read_from_api(
            self,
            codigo_serie: int,
            data_inicio: str,
            data_fim: str
    ) -> pd.DataFrame:
        """ Read data in csv format from the SGS API """
        url = (
            "http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}"
            "/dados?formato=csv&dataInicial={}&dataFinal={}"
        )
        serie = pd.read_csv(
            url.format(codigo_serie, data_inicio, data_fim),
            index_col="data",
            parse_dates=True,
            dayfirst=True,
            sep=";",
        )
        serie = serie.rename(columns={'valor': codigo_serie})
        if 'datafim' in serie.columns:
            del serie['datafim']

        del serie.index.name
        return serie

    def get_valores_series(
            self,
            codigo_serie: Union[int, List],
            data_inicio: str,
            data_fim: str
    ) -> pd.DataFrame:
        """ Solicita uma série temporal ao SGS.

            Parâmetros
            ----------

            * codigo_serie(int): código da série
            * data_inicio(str): data de inicio no format dd/mm/yyyy
            * data_fim(str): data de fim no format dd/mm/yyyy

            Retorna dataframe contendo os valores da série temporal.
        """
        if not isinstance(codigo_serie, (list, tuple)):
            codigos = [codigo_serie]
        else:
            codigos = codigo_serie

        series = []
        for cod in codigos:
            serie = self.read_from_api(cod, data_inicio, data_fim)
            series.append(serie)

        return pd.concat(series, axis=1)
