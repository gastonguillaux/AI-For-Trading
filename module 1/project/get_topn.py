# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:19:45 2018

@author: Gaston Guillaux
"""

def get_top_n(prev_returns, top_n):
    """
    Select the top performing stocks
    
    Parameters
    ----------
    prev_returns : DataFrame
        Previous shifted returns for each ticker and date
    top_n : int
        The number of top performing stocks to get
    
    Returns
    -------
    top_stocks : DataFrame
        Top stocks for each ticker and date marked with a 1
    """
    import numpy as np
    import pandas as pd
    # TODO: Implement Function
    aux = []
    for r in prev_returns.iterrows():
        s = r[1]                                        # from the row tuple get the series
        top_symbols = s.nlargest(top_n)                 # from the series, get the top n
        s_bool = s.isin(top_symbols).astype(np.int64)   # get a boolean numeric image of the series
        aux.append(s_bool)                              # append this result to a list to be used to create new dataframe
    
    return pd.concat(aux, axis=1).transpose()

#============================================================================


def date_top_industries(prices, sector, date, top_n):
    """
    Get the set of the top industries for the date
    
    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date
    sector : Series
        Sector name for each ticker
    date : Date
        Date to get the top performers
    top_n : int
        Number of top performers to get
    
    Returns
    -------
    top_industries : set
        Top industries for the date
    """
    # TODO: Implement Function
    
    filtered_series = prices.loc[date]
    top_guys = filtered_series.nlargest(top_n)
    top_sec = sector.loc[top_guys.index.tolist()]
    
    return set(top_sec)


def portfolio_returns(df_long, df_short, lookahead_returns, n_stocks):
    """
    Compute expected returns for the portfolio, assuming equal investment in each long/short stock.
    
    Parameters
    ----------
    df_long : DataFrame
        Top stocks for each ticker and date marked with a 1
    df_short : DataFrame
        Bottom stocks for each ticker and date marked with a 1
    lookahead_returns : DataFrame
        Lookahead returns for each ticker and date
    n_stocks: int
        The number number of stocks chosen for each month
    
    Returns
    -------
    portfolio_returns : DataFrame
        Expected portfolio returns for each ticker and date
    """
    # TODO: Implement Function
    
    longed = df_long * lookahead_returns 
    shorted = (df_short * lookahead_returns) * -1 
    r = (longed + shorted) / 3
    
    return r
