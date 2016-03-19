use kalamacom;

pager > /dev/null
select * from app_stocksprices use index(unique_index2) order by stock,time;
select * from app_opinion use index(unique_index) order by twitter_id,stock;
select * from app_opinion use index(stock_rel) order by stock,relevancy;


CACHE INDEX app_opinion.unique_index IN opinion_cache;
LOAD INDEX INTO CACHE app_opinion;

CACHE INDEX app_stocksprices IN stocksprices_cache;
LOAD INDEX INTO CACHE app_stocksprices;

