# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 22:38:01 2018

@author: Gaston Guillaux
"""

#given dataframe a below formula helps to calculate each day returns
#returns is defined as below
# return = (today_price - previous_price)/ previous_price



def create_random_dataframe(days=5, stocks_number=3):
    import pandas as pd
    dias = pd.date_range('01/01/2018', periods=days, freq='D')    
    stocks = {}

    
    for n in range(stocks_number):
        stock_name = random_string(4)
        stock_prices = random_prices(3,120,days)
        stocks[stock_name] = stock_prices
    
    return pd.DataFrame(stocks, dias)
    

def random_string(string_size=3):
    import random as r
    import string as s
    chars = s.ascii_uppercase
    return ''.join(r.choice(chars) for x in range(string_size))

def random_prices(low=1, high=99, days=5):
    import random as r
    return r.sample(range(low, high), k=days)

def calculate_return(stocks_dataframe, dias=1):
    hoje = stocks_dataframe
    ontem = stocks_dataframe.shift(dias)
    retorno = (hoje-ontem)/ontem
    return retorno