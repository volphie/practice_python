import pandas as pd
from datetime import datetime
from connection import insert_macro_economic_index

def get_index_go_kr_data(stts_cd, idx_cd, freq, start, end):
    url = 'http://www.index.go.kr/strata/jsp/showStblGams3.jsp?'\
        'stts_cd={0}&idx_cd={1}&freq={2}&period={3}:{4}'.format(stts_cd, idx_cd, freq, start, end)
    dfs = pd.read_html(url, encoding="utf-8")
    
    return dfs[0]



def save_won_dollar_exchange_rate_data(freq, start, end):
    
    df = get_index_go_kr_data('106801', '1068', freq, start, end)
    
    time_series = list(df.columns)[1:-1]
    time_series = [datetime(int(time[0:4]),int(time[4:6]),1) for time in time_series]
    
    values =df.iloc[[0],2:].values.tolist()[0]
    
    data_dic={
                'INDEX_ID': '106801', 
                'OBS_TIME': time_series, 
                'FREQ_TYPE' : 'Monthly' if freq == 'M' else 'Yearly', 
                'INDEX_NAME' : 'Won Dollar exchange rate', 
                'VAL': values 
            }
    
    insert_macro_economic_index(data_dic)
    
def save_nat_treasury_bond_data(freq, start, end):
    
    stts_cd = '107301' 
    idx_cd='1073'
    
    df = get_index_go_kr_data(stts_cd, idx_cd, freq, start, end)
    
    time_series = list(df.columns)[1:]
    time_series = [datetime(int(time[0:4]),int(time[4:6]),1) for time in time_series]
    print(time_series)
    
    # National Treasury Bond - 3 Years
    values =df.iloc[[0],1:].values.tolist()[0]   
    print(values)
    
    data_dic={
                'INDEX_ID': '{0}_03'.format(stts_cd), #National Treasury Bond - 3 Years code
                'OBS_TIME': time_series, 
                'FREQ_TYPE' : 'Monthly' if freq == 'M' else 'Yearly', 
                'INDEX_NAME' : 'National Treasury Bond - 3 Years', 
                'VAL': values 
            }
    
    insert_macro_economic_index(data_dic)    


    # National Treasury Bond - 10 Years
    values =df.iloc[[2],1:].values.tolist()[0]   #National Treasury Bond - 10 Years
    print(values)
    
    data_dic={
                'INDEX_ID': '{0}_10'.format(stts_cd), #National Treasury Bond - 10 Years code
                'OBS_TIME': time_series, 
                'FREQ_TYPE' : 'Monthly' if freq == 'M' else 'Yearly', 
                'INDEX_NAME' : 'National Treasury Bond - 10 Years', 
                'VAL': values 
            }
    
    insert_macro_economic_index(data_dic) 


# save_won_dollar_exchange_rate_data('M', '200001', '201707')
save_nat_treasury_bond_data('M', '199701', '201707')    