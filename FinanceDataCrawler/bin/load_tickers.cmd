echo off

c:
cd "C:\Program Files (x86)\MySQL\MySQL Server 5.7\bin"
mysql -uvolphie -pjjo12345 --local-infile stockanalysis -e "LOAD DATA LOCAL INFILE 'E:/eclipse-workspace/FinanceDataCrawler/data/krx_stock_list.csv'  INTO TABLE stock_ticker FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (@col1,@col2,@col3,@col4) set ticker=@col2, ticker_name=@col3, sector_code=@col4"
