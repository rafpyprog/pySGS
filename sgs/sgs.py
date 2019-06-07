from collections import OrderedDict
import os

import defusedxml.cElementTree as ET
from jinja2 import BaseLoader, Environment, select_autoescape
import numpy as np
import pandas as pd
import requests


# jinja template for webservice requests
template = """
    <?xml version="1.0" encoding="utf-8"?>
      <soapenv:Envelope
        xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <soapenv:Body>
          <{{ method }}
            xmlns="https://www3.bcb.gov.br/wssgs/services/FachadaWSSGS">
            {% for p in params %}
              {% if p == "codigosSeries" %}
                <{{ p }}><item>{{ params[p] }}</item></{{ p }}>
              {% else %}
                <{{ p }}>{{ params[p] }}</{{ p }}>
              {% endif %}
            {% endfor %}
          </{{ method }}>
        </soapenv:Body>
      </soapenv:Envelope>""".strip()


def parse_data(data: str) -> str:
    """ extrai a data e formata retornando no formato dd/mm/aaaa """
    dmy = data.split("/")
    fill = [2, 2, 4]
    dt = "/".join([i.zfill(fill[n]) for n, i in enumerate(dmy)])
    return dt


class SGS:
    """ Consulta séries temporais no SGS - Sistema Gerenciador de Séries
        Temporais do Banco Central do Brasil """

    def __init__(self) -> None:
        pass

    def load_template(self):
        """ Carrega e preeche o template do corpo do request ao webservice
            do SGS """

        autoescape = select_autoescape(default_for_string=True, default=True)
        loader = Environment(autoescape=True, loader=BaseLoader)
        return loader.from_string(template)

    def requests_wssgs(self, method: str, params: dict) -> bytes:
        """ Envia o request ao webservise do SGS """
        URL_WEBSERVICE = "https://www3.bcb.gov.br/wssgs/services/FachadaWSSGS"
        template = self.load_template()
        body = template.render(method=method, params=params)
        url = "{}?method={}".format(URL_WEBSERVICE, method)
        headers = {"soapAction": "{}/{}".format(URL_WEBSERVICE, method)}
        response = requests.post(url, headers=headers, data=body)
        response.raise_for_status()
        xml = response.content
        return xml

    def get_valores_series(
        self, codigo_serie: str, data_inicio: str, data_fim: str
    ) -> pd.DataFrame:
        """ Solicita uma série temporal ao SGS.

            Parâmetros:
            * codigo_serie(int): código da série
            * data_inicio(str): data de inicio no format dd/mm/yyyy
            * data_fim(str): data de fim no format dd/mm/yyyy

            Retorna dataframe contendo os valores da série temporal.
        """

        method = "getValoresSeriesXML"

        params = OrderedDict(
            [
                ("codigosSeries", codigo_serie),
                ("dataInicio", data_inicio),
                ("dataFim", data_fim),
            ]
        )

        wssg_response = self.requests_wssgs(method, params)
        if "Value(s) not found" in wssg_response.decode():
            msg = (
                "Valores não encontrados."
                " Verifique o código da série e a data de vigência."
            )
            raise ValueError(msg)

        tree = ET.fromstring(wssg_response)
        xml_return = list(tree.iter(tag="getValoresSeriesXMLReturn"))[0]
        serie = ET.fromstring(xml_return.text.encode("ISO-8859-1"))[0]
        colum_names = [i.tag for i in serie[0]]
        serie_temporal = []

        for item in serie:
            values = []
            for coluna in item:
                val = coluna.text
                if coluna.tag.startswith("DATA"):
                    val = parse_data(coluna.text)
                if coluna.tag.startswith("VALOR"):
                    try:
                        val = float(val)
                    except TypeError:  # trata valores nulos
                        val = np.nan
                values.append(val)
            serie_temporal.append(values)
        print(serie_temporal)

        df = pd.DataFrame(serie_temporal, columns=colum_names)

        for col in df:
            if col.startswith("DATA"):
                df.index = pd.to_datetime(df[col], dayfirst=True)
                df = df.drop("DATA", axis=1)
        if "BLOQUEADO" in df.columns:
            del df["BLOQUEADO"]

        df = df.rename(columns={"VALOR": codigo_serie})

        return df
