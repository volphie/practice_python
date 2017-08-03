select state.TICKER,
	(select TICKER_NAME from stock_ticker where TICKER = state.TICKER) as TICKER_NAME,
	state.IV, 
	price.CLOSE_PRICE, 
    (state.IV - price.CLOSE_PRICE)/price.CLOSE_PRICE*100 as DIFF
from
	(
		select t.TICKER, ((t.EPSY+t.EPSY_1+t.EPSY_2)/10 + t.BPSY)/2 as IV 
		from (
		select TICKER,
			sum(case when year(FIN_YEAR) = '2017' then EPS*10 end ) as 'EPSY',
			sum(case when year(FIN_YEAR) = '2016' then EPS*10 end ) as 'EPSY_1',
			sum(case when year(FIN_YEAR) = '2015' then EPS*10 end ) as 'EPSY_2',
			sum(case when year(FIN_YEAR) = '2017' then BPS end ) as 'BPSY'
		from financial_index
		group by TICKER
		order by TICKER
		) t
	) state,
	(
		select l.TICKER, l.CLOSE_PRICE
		from stock_price l,(
			select TICKER, max(TR_DATE) as TR_DATE
			from stock_price
			group by TICKER) r
		where l.TICKER = r.TICKER
		and l.TR_DATE = r.TR_DATE
	) price
where state.TICKER = price.TICKER
-- and state.IV > price.CLOSE_PRICE
-- and state.IV > 0
and state.TICKER = '001720'
order by DIFF DESC;