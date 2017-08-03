import os

#cmd = '\"C:/Program Files (x86)/MySQL/MySQL Server 5.7/bin/mysql\" -uroot -p --local-infile scrapping -e \"LOAD DATA LOCAL INFILE \'E:/eclipse-workspace/FinanceDataCrawler/result/000020.csv\'  INTO TABLE financial_index  FIELDS TERMINATED BY \',\' LINES TERMINATED BY \'\n\' IGNORE 1 ROWS\"'
cmd = "E:/eclipse-workspace/FinanceDataCrawler/bin/load.cmd 095570.csv"
os.system(cmd)