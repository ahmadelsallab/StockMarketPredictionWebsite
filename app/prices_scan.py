from datetime import datetime
from app.models import Opinion,Stocks,StocksPrices
from django.utils import timezone
from Filter.Filter import Filter
import threading, time
import datetime
from django.utils import timezone
from datetime import date, datetime, timedelta
import datetime
import os
import re


import django
django.setup()

for x in Stocks.objects.filter().exclude(stock=None).exclude(stock='none').exclude(stock=''):
    line = x.stock_id
    stock_name = x.stock
    #tweetes_to_render = Opinion.objects.filter(stock=line,created_at__isnull=False,stocksprices_id__isnull=True).order_by('-created_at');
    month_ago = timezone.now() - timedelta(days=30)
    tweetes_to_render = Opinion.objects.filter(stock=line,created_at__gt=month_ago,stocksprices_id__isnull=True).order_by('-id')[0:1000];
    print(str(stock_name) + ": Number of tweetes: " + str(len(tweetes_to_render)))
    if len(tweetes_to_render) > 0:
        price_list = StocksPrices.objects.filter(stock=line).order_by('-id')
        c=0
        for x in range(0,len(tweetes_to_render)):
            tweet_time=tweetes_to_render[x].created_at+timedelta(hours=3)
            done = False
            
            while c < len(price_list) and not done:
                if(tweet_time > price_list[c].time):
                    #print(str(tweetes_to_render[x].twitter_id) + ' price ID is ' + str(price_list[c].id))
                    done = True
                    tweetes_to_render[x].stocksprices_id = price_list[c].id
                    tweetes_to_render[x].save()
                else:
                    c=c+1
