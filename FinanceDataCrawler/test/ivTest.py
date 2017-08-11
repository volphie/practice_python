'''
Created on 2017. 8. 11.

@author: P116402
'''

import connection
import numpy as np
import matplotlib.pyplot as plt

df = connection.query_eps_and_bps('002300')
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

df2 = connection.query_stock_prices_after('002300', '2015-01-01')
df2['YEAR'] = [x.strftime('%Y') for x in df2['TR_DATE']]
print(df2)

df2['IV'] = [df.loc[df['YEAR'] == x]['IV'].values[0] for x in df2['YEAR']]
print(df2)

plt.plot(df2['TR_DATE'],df2['CLOSE_PRICE'])
plt.plot(df2['TR_DATE'],df2['IV'])

plt.show()
