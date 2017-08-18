'''
Created on 2017. 8. 11.

@author: P116402
'''

import connection as con
import numpy as np
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

ticker = '002300'
ticker_name = con.query_ticker_name(ticker)


df = con.query_eps_and_bps(ticker)
print(df)

eps = list(df['EPS'])
bps = list(df['BPS'])
weights = [1,2,3]

iv = list()
for i in range(len(eps)):
    if i == 0 or i == 1 or i == 2 :
        iv.append('')
    else :
        subeps = eps[i-3:i]
#         print(subeps)
        iv.append((np.average(subeps, weights = weights)*10 + bps[i-1])/2)
df['IV'] = iv    
df['YEAR'] = [x.strftime('%Y') for x in df['FIN_YEAR']]
print(df)

df2 = con.query_stock_prices_after(ticker, '2015-01-01')
df2['YEAR'] = [x.strftime('%Y') for x in df2['TR_DATE']]
print(df2)

df2['IV'] = [df.loc[df['YEAR'] == x]['IV'].values[0] for x in df2['YEAR']]
print(df2)

# 한글 사용을 위한 font 선택
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.title('Price and Internal Value Spread for {0}({1})'.format(ticker_name, ticker))
plt.plot(df2['TR_DATE'],df2['CLOSE_PRICE'])
plt.plot(df2['TR_DATE'],df2['IV'])

plt.show()
