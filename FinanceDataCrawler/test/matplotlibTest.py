import matplotlib.pyplot as plt
from connection import query_stock_prices

df = query_stock_prices('000020', '2017')

plt.plot(df['TR_DATE'], df['CLOSE_PRICE'])

plt.show()