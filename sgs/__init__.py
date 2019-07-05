"""
# Time Series Management System

The SGS is a system maintened by the Central Bank of Brazil with the
objective of consolidating and making available economic-financial
information, as well as maintaining uniformity among documents
produced based on time series stored in it.
"""

from .__version__ import __version__
from .dataframe import dataframe
from .ts import time_serie
from .metadata import metadata
from .search import search_ts
