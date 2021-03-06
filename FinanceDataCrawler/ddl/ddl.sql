CREATE TABLE `stockanalysis`.`stock_price` (
  `TICKER` VARCHAR(10) NOT NULL,
  `TR_DATE` DATETIME NOT NULL,
  `OPEN_PRICE` DECIMAL(10,1) NULL,
  `HIGH_PRICE` DECIMAL(10,1) NULL,
  `LOW_PRICE` DECIMAL(10,1) NULL,
  `CLOSE_PRICE` DECIMAL(10,1) NULL,
  `TR_VOLUME` DECIMAL(10) NULL,
  PRIMARY KEY (`TICKER`, `TR_DATE`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;;
  
CREATE TABLE `stockanalysis`.`stock_ticker` (
  `TICKER` varchar(10) NOT NULL COMMENT '종목 코드',
  `TICKER_NAME` varchar(100) DEFAULT NULL COMMENT '종목명',
  `MARKET` varchar(10) DEFAULT NULL COMMENT '업종코드',
  PRIMARY KEY (`TICKER`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `stockanalysis`.`financial_index2` (
  `FIN_YEAR` DATETIME NOT NULL,
  `TICKER` varchar(10) NOT NULL,
  `REVENUE` decimal(10,1) DEFAULT NULL,
  `OP_INCOME` decimal(10,1) DEFAULT NULL COMMENT '영업이익',
  `INCOME_BFR_TAX` decimal(10,1) DEFAULT NULL,
  `NET_INCOME` decimal(10,1) DEFAULT NULL,
  `NET_INCOME_CON` decimal(10,1) DEFAULT NULL,
  `NET_INCOME_NCON` decimal(10,1) DEFAULT NULL,
  `TOT_ASSET` decimal(10,1) DEFAULT NULL,
  `TOT_DEBT` decimal(10,1) DEFAULT NULL,
  `TOT_EQUITY` decimal(10,1) DEFAULT NULL COMMENT '자본',
  `TOT_EQUITY_CON` decimal(10,1) DEFAULT NULL COMMENT '자본(지배)',
  `TOT_EQUITY_NCON` decimal(10,1) DEFAULT NULL COMMENT '자본(비지배)',
  `CAPITAL_STOCK` decimal(10,1) DEFAULT NULL COMMENT '자본금',
  `OP_CASH_FLOW` decimal(10,1) DEFAULT NULL COMMENT '영업활동현금흐름',
  `INV_CASH_FLOW` decimal(10,1) DEFAULT NULL COMMENT '투자현금흐름',
  `FIN_CASH_FLOW` decimal(10,1) DEFAULT NULL COMMENT '재무활동현금흐름',
  `CAPEX` decimal(10,1) DEFAULT NULL,
  `FCF` decimal(10,1) DEFAULT NULL,
  `INTEREST_DEBT` decimal(10,1) DEFAULT NULL COMMENT '이자발생부채',
  `OP_INCOME_RATE` decimal(7,3) DEFAULT NULL COMMENT '영업이익률',
  `NET_INCOME_RATE` decimal(7,3) DEFAULT NULL COMMENT '순이익률',
  `ROE` decimal(7,3) DEFAULT NULL,
  `ROA` decimal(7,3) DEFAULT NULL,
  `DEBT_RATIO` decimal(7,3) DEFAULT NULL COMMENT '부채비율',
  `RESERVE_RATIO` decimal(7,3) DEFAULT NULL COMMENT '자본유보율',
  `EPS` decimal(10,1) DEFAULT NULL COMMENT '주당수익',
  `PER` decimal(7,3) DEFAULT NULL COMMENT '주가수익률',
  `BPS` decimal(10,1) DEFAULT NULL COMMENT 'Book value Per Share',
  `PBR` decimal(7,3) DEFAULT NULL,
  `DPS` decimal(10,1) DEFAULT NULL COMMENT '주당배당금',
  `DPSP` decimal(7,3) DEFAULT NULL COMMENT '배당수익률',
  `PROP_TO_DIV` decimal(7,3) DEFAULT NULL COMMENT '배당성향',
  `NO_OF_STOCKS` decimal(12,1) DEFAULT NULL COMMENT '발행주식수\n',
  PRIMARY KEY (`FIN_YEAR`,`TICKER`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `stockanalysis`.`macro_economic_index` (
  `INDEX_ID` varchar(10) NOT NULL COMMENT '지표 ID',
  `OBS_TIME` DATETIME NOT NULL COMMENT '관측 기준 시간',
  `FREQ_TYPE` varchar(10) NOT NULL COMMENT '관측 주기 - Yearly, Monthly, Daily',
  `INDEX_NAME` varchar(100) DEFAULT NULL COMMENT '지표 명',
  `VAL` DECIMAL(10,3) DEFAULT NULL COMMENT '값',
  PRIMARY KEY (`INDEX_ID`, `OBS_TIME`,`FREQ_TYPE` )
) ENGINE=InnoDB DEFAULT CHARSET=utf8;