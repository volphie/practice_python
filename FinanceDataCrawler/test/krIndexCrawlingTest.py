import pandas as pd
from datetime import datetime

url = 'http://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=106801&idx_cd=1068&freq=M&period=197001:201706'
dfs = pd.read_html(url, encoding="utf-8")

cols_time = list(dfs[0].columns)
print(cols_time)
cols_time = cols_time[1:-1]
print(cols_time)

# year = int(cols_time[0][0:4])
# month = int(cols_time[0][4:6])
# print(datetime(2000, 1, 1))

cols_time = [datetime(int(time[0:4]),int(time[4:6]),1) for time in cols_time]
print(cols_time)

cols_value =dfs[0].iloc[[0],2:].values.tolist()[0]
print(cols_value)

#  
# row1 = dfs[0].iloc[[0]]
# print(row1)
# row = dfs[0].iloc[[0],2:]
# row.iloc[[0],[-1]]=0
# print(row)
