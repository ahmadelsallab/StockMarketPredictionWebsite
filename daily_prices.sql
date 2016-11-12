SET group_concat_max_len=15000;
CREATE TABLE IF NOT EXISTS temp_table5 AS (select app_stocks.stock, DATE_FORMAT(time,'%Y-%m-%d'), min(close),max(close),GROUP_CONCAT(distinct close ORDER BY app_stocksprices.id desc) from app_stocksprices,app_stocks where time <> '2000-01-01 00:00:00' and app_stocksprices.stock_id=app_stocks.stock_id group by app_stocks.stock,DATE_FORMAT(time,'%Y-%m-%d'));
delete from app_dailyprices;
insert into app_dailyprices (stock,day,min,max,concat) select * from temp_table5;
DROP TABLE IF EXISTS temp_table5;


CREATE TABLE IF NOT EXISTS temp_table6 AS (select app_stocks.stock, DATE_FORMAT(created_at,'%Y-%m-%d'), sentiment,count(*) from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and sentiment <> '' group by app_stocks.stock,DATE_FORMAT(created_at,'%Y-%m-%d'),sentiment);
delete from app_dailysentiment;
insert into app_dailysentiment (stock,day,sentiment,counter) select * from temp_table6;
DROP TABLE IF EXISTS temp_table6;
