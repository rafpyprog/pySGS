.. _quickstart:

Quickstart
==========

Eager to get started? This page gives a good introduction in how to get started with **sgs**.

First, make sure that:

* Sgs is :ref:`installed <install>`

Let’s get started with some simple examples.


Time Serie
----------
Access time series data with **sgs** is very simple

Begin by importing the ``sgs`` module::

    >>> import sgs

Now, let's try to get a time serie. For this example, let's get the
"Interest rate - CDI" time serie in 2018, wich has the code 12.
Don't worry, on the next steps we will learn how to search for time
series codes::

    >>> CDI_CODE = 12
    >>> ts = sgs.time_serie(CDI_CODE, start='02/01/2018', end='31/12/2018')

Now, we have a Pandas Series object called ``ts``, with all the data and the index
representing the dates.

    >>> ts.head()
    2018-01-02    0.026444
    2018-01-03    0.026444
    2018-01-04    0.026444
    2018-01-05    0.026444
    2018-01-08    0.026444

Dataframe
---------
A common use case is building a dataframe with many time series. Once you have the desired time
series codes, you can easily create a dataframe with a single line of code. PySGS will fetch the
data and join the time series using the dates. Lets create a dataframe with two time series:

    >>> CDI = 12
    >>> INCC = 192  #  National Index of Building Costs
    >>> df = sgs.dataframe([CDI, INCC], start='02/01/2018', end='31/12/2018')

Now, we have a Pandas DataFrame object called ``df``, with all the data and the index
representing the dates used to join the two time series.

    >>> df.head()
                     12    192
    2018-01-01       NaN  0.31
    2018-01-02  0.026444   NaN
    2018-01-03  0.026444   NaN
    2018-01-04  0.026444   NaN
    2018-01-05  0.026444   NaN

The ``NaN`` values are due to the fact that the INCC time serie frequency is monthly
while CDI has a daily frequency.


Searching
---------

The SGS service provides thousands of time series. It's possible to search for time series by code and
also by name, with support to queries in English and Portuguese.


Search by name
~~~~~~~~~~~~~~
Let’s perform a search for time series with data about gold.

* English

    >>> results = sgs.search_ts("gold", language="en")
    >>> print(len(results))
    29
    >>> results[0]
    {'code': 4, 'name': 'BM&F Gold - gramme', 'unit': 'c.m.u.',
     'frequency': 'D', 'first_value': Timestamp('1989-12-29 00:00:00'),
     'last_value': Timestamp('2019-06-27 00:00:00'), 'source': 'BM&FBOVESPA'}

* Portuguese

    >>> results = sgs.search_ts("ouro", language="pt")
    >>> print(len(results))
    29
    >>> results[0]
    {'code': 4, 'name': 'Ouro BM&F - grama', 'unit': 'u.m.c.',
     'frequency': 'D', 'first_value': Timestamp('1989-12-29 00:00:00'),
     'last_value': Timestamp('2019-06-27 00:00:00'), 'source': 'BM&FBOVESPA'}


Search by code
~~~~~~~~~~~~~~
If you already have the time serie's code, this may be usefull to get the metadata.

    >>> GOLD_BMF = 4
    >>> sgs.search_ts(GOLD_BMF, language="pt")
    [{'code': 4, 'name': 'Ouro BM&F - grama', 'unit': 'u.m.c.', 'frequency': 'D',
      'first_value': Timestamp('1989-12-29 00:00:00'),
      'last_value': Timestamp('2019-06-27 00:00:00'),
      'source': 'BM&FBOVESPA'}]


Metadata
--------

To get the metadata about all the series present in a dataframe use the ``metadata`` function:

    >>> CDI = 12
    >>> INCC = 192  #  National Index of Building Costs
    >>> df = sgs.dataframe([CDI, INCC], start='02/01/2018', end='31/12/2018')
    >>> sgs.metadata(df)
    [{'code': 12, 'name': 'Interest rate - CDI', 'unit': '% p.d.', 'frequency': 'D',
    'first_value': Timestamp('1986-03-06 00:00:00'), 'last_value': Timestamp('2019-06-27 00:00:00'),
    'source': 'Cetip'}, {'code': 192, 'name': 'National Index of Building Costs (INCC)',
    'unit': 'Monthly % var.', 'frequency': 'M', 'first_value': Timestamp('1944-02-29 00:00:00'),
    'last_value': Timestamp('2019-05-01 00:00:00'), 'source': 'FGV'}]
