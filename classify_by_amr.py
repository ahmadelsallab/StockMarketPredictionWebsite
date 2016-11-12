from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax
from app.models import Sources, Sectors, Stocks, Tweeter, Opinion, CorrectionData, StocksPrices, LabledCounter, StockCounter, RelevancyCounter, SentimentCounter, DailyPrices, WeeklyPrices, UserCounter
from django.utils import timezone
from Filter.Filter import Filter
from bs4 import BeautifulSoup
from django.db.models import Sum
from random import randint
from django.forms.models import model_to_dict
import urllib
import json
from TwitterCrawler.TwitterCrawler import *
import os
import threading
import django_crontab
#from pytz import timezone
from dateutil.parser import parse
from requests_oauthlib import OAuth1
import requests
import urllib.parse as urllib_parse
from twitter import *
import re
import gc
import subprocess
from django.http import HttpResponse, JsonResponse
import os
from Filter import FilterStocks

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoWebProject1.settings'
application = get_wsgi_application()


stock_dict={}
for stocks in Stocks.objects.exclude(stock_id__in=[1,2,4,5]).values('stock','stock_id'):
    stock_dict.update({stocks['stock_id']:stocks['stock']})

for values in stock_dict.items():
    sid=values[0]
    sname=values[1]
    print('Classifying Stock:' + str(sname))
    tweets = Opinion.objects.filter(stock=sid, relevancy = '', manual_labeled= False).exclude(conversation_reply__isnull=True)[0:1];
    outf = open(os.path.join('data','filter_output.txt'), 'w')
    load_path = os.path.join('data','filter.bin')
    f2 = FilterStocks.Filter.load(load_path)
    label = ['Uncertain', 'relevant', 'irrelevant']
    for tweet in tweets:
        pred = f2.Classify(tweet.text, stockName= sname)
        print(pred)
        for i in range(len(pred)):
            print(sname, label[pred[i]], tweet.text)

