import re
import os
import pandas as pd
from connection import engine
from connection import query_stock_tickers

'''
get_date_str(s) - 문자열 s 에서 "YYYY/MM" 문자열 추출
'''
def get_date_str(s):
    date_str = ''
    r = re.search("\d{4}/\d{2}", str(s))
    if r:
        date_str = r.group()
        date_str = date_str.replace('/', '-')
    
    return date_str

'''
컬럼 헤더 형식이 원래의 소스와 달라 시작하는 괄호와 종료되는 괄호를 삭제하도록 문자열 변경
패턴 : (***,)
정규표현식을 사용하려 했으나, 여의치 않아 그냥 문자열 변경
'''
def get_col_str(s):
# col_str = ''
# r = re.search("",str(s))
# if r:
# col_str = r.group()
#
# return col_str;
    col_str = str(s)
    col_str = 'date' if col_str == "'date'" else col_str[2:-3]
# print(col_str)

    return col_str

'''
@ Arguments
* code: 종목코드
* fin_type = '0': 재무제표 종류 (0: 주재무제표, 1: GAAP개별, 2: GAAP연결, 3: IFRS별도, 4:IFRS연결)
* freq_type = 'Y': 기간 (Y:년, Q:분기)

@ return
 DataFrame 재무재표 정보
'''
def get_finstate_naver(code, fin_type='0', freq_type='Y'):
    url_tmpl = 'http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?' \
    'cmp_cd=%s&fin_typ=%s&freq_typ=%s'
    
    url = url_tmpl % (code, fin_type, freq_type)
    #print(url)

    dfs = pd.read_html(url, encoding="utf-8")
    df = dfs[0]
    if df.ix[0,0].find('해당 데이터가 존재하지 않습니다') >= 0:
        return None

    df.rename(columns={'주요재무정보':'date'}, inplace=True)
    df.set_index('date', inplace=True)

    cols = list(df.columns)

    if '연간' in cols: cols.remove('연간')
    if '분기' in cols: cols.remove('분기')
    cols = [get_date_str(x) for x in cols]

    # This line is attached to the original source
    cols = cols[:-1]

    df = df.ix[:, :-1]
    df.columns = cols
    dft = df.T
    dft.index = pd.to_datetime(dft.index)

    # These lines are attached to the original source
    cols = list(dft.columns)
    cols = [get_col_str(x) for x in cols]
    dft.columns = cols
    #dft.set_index('date', inplace=True)

    # remove if index is NaT
    dft = dft[pd.notnull(dft.index)]
    # Add 종목코드 column to the table
    dft.insert(0,'종목코드', code)
    
    #print(dft)
    return dft

'''
@ Arguments
 ticker(종목코드)를 파라미터로 받아

@ Description
  같은 이름의 csv 파일을 DB에 로딩하는 batch 파일을 실행시킴
'''
def load_file_to_financial_index_table(ticker):
    cmd = "E:/eclipse-workspace/FinanceDataCrawler/bin/load.cmd {0}.csv".format(ticker)
    os.system(cmd)


def save_to_financial_index_table(df):
#     engine = create_engine('mysql+pymysql://volphie:jjo12345@localhost/stockanalysis?charset=utf8')
#     df = get_finstate_naver(ticker)
    cols = ['TICKER', 'REVENUE', 'OP_INCOME', 'INCOME_BFR_TAX', 'NET_INCOME', 'NET_INCOME_CON', 'NET_INCOME_NCON', \
          'TOT_ASSET', 'TOT_DEBT', 'TOT_EQUITY' , 'TOT_EQUITY_CON' , 'TOT_EQUITY_NCON' , 'CAPITAL_STOCK', 'OP_CASH_FLOW' , \
          'INV_CASH_FLOW' , 'FIN_CASH_FLOW' , 'CAPEX' , 'FCF' , 'INTEREST_DEBT' , 'OP_INCOME_RATE' , 'NET_INCOME_RATE' , \
          'ROE' , 'ROA' , 'DEBT_RATIO' , 'RESERVE_RATIO' , 'EPS', 'PER', 'BPS', 'PBR', 'DPS', 'DPSP', 'PROP_TO_DIV' , 'NO_OF_STOCKS']
    df.columns = cols
    df.insert(0, 'FIN_YEAR', df.index)
#     print(df)
    df.to_sql('financial_index', engine, if_exists='append', index=False)


# path = Path(os.getcwd()+'\data\krx_stock_list.csv')
# print(path)
# Read stock ticker
# df = pd.read_csv(os.getcwd()+'\data\krx_stock_list.csv', dtype=object)
# cols = df['종목코드']
# print(cols)
# i = 0
# for ticker in cols:
#     # Query financial information by stock ticker and save to each file named after the ticker
#     dfa = get_finstate_naver(ticker)
#     i = i + 1
# # print(dfa)
# # result_file =
# # print(result_file)
#     dfa.to_csv('{0}\\result\{1}.csv'.format(os.getcwd(), ticker))
#     print('{0}. {1}.csv file was saved'.format(i, ticker))
#     load_file_to_financial_index_table(ticker)
df = query_stock_tickers()
for index, row in df.iterrows() :
    try:
        data = get_finstate_naver(row['TICKER'])
        save_to_financial_index_table(data)
        print("{0}. {1} is saved to the table financial_index ...".format(index, row['TICKER']))
    except :
        print("[Exception] Error occurs during handling {0}'s financial index data".format(row['TICKER']))
        pass
# save_to_financial_index_table('000020')
