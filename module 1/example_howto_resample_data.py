# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 22:09:23 2018

@author: Gaston Guillaux
"""



def days_to_weeks(open_prices, high_prices, low_prices, close_prices):
    import pandas as pd
    
    """Converts daily OHLC prices to weekly OHLC prices.
    
    Parameters
    ----------
    open_prices : DataFrame
        Daily open prices for each ticker and date
    high_prices : DataFrame
        Daily high prices for each ticker and date
    low_prices : DataFrame
        Daily low prices for each ticker and date
    close_prices : DataFrame
        Daily close prices for each ticker and date

    Returns
    -------
    open_prices_weekly : DataFrame
        Weekly open prices for each ticker and date
    high_prices_weekly : DataFrame
        Weekly high prices for each ticker and date
    low_prices_weekly : DataFrame
        Weekly low prices for each ticker and date
    close_prices_weekly : DataFrame
        Weekly close prices for each ticker and date
    """
    
    ow = open_prices.resample('W').ohlc()[['open']]
    hw = high_prices.resample('W').ohlc()[['high']]
    lw = low_prices.resample('W').ohlc()[['low']]
    cw = close_prices.resample('W').ohlc()[['close']]
    
    
    # TODO: Implement Function
    return ow, hw, lw, cw
    #return None, None, None, None

def resample_prices(close_prices, freq='M'):
    """
    Resample close prices for each ticker at specified frequency.
    
    Parameters
    ----------
    close_prices : DataFrame
        Close prices for each ticker and date
    freq : str
        What frequency to sample at
        For valid freq choices, see http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
    
    Returns
    -------
    prices_resampled : DataFrame
        Resampled prices for each ticker and date
    """
    # TODO: Implement Function
    import pandas as pd
    symbols = close_prices.columns.tolist()
    series = []
    
    for symbol in symbols:
        aux_s = close_prices[symbol].resample(freq).ohlc()['close']
        aux_s.name = symbol
        series.append(aux_s)
    return pd.concat(series, axis=1)