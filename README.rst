.. image:: https://travis-ci.org/rafpyprog/pySGS.svg?branch=master
    :target: https://travis-ci.org/rafpyprog/pySGS


|pic 1| **pySGS**
=================

.. |pic 1| image:: https://raw.githubusercontent.com/rafpyprog/sgs/master/icon.png

Este pacote funciona como um wrapper para o webservice do
Sistema Gerenciador de Séries Temporais (SGS) do Banco Central do Brasil, facilitando o trabalho de desenvolvedores e pesquisadores que necessitam de séries temporais de indicadores financeiros.

Instalação
==========

.. code-block:: bash

    pip install sgs


Tutorial
========


Para obter a série temporal de um indicador, instancie a classe SGS, utilizando como parâmetros o código da série desejada e a data de ínicio e fim. Será retornado um pandas.DataFrame, com a coluna do tipo data devidamente formatadas no formato datetime e os valores da série.

.. code-block:: python

    # Exemplo de pesquisa do CDI no ano de 2016
    >>> from sgs import SGS
    >>>
    >>> sgs = SGS()
    >>> df = sgs.get_valores_series(12, '01/01/2016', '31/12/2016')
    >>> df.head()


+---+------------+----------+
|   | **DATA**   | **VALOR**|
+---+------------+----------+
| 0 | 2016-01-04 | 0.052496 |
+---+------------+----------+
| 1 | 2016-01-05 | 0.052496 |
+---+------------+----------+
| 2 | 2016-01-06 | 0.052496 |
+---+------------+----------+
| 3 | 2016-01-07 | 0.052496 |
+---+------------+----------+
| 4 | 2016-01-08 | 0.052496 |
+---+------------+----------+


O módulo auxiliar 'series' possui o código de alguns indicadores mais comuns:

.. code-block:: python

    >>> from sgs import SGS, series
    >>>
    >>> sgs = SGS()
    >>> df = sgs.get_valores_series(series.BOVESPA_INDICE, '31/12/2017', '01/02/2018')
    >>> df.head()


+--+------------+-----------+
|  | **DATA**   | **VALOR** |
+--+------------+-----------+
|0 | 2018-01-02 |77891      |
+--+------------+-----------+
|1 | 2018-01-03 |77995      |
+--+------------+-----------+
|2 | 2018-01-04 |78647      |
+--+------------+-----------+
|3 | 2018-01-05 |79071      |
+--+------------+-----------+
|4 | 2018-01-08 |79378      |
+--+------------+-----------+


.. code-block:: python

    >>> # Indicadores disponíveis
    >>> dir(series)[-8]
    ['BOVESPA_VALOR_LISTADAS', 'BOVESPA_INDICE', 'BOVESPA_QTD_LISTADAS', 'BOVESPA_VOLUME', 'CDI',
     'DOWN_JONES', 'IGP10', 'IGPDI', 'INCC', 'IPA', 'IPC', 'IPCA', 'NASDAQ', 'OURO', 'PIB_RS_CORRENTE',
     'PIB_VAR_PERC', 'POUPANCA_I', 'POUPANCA_II', 'SELIC', 'SELIC_ACUM_MES', 'SELIC_META', 'TBF',
     'TJLP', 'TR']


Para consultar código das séries disponíveis e outras informações, visite o site do SGS: https://www3.bcb.gov.br/sgspub/
