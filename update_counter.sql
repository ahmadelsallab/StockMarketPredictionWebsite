DROP TABLE IF EXISTS temp_table;
CREATE TABLE IF NOT EXISTS temp_table AS (select app_stocks.stock,ISNULL(similarId), count(*) counter from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id group by stock,ISNULL(similarId));
delete from app_stockcounter;
alter table app_stockcounter auto_increment = 1;
insert into app_stockcounter(stock,is_original,counter) select * from temp_table;
DROP TABLE IF EXISTS temp_table;

CREATE TABLE IF NOT EXISTS temp_table AS (select app_stocks.stock, count(*) counter from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and labeled=1 group by app_stocks.stock);
delete from app_labledcounter;
alter table app_labledcounter auto_increment = 1;
insert into app_labledcounter (stock,counter) select * from temp_table;
DROP TABLE IF EXISTS temp_table;

CREATE TABLE IF NOT EXISTS temp_table AS (select app_stocks.stock,relevancy, count(*) counter from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and relevancy in ('relevant','irrelevant')  group by app_stocks.stock,relevancy);
delete from app_relevancycounter;
alter table app_relevancycounter auto_increment = 1;
insert into app_relevancycounter (stock,relevancy,counter) select * from temp_table;
DROP TABLE IF EXISTS temp_table;

CREATE TABLE IF NOT EXISTS temp_table AS (select app_stocks.stock,sentiment, ISNULL(NULLIF(similarId,'')),count(*),sum(distinct tweeter_followers_count) counter from app_opinion,app_stocks,app_tweeter where app_opinion.stock_id=app_stocks.stock_id and app_tweeter.tweeter_id=app_opinion.tweeter_id and sentiment in ('positive','negative','neutral')  group by app_stocks.stock,sentiment,ISNULL(NULLIF(similarId,'')));
delete from app_sentimentcounter;
alter table app_sentimentcounter auto_increment = 1;
insert into app_sentimentcounter (stock,sentiment,is_original,counter,follower_counter) select * from temp_table;
DROP TABLE IF EXISTS temp_table;

-- CREATE TABLE IF NOT EXISTS temp_table AS (select stock,sentiment,sum(tweeter_followers_count) from app_opinion,app_stocks,app_tweeter where app_opinion.stock_id=app_stocks.stock_id and app_tweeter.tweeter_id=app_opinion.tweeter_id group by stock,sentiment);
-- delete from app_followerscounter;
-- insert into app_followerscounter(stock,sentiment,sum) select * from temp_table;
-- drop table temp_table;

CREATE TABLE IF NOT EXISTS temp_table AS (select app_stocks.stock,labeled_user,relevancy,count(*) counter from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and source_id=1 and labeled_user !='' group by app_stocks.stock,labeled_user,relevancy);
delete from app_usercounter;
alter table app_usercounter auto_increment = 1;
insert into app_usercounter(stock,labeled_user,relevancy,counter) select * from temp_table;
insert into app_usercounter(stock,labeled_user,relevancy,counter) select app_stocks.stock,labeled_user_second,relevancy_second,count(*) counter from app_opinion, app_stocks where app_opinion.stock_id=app_stocks.stock_id and source_id=1 and labeled_user !='' group by app_stocks.stock,labeled_user_second,relevancy_second;
insert into app_usercounter(stock,labeled_user,relevancy,counter) select app_stocks.stock,labeled_user_third,relevancy_third,count(*) counter from app_opinion, app_stocks where app_opinion.stock_id=app_stocks.stock_id and source_id=1 and labeled_user !='' group by app_stocks.stock,labeled_user_third,relevancy_third;
DROP TABLE IF EXISTS temp_table;

DROP TABLE IF EXISTS temp_table10;
CREATE TABLE `temp_table10` (
  `stock` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `day` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `classifier` varchar(1) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `prediction` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `count` bigint(21) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
insert into temp_table10
select stock,DATE_FORMAT(DATE_ADD(created_at, INTERVAL 8 HOUR),'%Y-%m-%d') day,'r' classifier,p_relevancy prediction,count(*) count from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and p_relevancy is not null and head_opinion = 1 group by stock,p_relevancy,DATE_FORMAT(DATE_ADD(created_at, INTERVAL 8 HOUR),'%Y-%m-%d');
insert into temp_table10 
select stock,DATE_FORMAT(DATE_ADD(created_at, INTERVAL 8 HOUR),'%Y-%m-%d'),'s',p_sentiment,count(*) count from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and p_relevancy = 'relevant' and p_sentiment is not null and head_opinion = 1 group by stock,p_sentiment,DATE_FORMAT(DATE_ADD(created_at, INTERVAL 8 HOUR),'%Y-%m-%d');
insert into temp_table10 
select stock,DATE_FORMAT(DATE_ADD(created_at, INTERVAL 8 HOUR),'%Y-%m-%d'),'q',p_question,count(*) count from app_opinion,app_stocks where app_opinion.stock_id=app_stocks.stock_id and p_question is not null and p_relevancy = 'relevant' and head_opinion = 1 group by stock,p_question,DATE_FORMAT(DATE_ADD(created_at, INTERVAL 8 HOUR),'%Y-%m-%d');
delete from app_predictioncounter;
alter table app_predictioncounter auto_increment = 1;
insert into app_predictioncounter (stock,day,classifier,prediction,counter) select * from temp_table10;
DROP TABLE IF EXISTS temp_table10;

CREATE TABLE `temp_table13` (
  `stock_id` tinyint(3) unsigned DEFAULT NULL,
  `classifier` varchar(3) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `correction` tinyint(1) DEFAULT NULL,
  `segment` bigint(63) DEFAULT NULL,
  `counter` bigint(21) NOT NULL DEFAULT '0',
  `stock_count` int(6) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

set @stock_id_rank = 0;
set @current_stock_id = 3;
set @segment = 1; 
insert into temp_table13 select ranked.stock_id, 'r' classifier, ranked.r_correction correction, ranked.segment, count(*) counter, 0 stock_count
   FROM
     (SELECT r_correction, stock_id, r_correction_time, 
                  @stock_id_rank := IF(@current_stock_id = stock_id, @stock_id_rank + 1, 1) AS stock_id_rank,
                  @current_stock_id := stock_id,
                  @segment := CASE
                  when @stock_id_rank = 1 then 1
                  when (@stock_id_rank - 1) % 100 = 0 then @segment + 1
                  else @segment 
                  END
                  AS segment
       FROM app_opinion where r_correction is not null
       ORDER BY stock_id,r_correction_time DESC
     ) ranked group by stock_id, r_correction, segment;

set @stock_id_rank = 0;
set @current_stock_id = 3;
set @segment = 1; 
insert into temp_table13 select ranked.stock_id, 's' classifier, ranked.s_correction correction, ranked.segment, count(*) counter, 0 stock_count
   FROM
     (SELECT s_correction, stock_id, s_correction_time, 
                  @stock_id_rank := IF(@current_stock_id = stock_id, @stock_id_rank + 1, 1) AS stock_id_rank,
                  @current_stock_id := stock_id,
                  @segment := CASE
                  when @stock_id_rank = 1 then 1
                  when (@stock_id_rank - 1) % 100 = 0 then @segment + 1
                  else @segment 
                  END
                  AS segment
       FROM app_opinion where s_correction is not null and relevancy = 'relevant'
       ORDER BY stock_id,s_correction_time DESC
     ) ranked group by stock_id, s_correction, segment;


set @stock_id_rank = 0;
set @current_stock_id = 3;
set @segment = 1; 
insert into temp_table13 select ranked.stock_id, 'q' classifier, ranked.q_correction correction, ranked.segment, count(*) counter, 0 stock_count
   FROM
     (SELECT q_correction, stock_id, q_correction_time, 
                  @stock_id_rank := IF(@current_stock_id = stock_id, @stock_id_rank + 1, 1) AS stock_id_rank,
                  @current_stock_id := stock_id,
                  @segment := CASE
                  when @stock_id_rank = 1 then 1
                  when (@stock_id_rank - 1) % 100 = 0 then @segment + 1
                  else @segment 
                  END
                  AS segment
       FROM app_opinion where q_correction is not null and relevancy = 'relevant'
       ORDER BY stock_id,q_correction_time DESC
     ) ranked group by stock_id, q_correction, segment;

set @stock_id_rank = 0;
set @current_stock_id = 3;
set @segment = 1;
insert into temp_table13 select ranked.stock_id, 'p' classifier, ranked.p_correction correction, ranked.segment, count(*) counter, 0 stock_count
   FROM
     (SELECT p_correction, stock_id, p_correction_time, 
                  @stock_id_rank := IF(@current_stock_id = stock_id, @stock_id_rank + 1, 1) AS stock_id_rank,
                  @current_stock_id := stock_id,
                  @segment := CASE
                  when @stock_id_rank = 1 then 1
                  when (@stock_id_rank - 1) % 100 = 0 then @segment + 1
                  else @segment 
                  END
                  AS segment
       FROM app_opinion where p_correction is not null and relevancy = 'relevant'
       ORDER BY stock_id,p_correction_time DESC
     ) ranked group by stock_id, p_correction, segment;

insert into temp_table13 select 5 'stock_id', 'r' as 'classifier' ,correction,segment,sum(counter), count(*) stock_count from temp_table13 where classifier='r' group by segment,correction;
insert into temp_table13 select 5 'stock_id', 's' as 'classifier' ,correction,segment,sum(counter), count(*) stock_count from temp_table13 where classifier='s' group by segment,correction;
insert into temp_table13 select 5 'stock_id', 'q' as 'classifier' ,correction,segment,sum(counter), count(*) stock_count from temp_table13 where classifier='q' group by segment,correction;
insert into temp_table13 select 5 'stock_id', 'p' as 'classifier' ,correction,segment,sum(counter), count(*) stock_count from temp_table13 where classifier='p' group by segment,correction;

delete from app_correction;
alter table app_correction auto_increment = 1;
insert into app_correction(stock_id,classifier,correction,segment,counter,stock_count) select * from temp_table13;
DROP TABLE IF EXISTS temp_table13;
