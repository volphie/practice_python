import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://volphie:jjo12345@localhost/stockanalysis?charset=utf8')


def query_stock_tickers():
    
    return pd.read_sql_table('stock_ticker',engine)


def query_stock_prices(ticker, year):
    
    sql = "select TR_DATE, CLOSE_PRICE from stock_price where TICKER = {0} and year(TR_DATE) = '{1}'".format(ticker, year)
    
    return pd.read_sql_query(sql, engine)
    