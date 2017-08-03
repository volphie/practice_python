import pandas as pd
from connection import engine

cols = ['TICKER','TICKER_NAME','MARKET']

df=pd.read_csv('C:/eclipse-workspace/FinanceDataCrawler/data/krx_stock_list_kospi.csv')
df.columns= cols
print(df)
 
df.to_sql('stock_ticker',engine, if_exists='append', index=False)
 
df=pd.read_csv('C:/eclipse-workspace/FinanceDataCrawler/data/krx_stock_list_kosdaq.csv')
df.columns= cols
print(df)
 
df.to_sql('stock_ticker',engine, if_exists='append', index=False)