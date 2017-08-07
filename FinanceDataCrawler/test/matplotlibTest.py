import matplotlib.pyplot as plt
from connection import query_stock_prices
from connection import query_macro_economic_index

# df = query_stock_prices('000020', '2017')
# 
# plt.plot(df['TR_DATE'], df['CLOSE_PRICE'])

df = query_macro_economic_index('107301_10' , '200101', '201707', 'Monthly')
df2 = query_macro_economic_index('107301_03', '200101', '201707', 'Monthly')
df3 = query_macro_economic_index('T10Y2Y'   , '200101', '201707', 'Monthly')
df4 = query_macro_economic_index('DCOILWTICO'   , '200101', '201707', 'Monthly')

plt.plot(df['OBS_TIME'], df['VAL'])
plt.plot(df2['OBS_TIME'], df2['VAL'])
plt.plot(df3['OBS_TIME'], df3['VAL'])
plt.plot(df4['OBS_TIME'], df4['VAL'])

plt.show()