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

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoWebProject1.settings'
application = get_wsgi_application()


stock_dict={}
for stocks in Stocks.objects.exclude(stock_id__in=[1,2,4,5]).values('stock','stock_id'):
    stock_dict.update({stocks['stock_id']:stocks['stock']})
load_path = os.path.join('data','filter.bin')
f2 = FilterStocks.Filter.load(load_path)
for values in stock_dict.items():
    sid=values[0]
    sname=values[1]
    print('Classifying Stock:' + str(sname))
    tweets = Opinion.objects.filter(stock=sid, relevancy = '', manual_labeled= False).exclude(conversation_reply__isnull=True)[0:1];
    
    label = ['Uncertain', 'relevant', 'irrelevant']
    print(len(tweets))
    for tweet in tweets:
        pred = f2.Classify(tweet.text, stockName= sname)
        print(pred)
        for i in range(len(pred)):
            print(sname, label[pred[i]], tweet.text)

