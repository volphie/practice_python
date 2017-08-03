import pandas as pd


url = 'http://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=107301&idx_cd=1073&freq=M&period=199701:201706'
dfs = pd.read_html(url, encoding="utf-8")

print(dfs.T)