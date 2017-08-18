import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://volphie:jjo12345@localhost/stockanalysis?charset=utf8')


'''
#
# stock_ticker
#
'''
def query_stock_tickers():
    
    return pd.read_sql_table('stock_ticker',engine)


def query_ticker_name(ticker):
    
    sql ="select TICKER_NAME from stock_ticker where TICKER = \'{0}\'".format(ticker)
    return pd.read_sql_query(sql,engine)['TICKER_NAME'][0]



'''
#
# stock_price
#
'''
def query_stock_prices(ticker, year):
    
    sql = "select TR_DATE, CLOSE_PRICE from stock_price where TICKER = {0} and year(TR_DATE) = '{1}'".format(ticker, year)
    return pd.read_sql_query(sql, engine)

def query_stock_prices_after(ticker, day):
    
    sql = "select TR_DATE, CLOSE_PRICE from stock_price where TICKER = {0} and TR_DATE >= '{1}'".format(ticker, day)
    return pd.read_sql_query(sql, engine)




'''
#
# financial_index
#
'''
def query_eps_and_bps(ticker):
    
    sql = "select FIN_YEAR, EPS, BPS from financial_index where TICKER = {0} order by FIN_YEAR ASC".format(ticker)
    return pd.read_sql_query(sql, engine)


'''
#
# macro_economic_index
#
'''
def insert_macro_economic_index(data_dic):

    df = DataFrame(data_dic)
    df.to_sql('macro_economic_index', engine, if_exists='append', index=False)
    
    
def query_macro_economic_index(index_cd, start, end, freq ='Monthly'):
    
    sql = 'select OBS_TIME, VAL from macro_economic_index'\
          ' where INDEX_ID = \'{0}\' and FREQ_TYPE = \'{1}\''\
          ' and OBS_TIME between \'{2}-{3}-01\' and \'{4}-{5}-01\' '.format(index_cd, freq, start[0:4], start[4:6], end[0:4], end[4:6])
    return pd.read_sql_query(sql, engine)