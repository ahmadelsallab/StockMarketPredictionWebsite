from Filter import FilterStocks
from datetime import datetime
from app.models import Sources, Stocks, Opinion, Tweeter
from django.utils import timezone
from Filter.Filter import Filter
import threading, time
import datetime
import unicodedata
import os

import django
django.setup()


stock_dict={}
label = {0:'Uncertain', 1:'relevant', 2:'irrelevant',4:None}
#for stocks in Stocks.objects.exclude(stock_id__in=[1,2,4,5]).values('stock','stock_id'):
for stocks in Stocks.objects.exclude(stock_id__in=[1,2,4,5]).values('stock','stock_id'):
#for stocks in Stocks.objects.filter(stock_id__in=[81]).values('stock','stock_id'):
    stock_dict.update({stocks['stock_id']:stocks['stock']})

# issue with stock 81

save_path = 'data'
#FilterStocks.Filter.init(save_path)

for values in stock_dict.items():
    sid=values[0]
    sname=values[1]
    print('Classifying Stock:' + str(sname))
    tweets = Opinion.objects.filter(stock=sid, relevancy = '', p_relevancy=None).filter(head_opinion = True).order_by('-created_at');
    print(len(tweets))
    for x in range(0,len(tweets)):
        print("###########################")
        print(sname)
        pred = FilterStocks.Filter.classify([tweets[x].text],sid,save_path)
        print(tweets[x].text)
        print(pred)
        p_relevancy=pred[0]
        tweets[x].r_correction=None
        tweets[x].s_correction=None
        tweets[x].q_correction=None
        tweets[x].p_correction=None
        tweets[x].p_relevancy=label[p_relevancy]
        tweets[x].save()
