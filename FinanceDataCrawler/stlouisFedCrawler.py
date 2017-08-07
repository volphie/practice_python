import requests
import matplotlib.pyplot as plt
from test.datetimeTest import datetime_from_millis
from connection import insert_macro_economic_index
from pandas import DataFrame

def get_stlouisfed_data(index_id, freq='Monthly'):
    
    if freq!='Monthly' and freq!='Daily':
        freq = 'Monthly'
        
    url = 'https://fred.stlouisfed.org/graph/graph-data.php?mode=fred&id={0}&fq={1}'.format(index_id, freq)
    
    result = requests.get(url).json()
    
    data = result['seriess'][0]['obs']
    
    col_time = [datetime_from_millis(x[0]) for x in data]
    col_val  = [x[1] for x in data]

    return col_time, col_val

def save_slouisfed_data(index_id, idName, freq):
    
    #get data
    time_series, values = get_stlouisfed_data(index_id, freq)
    
    data_dic = {'INDEX_ID':index_id, 'OBS_TIME': time_series, 'FREQ_TYPE' : freq, 'INDEX_NAME' : idName, 'VAL': values }
    insert_macro_economic_index(data_dic)

# # WTI crude oil
# url = 'https://fred.stlouisfed.org/graph/graph-data.php?mode=fred&id=DCOILWTICO'
# #     '&fq=Daily&fam=avg&transformation=lin&nd=1986-01-02&ost=-99999&oet=99999&lsv=&lev=&fml=a&fgst=lin&fgsnd=2009-06-01'\
# #     '&mma=0&scale=left&line_color=%234572a7&line_style=solid&vintage_date=&revision_date=&chart_type=line&stacking=&drp=0&cosd=&coed=&log_scales='
# 
# # Interest rate spread
# url2 = 'https://fred.stlouisfed.org/graph/graph-data.php?mode=fred&id=T10Y2Y&fq=Monthly'
# #     '&fq=Daily&fam=avg&transformation=lin&nd=1980-06-01&ost=-99999&oet=99999&lsv=&lev=&fml=a&fgst=lin&fgsnd=2009-06-01'\
# #     '&mma=0&scale=left&line_color=%234572a7&line_style=solid&vintage_date=&revision_date=&chart_type=line&stacking=&drp=0&cosd=&coed=&log_scales='
#     

save_slouisfed_data('T10Y2Y','Interest Rate Spread(USA)','Monthly')
save_slouisfed_data('DCOILWTICO','WTI Crude Oil Price','Monthly')


# plt.plot(times, values)
# plt.show()
