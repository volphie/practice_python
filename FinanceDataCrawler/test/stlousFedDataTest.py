import json, requests
import matplotlib.pyplot as plt
from test.datetimeTest import datetime_from_millis

# WTI crude oil
url = 'https://fred.stlouisfed.org/graph/graph-data.php?recession_bars=on&mode=fred&id=DCOILWTICO'
#     '&fq=Daily&fam=avg&transformation=lin&nd=1986-01-02&ost=-99999&oet=99999&lsv=&lev=&fml=a&fgst=lin&fgsnd=2009-06-01'\
#     '&mma=0&scale=left&line_color=%234572a7&line_style=solid&vintage_date=&revision_date=&chart_type=line&stacking=&drp=0&cosd=&coed=&log_scales='

# Interest rate spread
url2 = 'https://fred.stlouisfed.org/graph/graph-data.php?recession_bars=on&mode=fred&id=T10Y2Y'
#     '&fq=Daily&fam=avg&transformation=lin&nd=1980-06-01&ost=-99999&oet=99999&lsv=&lev=&fml=a&fgst=lin&fgsnd=2009-06-01'\
#     '&mma=0&scale=left&line_color=%234572a7&line_style=solid&vintage_date=&revision_date=&chart_type=line&stacking=&drp=0&cosd=&coed=&log_scales='
    
data = requests.get(url2).json()

obs = data['seriess'][0]['obs']

times = [datetime_from_millis(x[0]) for x in obs]
values = [x[1] for x in obs]

# print(json.dumps(data,indent=2))
# print(times)
# print(values)
plt.plot(times, values)
plt.show()