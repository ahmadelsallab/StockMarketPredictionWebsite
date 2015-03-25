CREATE TEMPORARY TABLE IF NOT EXISTS temp_table AS (select  stock, count(*) counter from app_opinion group by stock);
delete from app_stockcounter;
insert into app_stockcounter(stock,counter) select * from temp_table;
DROP TEMPORARY TABLE IF EXISTS temp_table;

CREATE TEMPORARY TABLE IF NOT EXISTS temp_table AS (select  stock, count(*) counter from app_opinion where labeled=1 group by stock);
delete from app_labledcounter;
insert into app_labledcounter (stock,counter) select * from temp_table;
DROP TEMPORARY TABLE IF EXISTS temp_table;

CREATE TEMPORARY TABLE IF NOT EXISTS temp_table AS (select stock,relevancy, count(*) counter from app_opinion where relevancy !='none'  group by stock,relevancy);
delete from app_relevancycounter;
insert into app_relevancycounter (stock,relevancy,counter) select * from temp_table;
DROP TEMPORARY TABLE IF EXISTS temp_table;

CREATE TEMPORARY TABLE IF NOT EXISTS temp_table AS (select stock,sentiment, count(*) counter from app_opinion where sentiment !='none'  group by stock,sentiment);
delete from app_sentimentcounter;
insert into app_sentimentcounter (stock,sentiment,counter) select * from temp_table;
DROP TEMPORARY TABLE IF EXISTS temp_table;
