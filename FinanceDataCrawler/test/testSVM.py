'''
Created on 2017. 8. 11.

@author: P116402
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader.data as web
from sklearn import neighbors, svm
from sklearn.ensemble import RandomForestClassifier
import connection



def price_bak(stock, start):

    price = web.DataReader(name=stock, data_source='yahoo', start=start)['Adj Close']

    return price.div(price.iat[0]).resample('M').last().to_frame('price')


def price(stock, start):
    
    df = connection.query_stock_prices_after(stock, start)
    df.index = df['TR_DATE']
    df=df['CLOSE_PRICE']
    
    df = df.div(df.iat[0]).resample('M').last().to_frame('price')
    
    print(df)
    
    return df
    

def fractal(a, p):

    df = pd.DataFrame()

    for count in range(1,p+1):

        a['direction'] = np.where(a['price'].diff(count)>0,1,0)

        a['abs'] = a['price'].diff(count).abs()

        a['volatility'] = a.price.diff().abs().rolling(count).sum()

        a['fractal'] = a['abs']/a['volatility']*a['direction']

        df = pd.concat([df, a['fractal']], axis=1)

    return df



def meanfractal(a, l=12):

    a['meanfractal']= pd.DataFrame(fractal(a, l)).sum(1,skipna=False)/l



def run():
#     a = price('^K11','2000-01-01')
    
    a = price('005380', '2005-01-01')    
    a['cash'] = [(1.03**(1/12))**x for x in range(len(a.index))]
    a['meanfractal']= pd.DataFrame(fractal(a, 12)).sum(1,skipna=False)/12   
    a['rollingstd'] = a.price.pct_change().shift(1).rolling(12).std()
    a['result'] = np.where(a.price > a.price.shift(1), 1,0)     
    a = a.dropna()
        
    print(a)
        
    clf = neighbors.KNeighborsClassifier(n_neighbors=3)
    clf1 = svm.SVC()
    clf3 = RandomForestClassifier(n_estimators=5)
    
    a['predicted']= pd.Series()
    
    for i in range(12,len(a.index)):
        x  =  a.iloc[i-12:i,6:8]    
        y  =  a['result'][i-12:i] 
        clf.fit(x, y)
        a['predicted'][i]= clf.predict(x)[-1] 
    
    a = a.dropna()
    a.price = a.price.div(a.price.ix[0])
    
    print(a)
    
    accuracy=clf.score(a.iloc[:,6:8],a['result'])


run()
# price('005380', '2005-01-01')