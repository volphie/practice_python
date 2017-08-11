import googlefinance.client as gfc
import pandas as pd
from connection import engine
from connection import query_stock_tickers
#from sqlalchemy import create_engine

# get closing price data (return pandas dataframe) from googlefinance API
# params=[
# {
# 'q': "000020",
# 'x': "KRX",
# }
# ]
# period = "1M"
# df = gfc.get_closing_data(params, period)
# print(df)

#engine = create_engine('mysql+pymysql://volphie:jjo12345@localhost/stockanalysis?charset=utf8')

'''
* Parameter : ticker(종목코드)
* ticker에 해당하는 종목 데이터를 googlefinance로부터 얻어 MysqlDB에 저장함
'''
def save_stock_price_to_db(ticker, market, yesterday=False):
# get price data from googlefinance
    
    param = {
      'q': ticker,  # Stock symbol (ex: "AAPL")
      'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
      'x': "KRX" if market =='KOSPI' else "KOSDAQ",  # Stock exchange symbol on which stock is traded (ex: "KRX" for KOSPI)
      'p': "20Y"  # Period (Ex: "1Y" = 1 year)
    }
    
#     print(param)
    df = gfc.get_price_data(param)
    if yesterday == True :
        df = df.ix[-1:,:]
#     print(df)
    
    # I am going to save data to Mysql DB
    df.insert(0, 'tr_date', df.index)
    df.insert(0, 'ticker', ticker)
    # Column labels should be the same with table fields
    df.columns = ['TICKER', 'TR_DATE', 'OPEN_PRICE', 'HIGH_PRICE', 'LOW_PRICE', 'CLOSE_PRICE', 'TR_VOLUME']
    # print(df)
    # When using pymysql, connection string should be like this ; mysql+pymysql://...
    #engine = create_engine('mysql+pymysql://volphie:jjo12345@localhost/stockanalysis')
    df.to_sql('stock_price', engine, if_exists='append', index=False)

'''
* Select * from stock_ticker
* return the result as a form of DataFrame
'''
# df = query_stock_tickers()
# for index, row in df.iterrows() :
#     try:
#         save_stock_price_to_db(row['TICKER'],row['MARKET'])
#         print("{0} is saved to the table...".format(row['TICKER']))
#     except :
#         print("[Exception] Error occurs during handling {0}".format(row['TICKER']))
#         pass
save_stock_price_to_db('002300',market='KOSPI', yesterday=False)
