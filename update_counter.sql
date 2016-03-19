DROP TABLE IF EXISTS temp_table;
CREATE TABLE IF NOT EXISTS temp_table AS (select app_stocks.stock, count(*) counter from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id group by stock);
delete from app_stockcounter;
insert into app_stockcounter(stock,counter) select * from temp_table;
DROP TABLE IF EXISTS temp_table;

CREATE TABLE IF NOT EXISTS temp_table AS (select app_stocks.stock, count(*) counter from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and labeled=1 group by app_stocks.stock);
delete from app_labledcounter;
insert into app_labledcounter (stock,counter) select * from temp_table;
DROP TABLE IF EXISTS temp_table;

CREATE TABLE IF NOT EXISTS temp_table AS (select app_stocks.stock,relevancy, count(*) counter from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and relevancy in ('relevant','irrelevant')  group by app_stocks.stock,relevancy);
delete from app_relevancycounter;
insert into app_relevancycounter (stock,relevancy,counter) select * from temp_table;
DROP TABLE IF EXISTS temp_table;

CREATE TABLE IF NOT EXISTS temp_table AS (select app_stocks.stock,sentiment, count(*) counter from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and sentiment in ('positive','negative','neutral')  group by app_stocks.stock,sentiment);
delete from app_sentimentcounter;
insert into app_sentimentcounter (stock,sentiment,counter) select * from temp_table;
DROP TABLE IF EXISTS temp_table;

CREATE TABLE IF NOT EXISTS temp_table AS (select app_stocks.stock,labeled_user,relevancy,count(*) counter from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and source='twitter.com' group by app_stocks.stock,labeled_user,relevancy having labeled_user !='');
delete from app_usercounter;
insert into app_usercounter(stock,labeled_user,relevancy,counter) select * from temp_table;
insert into app_usercounter(stock,labeled_user,relevancy,counter) select app_stocks.stock,labeled_user_second,relevancy_second,count(*) counter from app_opinion, app_stocks where app_opinion.stock_id=app_stocks.stock_id and source='twitter.com' group by app_stocks.stock,labeled_user_second,relevancy_second having labeled_user_second !='' ;
insert into app_usercounter(stock,labeled_user,relevancy,counter) select app_stocks.stock,labeled_user_third,relevancy_third,count(*) counter from app_opinion, app_stocks where app_opinion.stock_id=app_stocks.stock_id and source='twitter.com' group by app_stocks.stock,labeled_user_third,relevancy_third having labeled_user_third !='' ;
DROP TABLE IF EXISTS temp_table;
