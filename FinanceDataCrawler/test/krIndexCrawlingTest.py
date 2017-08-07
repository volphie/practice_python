import pandas as pd
from datetime import datetime
from connection import insert_macro_economic_index
# 
# url = 'http://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=106801&idx_cd=1068&freq=M&period=197001:201706'
# dfs = pd.read_html(url, encoding="utf-8")
# 
# cols_time = list(dfs[0].columns)
# print(cols_time)
# cols_time = cols_time[1:-1]
# print(cols_time)
# 
# # year = int(cols_time[0][0:4])
# # month = int(cols_time[0][4:6])
# # print(datetime(2000, 1, 1))
# 
# cols_time = [datetime(int(time[0:4]),int(time[4:6]),1) for time in cols_time]
# print(cols_time)
# 
# cols_value =dfs[0].iloc[[0],2:].values.tolist()[0]
# print(cols_value)

#  
# row1 = dfs[0].iloc[[0]]
# print(row1)
# row = dfs[0].iloc[[0],2:]
# row.iloc[[0],[-1]]=0
# print(row)

def get_index_go_kr_data(stts_cd, idx_cd, freq, start, end):
    url = 'http://www.index.go.kr/strata/jsp/showStblGams3.jsp?'\
        'stts_cd={0}&idx_cd={1}&freq={2}&period={3}:{4}'.format(stts_cd, idx_cd, freq, start, end)
    dfs = pd.read_html(url, encoding="utf-8")
    
    return dfs[0]


# def get_won_dollar_exchange_rate_data(freq, start, end):
#     
#     df = get_index_go_kr_data('106801', '1068', freq, start, end)
#     
#     time_series = list(df.columns)[1:-1]
#     time_series = [datetime(int(time[0:4]),int(time[4:6]),1) for time in time_series]
# #     print(time_series)
#     
#     values =df.iloc[[0],2:].values.tolist()[0]
# #     print(values)
#     
#     return time_series, values


def save_won_dollar_exchange_rate_data(freq, start, end):
    
    
#     time_series, values = get_won_dollar_exchange_rate_data(freq, start, end)
    df = get_index_go_kr_data('106801', '1068', freq, start, end)
    
    time_series = list(df.columns)[1:-1]
    time_series = [datetime(int(time[0:4]),int(time[4:6]),1) for time in time_series]
#     print(time_series)
    
    values =df.iloc[[0],2:].values.tolist()[0]
    
    data_dic={
                'INDEX_ID': '106801', 
                'OBS_TIME': time_series, 
                'FREQ_TYPE' : 'Monthly' if freq == 'M' else 'Yearly', 
                'INDEX_NAME' : 'Won Dollar exchange rate', 
                'VAL': values 
            }
    
    insert_macro_economic_index(data_dic)
    

save_won_dollar_exchange_rate_data('M', '200001', '201707')
    