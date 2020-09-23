from . import api

import numpy as np
import pandas as pd


def expectations(resource: str, begin: str, end: str) -> pd.DataFrame:
    """Get market expectations data.

    :param resource: str, one of "monthly", "quarterly", "yearly", "infl12m",
    "monthlytop5", "yearlytop5", "inst".
    :param start: start date (DD/MM/YYYY).
    :param end: end date (DD/MM/YYYY).

    :return: A pandas DataFrame.
    :rtype: pandas.DataFrame
    """
    valid_resources = ["monthly", "quarterly", "yearly", "infl12m",
                       "monthlytop5", "yearlytop5", "inst"]

    if resource not in valid_resources:
        raise ValueError(
            "Please input one of the valid resources: {}".format(valid_resources))

    response = api.get_data_olinda(resource, begin, end)
    df = pd.DataFrame.from_dict(response["value"])

    if "DataReferencia" in df:
        df["DataReferencia"] = pd.to_datetime(df["DataReferencia"])

    return df
