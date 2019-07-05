.. image:: https://img.shields.io/pypi/v/sgs.svg
    :target: https://pypi.org/project/sgs/

.. image:: https://img.shields.io/pypi/l/sgs.svg
    :target: https://pypi.org/project/sgs/

.. image:: https://img.shields.io/pypi/pyversions/sgs.svg
    :target: https://pypi.org/project/sgs/

.. image:: https://img.shields.io/pypi/dm/sgs.svg
    :target: https://pypi.org/project/sgs/

.. image:: https://img.shields.io/travis/rafpyprog/pysgs.svg
    :target: https://travis-ci.org/rafpyprog/pySGS/

.. image:: https://img.shields.io/codecov/c/github/rafpyprog/pysgs.svg
    :target: https://codecov.io/github/rafpyprog/pysgs
    :alt: codecov.io


.. image:: https://img.shields.io/readthedocs/pysgs.svg
    :target: https://pysgs.readthedocs.io/en/stable/
    :alt: Read the docs!

|pic 1| **SGS**
=================

.. |pic 1| image:: https://raw.githubusercontent.com/rafpyprog/sgs/master/icon.png



Introduction
------------
This library provides a pure Python interface for the Brazilian Central Bank's
`Time Series Management System (SGS) <https://www.bcb.gov.br/?sgs>`_  api.
It works with Python 3.5 and above.

SGS is a service with more than 18,000 time series with economical and financial information.
This library is intended to make it easier for Python programmers to use this data in projects of
any kind, providing mechanisms to search for, extract and join series.


Quickstart
----------
Access time series data with **sgs** is very simple

Begin by importing the ``sgs`` module:


.. code-block:: python

    import sgs


Now, let's try to get a time serie. For this example, let's get the
"Interest rate - CDI" time serie in 2018, wich has the code 12.


.. code-block:: python

    CDI_CODE = 12
    ts = sgs.time_serie(CDI_CODE, start='02/01/2018', end='31/12/2018')


Now, we have a Pandas Series object called ``ts``, with all the data and
the index representing the dates.

    ts.head()

+------------+----------+
| 2018-01-02 | 0.026444 |
+------------+----------+
| 2018-01-03 | 0.026444 |
+------------+----------+
| 2018-01-04 | 0.026444 |
+------------+----------+
| 2018-01-05 | 0.026444 |
+------------+----------+
| 2018-01-08 | 0.026444 |
+------------+----------+

