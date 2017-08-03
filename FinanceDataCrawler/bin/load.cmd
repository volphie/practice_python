echo off

IF %1.==. GOTO ERROR

echo "The file %1 is loading....."
c:
cd "C:\Program Files (x86)\MySQL\MySQL Server 5.7\bin"
mysql -uvolphie -pjjo12345 --local-infile stockanalysis -e "LOAD DATA LOCAL INFILE 'E:/eclipse-workspace/FinanceDataCrawler/result/%1'  INTO TABLE financial_index  FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS"
GOTO EXIT

:ERROR
echo "File name is required!!"

:EXIT
echo "Program exits"