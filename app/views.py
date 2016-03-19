﻿"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax
from app.models import Sectors, Stocks, Tweeter, Opinion, CorrectionData, StocksPrices, LabledCounter, StockCounter, RelevancyCounter, SentimentCounter, DailyPrices, WeeklyPrices, UserCounter
from django.utils import timezone
from Filter.Filter import Filter
from bs4 import BeautifulSoup
from django.db.models import Sum
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


request_token_url = 'https://api.twitter.com/oauth/request_token'
access_url = 'https://api.twitter.com/oauth/access_token'
authenticate_url = 'https://api.twitter.com/oauth/authenticate'
base_authorization_url = 'https://api.twitter.com/oauth/authorize'

consumerKey="xNRGvHoz9L4xKGP28m7qbg"
consumerSecret="oFv4dhBekboNg7pKa2BS0zztHqusr91SIdmKErDaycI"
accessToken="1846277677-36dTObVu6LfVDSuU72M3HCTCv2g50dYoTxzuAOZ"
accessTokenSecret="Yu4lZdbebuO3tpof6xYzi4Qy7HZL4aL3YQiCYgsro"
resource_owner_key = ""
resource_owner_secret = ""


class NewsItem:
    title = ""
    link = ""
    pubDate = ""
    
def isNumber(value):
    try:
        float(value)
        return True
    except ValueError:
        return False 
    
    
@ajax
def get_stocks_weights(request):
    content_return = []
    for stocks in Stocks.objects.filter().exclude(stock=None).exclude(stock='none').exclude(stock='').exclude(stock='ﺕﺎﺴﻳ').select_related('sector'):
        try:
            weight = StockCounter.objects.filter(stock=stocks.stock).values()[0]['counter']
        except:
            weight = 0
        sector = stocks.sector.sector
        content_return.append({'text':stocks.stock, 'weight':weight,'html':{'class':sector}})

    return content_return

    
def index(request):
    """Renders the home page."""
    if 'message' in request.session:
        message = request.session['message']
        del request.session['message']
    if 'error' in request.session:
        message = request.session['error']
        del request.session['error']

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'message': message if 'message' in locals() else "",
            'error': message if 'error' in locals() else "",
        })
    )

def index_proto(request):
    """Renders the home page."""
    if 'message' in request.session:
        message = request.session['message']
        del request.session['message']
    if 'error' in request.session:
        message = request.session['error']
        del request.session['error']

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index_proto.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'message': message if 'message' in locals() else "",
            'error': message if 'error' in locals() else "",
        })
    )


#@login_required
def home(request):
    '''
    from twython import Twython
    global twitter
    twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")
    '''
    if(request.user.is_authenticated()):
        # Start the TwitterCrawler      
        PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        configFileCrawler = os.path.join(PROJECT_DIR, 'TwitterCrawler','Configurations', 'Configurations.xml')
        global twitterCrawler
        twitterCrawler = TwitterCrawler(configFileCrawler, None, None, None)
        #results = twitterCrawler.SearchQueryAPI(query, -1, -1)
    
        return render(
            request,
            'app/home.html',
            context_instance = RequestContext(request,
            {
                'title':'Home',
                #'tweets': tweets,
            })
        )
    else:
        return redirect('/register')

#@login_required
def home_proto(request):
    '''
    from twython import Twython
    global twitter
    twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")
    '''
    try:
        if(request.session.get('user_authenticated')):
        
            # Start the TwitterCrawler      
            PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
            configFileCrawler = os.path.join(PROJECT_DIR, 'TwitterCrawler','Configurations', 'Configurations.xml')
            global twitterCrawler
            twitterCrawler = TwitterCrawler(configFileCrawler, None, None, None)
            #results = twitterCrawler.SearchQueryAPI(query, -1, -1)
        
            return render(
                request,
                'app/home_proto.html',
                context_instance = RequestContext(request,
                {
                    'title':'Home',
                    #'tweets': tweets,
                })
            )
    
        else:
            return redirect('/prototype')
    except:
        return redirect('/prototype')

#@login_required
def home_filtered(request):
    '''
    from twython import Twython
    global twitter
    twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")
    '''
    # Start the TwitterCrawler      
    PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    configFileCrawler = os.path.join(PROJECT_DIR, 'TwitterCrawler','Configurations', 'Configurations.xml')
    global twitterCrawler
    twitterCrawler = TwitterCrawler(configFileCrawler, None, None, None)
    #results = twitterCrawler.SearchQueryAPI(query, -1, -1)

    return render(
        request,
        'app/home_filtered.html',
        context_instance = RequestContext(request,
        {
            'title':'Home filtered',
            #'tweets': tweets,
        })
    )


@ajax
def get_prices_line(request):
    stock_name = request.POST['query']
    content_return = {}
    prices = DailyPrices.objects.filter(stock=stock_name).values()
    content_return = [];
    for price in prices:
        l=price['concat'].split(',')
        close=l[0]
        content_return.append([price['day'],float(close)]);

    return content_return[-50:];

@ajax
def get_prices_candle(request):
    stock_name = request.POST['query']
    print("Start get_prices_candle")
    content_return = {}
    prices = DailyPrices.objects.filter(stock=stock_name).values()
    content_return = [];
    for price in prices:
        l=price['concat'].split(',')
        close=l[0]
        open=l[-1]
        #print(price['day'])
        #print(price['min'])
        #print(price['max'])
        #print(open)
        #print(close)
        content_return.append([price['day'],float(price['min']),float(open),float(close),float(price['max']),'<b>'+price['day']+'</b>   O:'+open+' H:'+price['max']+' L:'+price['min']+' C:'+close]);
    print("End get_prices_candle")
    return content_return[-50:];

@ajax
def get_stock_volume(request):
    stock_name = request.POST['query']
    content_return = []
    print("Start get_stock_volume")
    now_time = timezone.now()
    start_point = timezone.datetime(now_time.year, now_time.month, now_time.day, 8, 0, 0,)
    graph_point = start_point
    end_point = timezone.datetime(now_time.year, now_time.month, now_time.day, 17, 0, 0,)
    one_hour = timezone.timedelta(hours=1)
    stock_id = Stocks.objects.filter(stock=stock_name)[0].stock_id
    all_tweets = Opinion.objects.filter(stock=stock_id).exclude(created_at=None).values().order_by('-id')
    while(graph_point <= end_point):
        prev_graph_point = graph_point
        graph_point += one_hour
        
        w = count_number_tweets_in_range(all_tweets, prev_graph_point, graph_point)
        # FIX: convert the prev_graph_point into the Saudi timezone. See http://stackoverflow.com/questions/1398674/python-display-the-time-in-a-different-time-zone
        # All timezones names can be found at: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        # Saudi is: 'Asia/Riyadh'
        content_return.append([{'v':[prev_graph_point.hour,0,0],'f':str(prev_graph_point.hour)}, w])

    print("End get_stock_volume")
    return content_return;

@ajax
def get_stock_col_rel_info(request):
    stock_name = request.POST['query']
    content_return = []
    print("Start get_stock_col_rel_info")
    now_time = timezone.now()
    start_point = timezone.datetime(now_time.year, now_time.month, now_time.day, 8, 0, 0,)
    graph_point = start_point
    end_point = timezone.datetime(now_time.year, now_time.month, now_time.day, 17, 0, 0,)
    one_hour = timezone.timedelta(hours=1)
    stock_id = Stocks.objects.filter(stock=stock_name)[0].stock_id
    rel_tweets = Opinion.objects.filter(stock=stock_id, voted_relevancy='Relevant').values().order_by('-id')
    irrel_tweets = Opinion.objects.filter(stock=stock_id, voted_relevancy='Irrelevant').values().order_by('-id')
    while(graph_point <= end_point):
        prev_graph_point = graph_point
        graph_point += one_hour
        
        rel_count = count_number_tweets_in_range(rel_tweets, prev_graph_point, graph_point)
        irrel_count = count_number_tweets_in_range(irrel_tweets, prev_graph_point, graph_point)
        # FIX: convert the prev_graph_point into the Saudi timezone. See http://stackoverflow.com/questions/1398674/python-display-the-time-in-a-different-time-zone
        # All timezones names can be found at: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        # Saudi is: 'Asia/Riyadh'
        content_return.append([{'v':[prev_graph_point.hour,0,0],'f':str(prev_graph_point.hour)}, rel_count, irrel_count])

    print("End get_stock_col_rel_info")
    return content_return;

@ajax
def get_stock_col_sent_info(request):
    stock_name = request.POST['query']
    content_return = []
    print("Start get_stock_col_sent_info")
    now_time = timezone.now()
    start_point = timezone.datetime(now_time.year, now_time.month, now_time.day, 8, 0, 0,)
    graph_point = start_point
    end_point = timezone.datetime(now_time.year, now_time.month, now_time.day, 17, 0, 0,)
    one_hour = timezone.timedelta(hours=1)
    stock_id = Stocks.objects.filter(stock=stock_name)[0].stock_id
    pos_tweets = Opinion.objects.filter(stock=stock_id, voted_sentiment='Positive').values().order_by('-id')
    neg_tweets = Opinion.objects.filter(stock=stock_id, voted_sentiment='Negative').values().order_by('-id')
    neu_tweets = Opinion.objects.filter(stock=stock_id, voted_sentiment='Neutral').values().order_by('-id')
    while(graph_point <= end_point):
        prev_graph_point = graph_point
        graph_point += one_hour
        
        pos_count = count_number_tweets_in_range(pos_tweets, prev_graph_point, graph_point)
        neg_count = count_number_tweets_in_range(neg_tweets, prev_graph_point, graph_point)
        neu_count = count_number_tweets_in_range(neu_tweets, prev_graph_point, graph_point)
        # FIX: convert the prev_graph_point into the Saudi timezone. See http://stackoverflow.com/questions/1398674/python-display-the-time-in-a-different-time-zone
        # All timezones names can be found at: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        # Saudi is: 'Asia/Riyadh'
        content_return.append([{'v':[prev_graph_point.hour,0,0],'f':str(prev_graph_point.hour)}, pos_count, neg_count, neu_count])

    print("End get_stock_col_sent_info")
    return content_return;

@ajax
def get_overall_rel_info(request):

    content_return = []
    print("Start get_overall_rel_info")
    #all_tweets = Opinion.objects.filter(stock=stock_name).values().order_by('-id')
    try:
        rel_count = RelevancyCounter.objects.extra(where={"`relevancy` = 'relevant' "}).values()[0]['counter']
    except:
        rel_count = 10
    try:
        irrel_count = RelevancyCounter.objects.extra(where={"`relevancy` = 'irrelevant' "}).values()[0]['counter']
    except:
        irrel_count = 10
    
    content_return.append(['Relevant', rel_count])
    content_return.append(['Irrelevant', irrel_count])
    print("End get_overall_rel_info")

    return content_return;
@ajax
def get_overall_sent_info(request):
    content_return = []
    #all_tweets = Opinion.objects.filter(stock=stock_name).values().order_by('-id')
    print("Start get_overall_sent_info")
    try:
        pos_count = SentimentCounter.objects.extra(where={"`sentiment` = 'positive' "}).values()[0]['counter']
    except:
        pos_count = 10
    try:
        neg_count = SentimentCounter.objects.extra(where={"`sentiment` = 'negative' "}).values()[0]['counter']
    except:
        neg_count = 10
    try:
        neu_count = SentimentCounter.objects.extra(where={"`sentiment` = 'neutral' "}).values()[0]['counter']
    except:
        neu_count = 10
    
    content_return.append(['Positive', pos_count])
    content_return.append(['Negative', neg_count])
    content_return.append(['Neutral', neu_count])

    print("End get_overall_sent_info")
    return content_return;  

@ajax
def get_stock_rel_info(request):
    stock_name = request.POST['query']
    content_return = []
    print("Start get_stock_rel_info")
    #all_tweets = Opinion.objects.filter(stock=stock_name).values().order_by('-id')
    try:
        rel_count = RelevancyCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `relevancy` = 'relevant' "}).values()[0]['counter']
    except:
        rel_count = 10
    try:
        irrel_count = RelevancyCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `relevancy` = 'irrelevant' "}).values()[0]['counter']
    except:
        irrel_count = 10
    
    content_return.append(['Relevant', rel_count])
    content_return.append(['Irrelevant', irrel_count])
    print("End get_stock_rel_info")

    return content_return;

@ajax
def get_stock_sent_info(request):
    stock_name = request.POST['query']
    content_return = []
    print("Start get_stock_sent_info")

    #all_tweets = Opinion.objects.filter(stock=stock_name).values().order_by('-id')
    try:
        pos_count = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'positive' "}).values()[0]['counter']
    except:
        pos_count = 10
    try:
        neg_count = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'negative' "}).values()[0]['counter']
    except:
        neg_count = 10
    try:
        neu_count = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'neutral' "}).values()[0]['counter']
    except:
        neu_count = 10
    
    content_return.append(['Positive', pos_count])
    content_return.append(['Negative', neg_count])
    content_return.append(['Neutral', neu_count])
    print("End get_stock_sent_info")

    return content_return;    

def count_number_tweets_in_range(all_tweets, prev_graph_point, graph_point):
    w = 0
    for tweet in all_tweets:
        #tweet_time_stamp = datetime.datetime.strptime(tweet['pub_date'], '%Y-%m-%d %H:%M:%S.%f+00:00')
        if tweet['created_at'] != None:
            tweet_time_stamp = tweet['created_at'].replace(tzinfo=None)
        else:
            tweet_time_stamp = None
        #tweetes_to_render[x].created_at+timedelta(hours=3)
        if((tweet_time_stamp >= prev_graph_point) and (tweet_time_stamp <= graph_point)):
            w += 1
    return w

@ajax
def get_overall_stats(request):
    content_return  = {}
    # Fill in total number of entries in DB for this stock
    # Full DB
    content_return['total_entries_in_DB'] = StockCounter.objects.aggregate(Sum('counter'))['counter__sum']
    if(LabledCounter.objects.aggregate(Sum('counter'))['counter__sum'] != None):
        content_return['total_labeled_entries_in_DB'] = LabledCounter.objects.aggregate(Sum('counter'))['counter__sum']
    else:
        content_return['total_labeled_entries_in_DB'] = 0
    content_return['total_relevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`relevancy` = 'relevant' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_irrelevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`relevancy` = 'irrelevant' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_positive_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'positive' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_negative_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'negative' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_neutral_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'neutral' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['user_total_labels_in_DB'] = UserCounter.objects.filter(labeled_user=request.user.username).aggregate(Sum('counter'))['counter__sum']
    return content_return

#@login_required


def runUpdate():
    subprocess.Popen(['sh','/project/DjangoWebProject1_20150924/update_counter.sh']);

@ajax
def update_counters(request):
    d = threading.Thread(target=runUpdate);
    d.start();

@ajax
def get_tweets(request):
    stock_name = request.POST['query']
    start_time = request.POST['start']
    end_time = request.POST['end']
    content_return = {}
    print(start_time)
    stock_id = Stocks.objects.filter(stock=stock_name)[0].stock_id

    try:
        price_list = StocksPrices.objects.filter(stock=stock_id).order_by('-id')
        price = price_list[0].close
        print('Price in DB')
    except:
        price = 0

    from django.utils import timezone 
    content_return['price'] = price

    if start_time == '' and end_time == '':
        tweetes_to_render=list(Opinion.objects.filter(stock=stock_id, labeled = False, manual_labeled= False, similarId='',created_at__isnull=False,stocksprices_id__isnull=False).exclude(labeled_user=request.user.username).select_related('tweeter').select_related('stocksprices').order_by('-created_at')[0:500]);
    elif start_time != '' and end_time == '':
        tweetes_to_render=list(Opinion.objects.filter(stock=stock_id, labeled = False, manual_labeled= False,similarId='',created_at__gte=start_time,created_at__isnull=False,stocksprices_id__isnull=False).exclude(labeled_user=request.user.username).select_related('tweeter').select_related('stocksprices').order_by('-created_at')[0:500]);
    elif start_time == '' and end_time != '':
        tweetes_to_render=list(Opinion.objects.filter(stock=stock_id, labeled = False, manual_labeled= False, similarId='',created_at__lte=end_time,created_at__isnull=False,stocksprices_id__isnull=False).exclude(labeled_user=request.user.username).select_related('tweeter').select_related('stocksprices').order_by('-created_at')[0:500]);
    elif start_time != '' and end_time != '':
        tweetes_to_render=list(Opinion.objects.filter(stock=stock_id, labeled = False, manual_labeled= False,similarId='',created_at__range=[start_time, end_time],created_at__isnull=False,stocksprices_id__isnull=False).exclude(labeled_user=request.user.username).select_related('tweeter').select_related('stocksprices').order_by('-created_at')[0:500]);

    #prevent Duplicate 
    tweets_dict = {}
    tweets_dict[''] = ''
    i = 1
    x = 0
    print(len(tweetes_to_render))
    print('Handling duplicates')
    content_return['statuses'] = [[] for m in range(min(150, len(tweetes_to_render)))]
    #content_return['statuses'] = []
    while x < min(150, len(tweetes_to_render)):
        tweet_render=tweetes_to_render[x];
        tweet_render_text=tweet_render.text.strip()
        tweet_render_text=re.sub(r"RT @\w*\w: ", '', tweet_render_text, flags=re.MULTILINE)
        tweet_render_text=re.sub(r'\.\.\.', '', tweet_render_text, flags=re.MULTILINE)
        try:
            urls=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet_render_text);
            for i in range(0,len(urls)):
                rep='r\''+urls[i]+'\''
                tweet_render_text=re.sub(r""+urls[i]+"", '', tweet_render_text, flags=re.MULTILINE)
        except:
            pass
        
        #print(x) 
        if tweet_render_text in tweets_dict.keys():
            #tweet = Opinion.objects.filter(twitter_id=tweet_render.get('twitter_id'))[0]
            #tweet.similarId = tweets_dict[tweet_render_text]
            #tweet.save();
            tweetes_to_render.pop(x); 
            #if (len(tweetes_to_render) > 150+i):
            #    tweetes_to_render.append(tweetes_to_render[149+i])
            #    i=i+1
        elif(tweet_render.labeled_user == request.user.username or tweet_render.labeled_user_second == request.user.username) and request.user.username != '':
            tweetes_to_render.remove(tweet_render)
            #if (len(tweetes_to_render) > 150+i):
            #    tweetes_to_render.append(tweetes_to_render[149+i])
            #    i=i+1
        else:
            #content_return['statuses'].append(model_to_dict(tweetes_to_render[x]))
            content_return['statuses'][x] = model_to_dict(tweetes_to_render[x]);
            content_return['statuses'][x]['created_at']=tweetes_to_render[x].created_at.strftime('%a %b %d %X %z %Y');
            content_return['statuses'][x]['user_followers_count']=tweetes_to_render[x].tweeter.tweeter_followers_count;
            content_return['statuses'][x]['user_profile_image_url']=tweetes_to_render[x].tweeter.tweeter_profile_image_url;
            content_return['statuses'][x]['user_location']=tweetes_to_render[x].tweeter.tweeter_location;
            content_return['statuses'][x]['tweeter_name']=tweetes_to_render[x].tweeter.tweeter_name;
            content_return['statuses'][x]['tweeter_sname']=tweetes_to_render[x].tweeter.tweeter_sname;
            content_return['statuses'][x]['price_time_then']=tweetes_to_render[x].stocksprices.time.strftime('%a %b %d %I:%M %p');
            content_return['statuses'][x]['price_then']=tweetes_to_render[x].stocksprices.close
            try:
                if tweetes_to_render[x].conversation_reply != '' and tweetes_to_render[x].conversation_reply != None:
                    #print(tweetes_to_render[x]['conversation_reply'])
                    tweet = Opinion.objects.filter(stock=stock_id,twitter_id=tweetes_to_render[x].conversation_reply).select_related('stocksprices').select_related('tweeter')[0]
                    content_return['statuses'].append([]);    
                    tweetes_to_render.insert(x+1,tweet);    
                x=x+1
            except:
                pass
            tweets_dict[tweet_render_text] = tweet_render.twitter_id
            
    #content_return['statuses'] = tweetes_to_render[0:150]

    print(len(tweetes_to_render)) 
    print('Start stats')
    # Fill in total number of entries in DB for this stock
    # Full DB
    content_return['total_entries_in_DB'] = StockCounter.objects.aggregate(Sum('counter'))['counter__sum']
    if(LabledCounter.objects.aggregate(Sum('counter'))['counter__sum'] != None):
        content_return['total_labeled_entries_in_DB'] = LabledCounter.objects.aggregate(Sum('counter'))['counter__sum']
    else:
        content_return['total_labeled_entries_in_DB'] = 0
    content_return['total_relevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`relevancy` = 'relevant' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_irrelevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`relevancy` = 'irrelevant' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_positive_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'positive' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_negative_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'negative' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_neutral_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'neutral' "}).aggregate(Sum('counter'))['counter__sum']

    # Stock DB
    try:
        content_return['stock_entries_in_DB'] = StockCounter.objects.extra(where={"`stock` = '"+stock_name+"' "}).values()[0]['counter']
    except:
        content_return['stock_entries_in_DB'] = 0
    try:
        content_return['stock_labeled_entries_in_DB'] = LabledCounter.objects.extra(where={"`stock` = '"+stock_name+"' "}).values()[0]['counter']
    except:
        content_return['stock_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_relevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `relevancy` = 'relevant' "}).values()[0]['counter']
    except:
        content_return['stock_relevant_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_irrelevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `relevancy` = 'irrelevant' "}).values()[0]['counter']
    except:
        content_return['stock_irrelevant_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_positive_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'positive' "}).values()[0]['counter']
    except:
        content_return['stock_positive_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_negative_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'negative' "}).values()[0]['counter']
    except:
        content_return['stock_negative_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_neutral_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'neutral' "}).values()[0]['counter']
    except:
        content_return['stock_neutral_labeled_entries_in_DB'] = 0

    #user counters
    try:
        content_return['user_relevant_for_stock_in_DB'] = UserCounter.objects.filter(labeled_user=request.user.username,stock=stock_name,relevancy='relevant').aggregate(Sum('counter'))['counter__sum']
    except:
        content_return['user_relevant_for_stock_in_DB'] = 0
    try:
        content_return['user_irrelevant_for_stock_in_DB'] = UserCounter.objects.filter(labeled_user=request.user.username,stock=stock_name,relevancy='irrelevant').aggregate(Sum('counter'))['counter__sum']
    except:
        content_return['user_irrelevant_for_stock_in_DB'] = 0
    content_return['user_total_labels_in_DB'] = UserCounter.objects.filter(labeled_user=request.user.username).aggregate(Sum('counter'))['counter__sum']

    print('Done')
    #gc.collect()
    return content_return 

#@login_required
@ajax
def get_tweets_proto(request):
    stock_name = request.POST['query']

    content_return = {}
    #query = stock_name
    #query = synonyms[query]

    #remove the adult content
    #naughty_words=" AND ( -ﺰﺑ -ﻂﻳﺯ -ﻂﻴﻇ -ﺲﻜﺳ -ﺲﻜﺴﻳ -ﺲﺣﺎﻗ -ﺞﻨﺳ -ﻦﻴﻛ -ﺞﻨﺳ -ﺏﺯ -ﺏﺯﺍﺯ -ﻚﺳ -ﻒﺤﻟ -ﻒﺣﻮﻠﻫ -ﺬﺑ )"
    stock_id = Stocks.objects.filter(stock=stock_name)[0].stock_id
    
    '''
    #tweets = twitter.search(q= query + 'OR ' + synonyms[query], result_type='recent')
    try:
        tweets = twitter.search(q=query, result_type='recent')
    except:
        from twython import Twython
        twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")
        tweets = twitter.search(q=query, result_type='recent')
    '''
    
    try:
        tweets = twitterCrawler.SearchQueryAPI(query, -1, -1)
    except:        
        PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        configFileCrawler = os.path.join(PROJECT_DIR, 'TwitterCrawler','Configurations', 'Configurations_Proto.xml')
        twitterCrawler = TwitterCrawler(configFileCrawler, None, None, None)
        #tweets = twitterCrawler.SearchQueryAPI(query, -1, -1)

    try:
        price_list = StocksPrices.objects.filter(stock=stock_id).order_by('-id')
        price = price_list[0].close
        print('Price in DB')
    except:
        price = 0


    from django.utils import timezone 
    content_return['price'] = price
    #tweets['price'] = CorrectionData.objects.get(stock_name=query)
    '''
    print('Saving tweets')
        
    for tweet in tweets:
        tweet_exist = Opinion.objects.filter(twitter_id=tweet['id_str'])
        if(len(tweet_exist) == 0):
            try:
                item = Opinion()
                item.twitter_id = tweet['id_str']
                item.user_id = tweet['user']['id']
                item.text = tweet['text']
                item.created_at = tweet['created_at']
                item.user_followers_count = tweet['user']['followers_count']
                item.user_profile_image_url = tweet['user']['profile_image_url']
                item.media_url = tweet['entities']
                item.tweeter_sname = tweet['user']['screen_name']
                item.tweeter_name = tweet['user']['name']
                #print('kkkkkkk'+str(tweet['entities']))
                item.pub_date = str(timezone.now())
                item.stock = stock_name
                item.labeled = False
                item.source = "twitter.com"
                if ' ﺰﺑ ' in tweet['text'] and ' ﻂﻳﺯ ' in tweet['text'] and ' ﻂﻴﻇ ' in tweet['text'] and ' ﺲﻜﺳ ' in tweet['text'] and ' ﺲﻜﺴﻳ ' in tweet['text'] and ' ﺲﺣﺎﻗ ' in tweet['text'] and ' ﺞﻨﺳ ' in tweet['text'] and ' ﺏﺯ ' in tweet['text'] and ' ﺏﺯﺍﺯ ' in tweet['text'] and ' ﻂﻳﺯ ' in tweet['text'] and ' ﻂﻳﺯ ' in tweet['text'] and ' ﻂﻳﺯ ' in tweet['text'] and ' ﻚﺳ ' in tweet['text'] and ' ﻒﺤﻟ ' in tweet['text'] and ' ﻒﺣﻮﻠﻫ ' in tweet['text'] and ' ﺬﺑ ' in tweet['text']:
                    print(tweet['text'])
                else:
                    item.save()
            except Exception as e: 
              pass
    print('Tweets saved')
    '''
    tweetes_to_render=list(Opinion.objects.filter(stock=stock_id, similarId='',created_at__isnull=False).values().order_by('-created_at')[0:50]);
    #tweetes_to_render_temp = Opinion.objects.filter(stock=stock_name).values().order_by('-id')[:20]
    #tweetes_to_render = sorted(tweetes_to_render_temp, key=lambda x: time.strptime(x['created_at'],'%a %b %d %X %z %Y'), reverse=True)[0:50];

    #tweetes_to_render = sorted(tweetes_to_render_temp, key=lambda x: time.strptime(x['created_at'],'%a %b %d %X %z %Y'), reverse=True);
    #my_list = list(tweetes_to_render)
    #print(json.dumps(my_list[0]))
    #tweetes_to_render_temp = Opview.objects.filter(stock=stock_name, labeled = False).values();
    #tweetes_to_render = sorted(tweetes_to_render_temp, key=lambda x: time.strptime(x['created_at'],'%a %b %d %X %z %Y'), reverse=True);

    #prevent Duplicate 
    tweets_dict = {}
    tweets_dict[''] = ''
    i = 1
    x = 0
    print('Handling duplicates')
    while x < min(50, len(tweetes_to_render)):
        
        try:
            tweet_render=tweetes_to_render[x];
                                
            # Get the tweet by ID 
            #retrievedTweet = dict(twitterCrawler.GetSingleTweetByID(tweet_render.get('twitter_id')))

            
            # Update the text in the tweet data
            #tweet_text = retrievedTweet['text']
            tweet_text = tweet_render['text']
            
            tweet_render['text'] = tweet_text
            if tweet_text.strip() in tweets_dict.keys():
                tweet = Opinion.objects.filter(twitter_id=tweet_render.get('twitter_id'))[0]
                tweet.similarId = tweets_dict[tweet_render['text']]
                tweet.save()
                tweetes_to_render.pop(x); 
                if (len(tweetes_to_render_temp) > 50+i):
                    tweetes_to_render.append(tweetes_to_render_temp[49+i])
                    i=i+1
            elif(request.user.username != "" and (tweet_render.get('labeled_user') == request.user.username or tweet_render.get('labeled_user_second') == request.user.username)):
                tweetes_to_render.remove(tweet_render)
                if (len(tweetes_to_render_temp) > 50+i):
                    tweetes_to_render.append(tweetes_to_render_temp[49+i])
                    i=i+1
            else:
                x=x+1
                tweets_dict[tweet_render.get('text').strip()] = tweet_render.get('twitter_id')

        except Exception as e:
            # Rate limit exceeded
            print('Error: ' + str(e)) 
            if('Twitter sent status 429' in str(e)):
                # Sleep 15 min, only 180 calls permitted per 15 min
                time.sleep(900)
                x=x+1
            elif('Twitter sent status 404' in str(e)):
                # Update the text in the tweet data
                tweet_text = 'Sorry, this tweet is not available for the free service'
                tweet_render['text'] = tweet_text
                if tweet_text.strip() in tweets_dict.keys():
                    tweet = Opinion.objects.filter(twitter_id=tweet_render.get('twitter_id'))[0]
                    tweet.similarId = tweets_dict[tweet_render['text']]
                    tweet.save()
                    tweetes_to_render.pop(x); 
                    if (len(tweetes_to_render_temp) > 50+i):
                        tweetes_to_render.append(tweetes_to_render_temp[49+i])
                        i=i+1
                elif(request.user.username != "" and (tweet_render.get('labeled_user') == request.user.username or tweet_render.get('labeled_user_second') == request.user.username)):
                    tweetes_to_render.remove(tweet_render)
                    if (len(tweetes_to_render_temp) > 50+i):
                        tweetes_to_render.append(tweetes_to_render_temp[49+i])
                        i=i+1
                else:
                    x=x+1
                    tweets_dict[tweet_render.get('text').strip()] = tweet_render.get('twitter_id')
            else:
                x=x+1
    content_return['statuses'] = tweetes_to_render
    
    print('Start stats')
    # Fill in total number of entries in DB for this stock
    # Full DB
    content_return['total_entries_in_DB'] = StockCounter.objects.aggregate(Sum('counter'))['counter__sum']
    if(LabledCounter.objects.aggregate(Sum('counter'))['counter__sum'] != None):
        content_return['total_labeled_entries_in_DB'] = LabledCounter.objects.aggregate(Sum('counter'))['counter__sum']
    else    :
        content_return['total_labeled_entries_in_DB'] = 0
    content_return['total_relevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`relevancy` = 'relevant' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_irrelevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`relevancy` = 'irrelevant' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_positive_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'positive' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_negative_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'negative' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_neutral_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'neutral' "}).aggregate(Sum('counter'))['counter__sum']

    # Stock DB
    try:
        content_return['stock_entries_in_DB'] = StockCounter.objects.extra(where={"`stock` = '"+stock_name+"' "}).values()[0]['counter']
    except:
        content_return['stock_entries_in_DB'] = 0
    try:
        content_return['stock_labeled_entries_in_DB'] = LabledCounter.objects.extra(where={"`stock` = '"+stock_name+"' "}).values()[0]['counter']
    except:
        content_return['stock_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_relevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `relevancy` = 'relevant' "}).values()[0]['counter']
    except:
        content_return['stock_relevant_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_irrelevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `relevancy` = 'irrelevant' "}).values()[0]['counter']
    except:
        content_return['stock_irrelevant_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_positive_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'positive' "}).values()[0]['counter']
    except:
        content_return['stock_positive_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_negative_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'negative' "}).values()[0]['counter']
    except:
        content_return['stock_negative_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_neutral_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'neutral' "}).values()[0]['counter']
    except:
        content_return['stock_neutral_labeled_entries_in_DB'] = 0
    print('Done')
    return content_return 

@ajax
def get_tweets_filtered(request):
    #gc.collect()
    stock_name = request.POST['query']
    content_return = {}
    print(start_time)
    stock_id = Stocks.objects.filter(stock=stock_name)[0].stock_id

    try:
        price_list = StocksPrices.objects.filter(stock=stock_id).order_by('-id')
        price = price_list[0].close
        print('Price in DB')
    except:
        price = 0

    from django.utils import timezone 
    content_return['price'] = price
    start_time = ''
    end_time = ''

    if start_time == '' and end_time == '':
        tweetes_to_render=list(Opinion.objects.filter(stock=stock_id, labeled = False, manual_labeled= False, similarId='',created_at__isnull=False,stocksprices_id__isnull=False).exclude(labeled_user=request.user.username).select_related('tweeter').select_related('stocksprices').order_by('-created_at')[0:500]);
    elif start_time != '' and end_time == '':
        tweetes_to_render=list(Opinion.objects.filter(stock=stock_id, labeled = False, manual_labeled= False,similarId='',created_at__gte=start_time,created_at__isnull=False,stocksprices_id__isnull=False).exclude(labeled_user=request.user.username).select_related('tweeter').select_related('stocksprices').order_by('-created_at')[0:500]);
    elif start_time == '' and end_time != '':
        tweetes_to_render=list(Opinion.objects.filter(stock=stock_id, labeled = False, manual_labeled= False, similarId='',created_at__lte=end_time,created_at__isnull=False,stocksprices_id__isnull=False).exclude(labeled_user=request.user.username).select_related('tweeter').select_related('stocksprices').order_by('-created_at')[0:500]);
    elif start_time != '' and end_time != '':
        tweetes_to_render=list(Opinion.objects.filter(stock=stock_id, labeled = False, manual_labeled= False,similarId='',created_at__range=[start_time, end_time],created_at__isnull=False,stocksprices_id__isnull=False).exclude(labeled_user=request.user.username).select_related('tweeter').select_related('stocksprices').order_by('-created_at')[0:500]);

    #prevent Duplicate 
    tweets_dict = {}
    tweets_dict[''] = ''
    i = 1
    x = 0
    print(len(tweetes_to_render))
    print('Handling duplicates')
    content_return['statuses'] = [[] for m in range(min(150, len(tweetes_to_render)))]
    #content_return['statuses'] = []
    while x < min(150, len(tweetes_to_render)):
        tweet_render=tweetes_to_render[x];
        tweet_render_text=tweet_render.text.strip()
        tweet_render_text=re.sub(r"RT @\w*\w: ", '', tweet_render_text, flags=re.MULTILINE)
        tweet_render_text=re.sub(r'\.\.\.', '', tweet_render_text, flags=re.MULTILINE)
        try:
            urls=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet_render_text);
            for i in range(0,len(urls)):
                rep='r\''+urls[i]+'\''
                tweet_render_text=re.sub(r""+urls[i]+"", '', tweet_render_text, flags=re.MULTILINE)
        except:
            pass
        
        #print(x) 
        # Classify the tweet
        PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        filter = Filter(PROJECT_DIR, 'tasnee3', False)
        text = [] 
        text.append(tweet_render_text)
        labels = filter.Classify(text)
        label = labels[0]
        if label == 1: # If irrelevant remove it
            tweetes_to_render.remove(tweet_render)
        elif tweet_render_text in tweets_dict.keys():
            #tweet = Opinion.objects.filter(twitter_id=tweet_render.get('twitter_id'))[0]
            #tweet.similarId = tweets_dict[tweet_render_text]
            #tweet.save();
            tweetes_to_render.pop(x); 
            #if (len(tweetes_to_render) > 150+i):
            #    tweetes_to_render.append(tweetes_to_render[149+i])
            #    i=i+1
        elif(tweet_render.labeled_user == request.user.username or tweet_render.labeled_user_second == request.user.username) and request.user.username != '':
            tweetes_to_render.remove(tweet_render)
            #if (len(tweetes_to_render) > 150+i):
            #    tweetes_to_render.append(tweetes_to_render[149+i])
            #    i=i+1
        else:
            #content_return['statuses'].append(model_to_dict(tweetes_to_render[x]))
            content_return['statuses'][x] = model_to_dict(tweetes_to_render[x]);
            content_return['statuses'][x]['created_at']=tweetes_to_render[x].created_at.strftime('%a %b %d %X %z %Y');
            content_return['statuses'][x]['user_followers_count']=tweetes_to_render[x].tweeter.tweeter_followers_count;
            content_return['statuses'][x]['user_profile_image_url']=tweetes_to_render[x].tweeter.tweeter_profile_image_url;
            content_return['statuses'][x]['user_location']=tweetes_to_render[x].tweeter.tweeter_location;
            content_return['statuses'][x]['tweeter_name']=tweetes_to_render[x].tweeter.tweeter_name;
            content_return['statuses'][x]['tweeter_sname']=tweetes_to_render[x].tweeter.tweeter_sname;
            content_return['statuses'][x]['price_time_then']=tweetes_to_render[x].stocksprices.time.strftime('%a %b %d %I:%M %p');
            content_return['statuses'][x]['price_then']=tweetes_to_render[x].stocksprices.close
            try:
                if tweetes_to_render[x].conversation_reply != '' and tweetes_to_render[x].conversation_reply != None:
                    #print(tweetes_to_render[x]['conversation_reply'])
                    tweet = Opinion.objects.filter(stock=stock_id,twitter_id=tweetes_to_render[x].conversation_reply).select_related('stocksprices').select_related('tweeter')[0]
                    content_return['statuses'].append([]);    
                    tweetes_to_render.insert(x+1,tweet);    
                x=x+1
            except:
                pass
            tweets_dict[tweet_render_text] = tweet_render.twitter_id
            
    #content_return['statuses'] = tweetes_to_render[0:150]

    print(len(tweetes_to_render)) 
    print('Start stats')
    # Fill in total number of entries in DB for this stock
    # Full DB
    content_return['total_entries_in_DB'] = StockCounter.objects.aggregate(Sum('counter'))['counter__sum']
    if(LabledCounter.objects.aggregate(Sum('counter'))['counter__sum'] != None):
        content_return['total_labeled_entries_in_DB'] = LabledCounter.objects.aggregate(Sum('counter'))['counter__sum']
    else:
        content_return['total_labeled_entries_in_DB'] = 0
    content_return['total_relevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`relevancy` = 'relevant' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_irrelevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`relevancy` = 'irrelevant' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_positive_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'positive' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_negative_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'negative' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_neutral_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'neutral' "}).aggregate(Sum('counter'))['counter__sum']

    # Stock DB
    try:
        content_return['stock_entries_in_DB'] = StockCounter.objects.extra(where={"`stock` = '"+stock_name+"' "}).values()[0]['counter']
    except:
        content_return['stock_entries_in_DB'] = 0
    try:
        content_return['stock_labeled_entries_in_DB'] = LabledCounter.objects.extra(where={"`stock` = '"+stock_name+"' "}).values()[0]['counter']
    except:
        content_return['stock_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_relevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `relevancy` = 'relevant' "}).values()[0]['counter']
    except:
        content_return['stock_relevant_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_irrelevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `relevancy` = 'irrelevant' "}).values()[0]['counter']
    except:
        content_return['stock_irrelevant_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_positive_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'positive' "}).values()[0]['counter']
    except:
        content_return['stock_positive_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_negative_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'negative' "}).values()[0]['counter']
    except:
        content_return['stock_negative_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_neutral_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'neutral' "}).values()[0]['counter']
    except:
        content_return['stock_neutral_labeled_entries_in_DB'] = 0

    #user counters
    try:
        content_return['user_relevant_for_stock_in_DB'] = UserCounter.objects.filter(labeled_user=request.user.username,stock=stock_name,relevancy='relevant').aggregate(Sum('counter'))['counter__sum']
    except:
        content_return['user_relevant_for_stock_in_DB'] = 0
    try:
        content_return['user_irrelevant_for_stock_in_DB'] = UserCounter.objects.filter(labeled_user=request.user.username,stock=stock_name,relevancy='irrelevant').aggregate(Sum('counter'))['counter__sum']
    except:
        content_return['user_irrelevant_for_stock_in_DB'] = 0
    content_return['user_total_labels_in_DB'] = UserCounter.objects.filter(labeled_user=request.user.username).aggregate(Sum('counter'))['counter__sum']
    print('Done')
    #gc.collect()
    return content_return 


def getSimilarlabeling():
    duplicate_tweetes = Opinion.objects.exclude(similarId='');
    for tweet in duplicate_tweetes:
        parent_tweet =  Opinion.objects.filter(twitter_id = tweet.similarId).values()[0]
        if parent_tweet['labeled'] == 1:
            tweet.voted_relevancy = parent_tweet['voted_relevancy']
            tweet.voted_sentiment = parent_tweet['voted_sentiment']
            tweet.labeled = True
            tweet.save()

@ajax
def get_correction(request):
    relevancy = request.POST['relevancy']
    sentiment = request.POST['sentiment']
    tweet_id = request.POST['tweet_id']
    stock_name = request.POST['stock']
    print(tweet_id)
    print(request.user.username)
    print(stock_name)
    stock_id = Stocks.objects.filter(stock=stock_name)[0].stock_id

    if(request.user.username == '' or request.user.username == None):
        print('ERROR: Empty user name')
        return
    
    tweet = Opinion.objects.filter(twitter_id=tweet_id, stock=stock_id)[0]
    if(relevancy == 'none' or relevancy == None):
        if(tweet.sentiment == 'none' or tweet.sentiment == '' or tweet.sentiment==None):
            tweet.sentiment = sentiment
            tweet.voted_sentiment = sentiment
        elif(tweet.sentiment_second == 'none' or tweet.sentiment_second == '' or tweet.sentiment_second == None):
            tweet.sentiment_second = sentiment
            if(tweet.sentiment == tweet.sentiment_second):
                tweet.sentiment_third= 'not_needed'
                tweet.voted_sentiment = sentiment
        elif(tweet.sentiment_third == 'none' or tweet.sentiment_third == '' or tweet.sentiment_third ==  None):
            tweet.sentiment_third = sentiment
            rel_list=[tweet.sentiment,tweet.sentiment_second,tweet.sentiment_third]
            tweet.voted_sentiment=max(((item, rel_list.count(item)) for item in set(rel_list)), key=lambda a: a[1])[0]

        #print('Sentiment')
    elif (sentiment == 'none' or sentiment == None):
        if(tweet.relevancy == 'none' or tweet.relevancy == '' or tweet.relevancy == None):
            tweet.relevancy = relevancy
            tweet.labeled_user = request.user.username
        elif(tweet.relevancy_second == 'none' or tweet.relevancy_second == '' or tweet.relevancy_second == None):
            tweet.relevancy_second = relevancy
            tweet.labeled_user_second = request.user.username
            if(tweet.relevancy == tweet.relevancy_second):
                tweet.labeled_user_third='not_needed'
                tweet.relevancy_third='not_needed'
                tweet.voted_relevancy=tweet.relevancy
        elif(tweet.relevancy_third == 'none' or tweet.relevancy_third == '' or tweet.relevancy_third ==  None):
            tweet.relevancy_third = relevancy
            tweet.labeled_user_third = request.user.username
            rel_list=[tweet.relevancy,tweet.relevancy_second,tweet.relevancy_third]
            tweet.voted_relevancy=max(((item, rel_list.count(item)) for item in set(rel_list)), key=lambda a: a[1])[0]
        #print('Relevance')

    if(((tweet.relevancy != 'none') & (tweet.relevancy != '') & (tweet.relevancy != None)) & ((tweet.sentiment != 'none') & (tweet.sentiment != '') & (tweet.sentiment != None))
        & ((tweet.relevancy_second != 'none') & (tweet.relevancy_second != '') & (tweet.relevancy_second != None)) & ((tweet.sentiment_second != 'none') & (tweet.sentiment_second != '')& (tweet.sentiment_second != None))
        & ((tweet.relevancy_third != 'none') & (tweet.relevancy_third != '') & (tweet.relevancy_third != None)) & ((tweet.sentiment_third != 'none') & (tweet.sentiment_third != '') & (tweet.sentiment_third != None))):
        tweet.labeled = True
        tweet.manual_labeled = True
        #print(tweet.votel_relevancy)
    tweet.save()

def correction_sentiment(request):
    relevancy = request.POST['relevancy']
    sentiment = request.POST['sentiment']
    text = request.POST['text']
    stock = request.POST['stock']
    
    try:
        correctionData = CorrectionData.objects.get(text=text)
        correctionData.relevancy = relevancy
    except:
        correctionData = CorrectionData(text=text,relevancy=relevancy,sentiment='neutral',stock=stock)

    
    correctionData.save()
    
   
        
def retrain():
    correctionData = CorrectionData.objects.all()
    trainSet= []
    for item in correctionData:
        trainSet.append({'label' : item.relevancy, 'text' :item.text })

    filter = Filter(r"C:\Users\Tarek Abdelhakim\workspace\DjangoWebProject1",item.stock.strip(),True)
    filter.GetBestClassifier(trainSet)
    

@login_required
def news(request):
    #Select Today's News 
    from django.utils import timezone
    today =datetime.datetime.strftime(timezone.now(),"%Y-%m-%d")
    newsList=Opinion.objects.extra(where={"`pub_date` LIKE CONCAT(  '%%',  '"+today+"',  '%%' ) and `source` != 'twitter.com' "}).values()
    
    News =[]
    for newsItem in newsList:
        n=NewsItem()
        n.link = newsItem['source']
        n.title = newsItem['text']
        News.append(n)
    """Renders the news page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/news.html',
        context_instance = RequestContext(request,
        {
            'title':'News',
            'News':News,
        })
    )

def runPriceCrawling():
    urlstr = 'http://www.marketstoday.net/markets/%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9/Companies/1/ar/'
    fileHandle = urllib.request.urlopen(urlstr)
    html = fileHandle.read()
    soup = BeautifulSoup(html)
    #print(soup)
    from pytz import timezone
    localtz = timezone('UTC')
    time_in_site=localtz.localize(parse(soup.findAll('span', attrs={'class':'tradhour'})[0].text.split('\n', 1)[1].split(" :")[1].replace('(local time)\r\n','',1)));

    urlstr_tasi = 'http://www.marketstoday.net/markets/%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9/Index-Performance/1/ar/'
    fileHandle_tasi = urllib.request.urlopen(urlstr_tasi)
    html_tasi = fileHandle_tasi.read()
    soup_tasi = BeautifulSoup(html_tasi)
    item = StocksPrices()
    item.stock_id=3
    item.close=soup_tasi.find('span', attrs={'class':'valuetxt'}).text.replace(',','')
    item.time=time_in_site
    try:
        item.save()
    except:
        pass

    for b in soup.findAll('tr', attrs={'class':'symbolflip'})[1:]:
        try:
            stockname=b.find('a', attrs={'class':'jTip'}).text
            stocks = Stocks.objects.filter(marketstoday_name=stockname)[0]
            close=b.findAll('td')[1].text.replace(',','')
            open=b.findAll('td')[2].text.replace(',','')
            max=b.findAll('td')[3].text.replace(',','')
            min=b.findAll('td')[4].text.replace(',','')
            vol=b.findAll('td')[8].text.replace(',','')
            print(stocks.stock)
            print(close)
            item = StocksPrices()
            item.stock_id=stocks.stock_id
            item.close=close
            item.open=open
            item.max=max
            item.min=min
            item.volume=vol
            item.time=time_in_site
            item.save()
        except:
            pass
    return True

def runNewsCrawling():
    rssPage = urllib.request.urlopen('http://www.cma.org.sa/Ar/News/_layouts/listfeed.aspx?List=%7B0622219A-483C-46C4-A066-AA4EDEDD0952%7D')
    rssFeed = minidom.parse(rssPage)

    for item in rssFeed.getElementsByTagName("item"):
        Op = Opinion()
        for a in item.getElementsByTagName("link"):
            Op.source=a.childNodes[1].nodeValue        
        for a in item.getElementsByTagName("title"):
            Op.text=a.childNodes[1].nodeValue
        #for a in item.getElementsByTagName("pubDate"):
        #    Op.pub_date=a.childNodes[0].nodeValue
        Op.pub_date= str(datetime.datetime.utcnow())
        Op.twitter_id = str(datetime.datetime.utcnow())
        Op.user_id = ''
        Op.created_at = None
        Op.user_followers_count = 0
        Op.user_profile_image_url = 'none'
        Op.media_url= 'none'
        Op.stock_id = Stocks.objects.filter(stock='none')[0].stock_id
        Op.labeled = False
        Op.relevancy = 'none'
        Op.sentiment = 'none'
        Op.labeled_user= 'none'
        Op.save()
    #Time by seconds
    threading.Timer(86400.0, runNewsCrawling).start()

#Crawl the News every 24 hours
#runNewsCrawling()


@login_required
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.datetime.now().year,
        })
    )

@login_required
def about(request):         
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.datetime.now().year,
        })
    )

def login_user_proto(request):
    
    oauth = OAuth1(consumerKey, client_secret=consumerSecret)
    r = requests.post(url=request_token_url, auth=oauth)
    credentials = urllib_parse.parse_qs(r.content.decode("utf-8"))
    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]
    
    #full_auth_url = authenticate_url + '?oauth_token=' + resource_owner_key
    #authorization_url = oauth.authorization_url(base_authorization_url)
    full_auth_url = base_authorization_url + '?oauth_token=' + resource_owner_key
    request.session['request_token'] = str(resource_owner_key)
    return redirect(full_auth_url)    
    
    '''
    if request.method == 'POST':
        #logout(request)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home_proto')
                #return HttpResponseRedirect('/about/')
    return redirect('/')
    '''
def twitter_authenticated(request):
    if request.method == 'GET':

        accessToken = request.GET['oauth_token']
        accessTokenVerifier = request.GET['oauth_verifier']
        accessTokenSecret = request.session.get('request_token', None)
        '''
        oauth = OAuth1(consumerKey, client_secret=consumerSecret)
        r = requests.post(url=request_token_url, auth=oauth)
        credentials = urllib_parse.parse_qs(r.content.decode("utf-8"))
        resource_owner_key = credentials.get('oauth_token')[0]
        resource_owner_secret = credentials.get('oauth_token_secret')[0]
    
        oauth = OAuth1(client_key=consumerKey, client_secret=consumerSecret, resource_owner_key=resource_owner_key, resource_owner_secret=resource_owner_secret)
        r = requests.post(url=access_url, auth=oauth)
        
        access_token_from_url = urllib_parse.parse_qs(r.content.decode("utf-8"))
        
        
        username = access_token_from_url['screen_name']
        '''
        '''
        oauth = OAuth1(consumerKey, client_secret=consumerSecret)
        r = requests.post(url=request_token_url, auth=oauth)
        credentials = urllib_parse.parse_qs(r.content.decode("utf-8"))
        resource_owner_key = credentials.get('oauth_token')[0]
        resource_owner_secret = credentials.get('oauth_token_secret')[0]
        #from requests_oauthlib import OAuth1Session
        oauth = OAuth1(consumerKey,
                              client_secret=consumerSecret,
                              resource_owner_key=resource_owner_key,
                              resource_owner_secret=resource_owner_secret,
                              verifier=accessTokenVerifier)
        
        #oauth_tokens = oauth.fetch_access_token(access_url)
        r = requests.post(url=access_url, auth=oauth)
        
        access_token_from_url = urllib_parse.parse_qs(r.content.decode("utf-8"))
        username = access_token_from_url['screen_name']
        #password = oauth_tokens['oauth_token_secret']
        password = accessTokenSecret
        '''
        oauth = OAuth1(consumerKey,
                       client_secret=consumerSecret,
                       resource_owner_key=accessToken,
                       resource_owner_secret=accessTokenSecret,
                       verifier=accessTokenVerifier)

        r = requests.post(url=access_url, auth=oauth)
        credentials = urllib_parse.parse_qs(r.content.decode("utf-8"))
        resource_owner_key = credentials.get('oauth_token')[0]
        resource_owner_secret = credentials.get('oauth_token_secret')[0]
        '''
        See http://requests-oauthlib.readthedocs.org/en/latest/oauth1_workflow.html#workflow-example-showing-use-of-both-oauth1-and-oauth1session
        >>> protected_url = 'https://api.twitter.com/1/account/settings.json'
        
        >>> # Using OAuth1Session
        >>> oauth = OAuth1Session(client_key,
                                  client_secret=client_secret,
                                  resource_owner_key=resource_owner_key,
                                  resource_owner_secret=resource_owner_secret)
        >>> r = oauth.get(protected_url)
        
        >>> # Using OAuth1 auth helper
        >>> oauth = OAuth1(client_key,
                           client_secret=client_secret,
                           resource_owner_key=resource_owner_key,
                           resource_owner_secret=resource_owner_secret)
        >>> r = requests.get(url=protected_url, auth=oauth)
        '''        
        
        t = Twitter(auth=OAuth(resource_owner_key,resource_owner_secret, consumerKey,consumerSecret))
        results = t.account.verify_credentials()
        username = results['screen_name']
        #password = resource_owner_secret
        #user = authenticate(username=username, password=password)
        from app.models import User
        
        try:
            user = User.objects.get(username=username)
            request.session['user_authenticated'] = True
            return redirect('/home_proto')
            
        except User.DoesNotExist:
            return render(
                            request,
                            'app/signup.html',
                            context_instance = RequestContext(request,
                            {
                                'twitter_username':username,
                            }))
    

        
def login_user(request):

    if request.method == 'POST':
        #logout(request)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home')
                #return HttpResponseRedirect('/about/')
    return redirect('/register')

def twitter_register(request):
    
    if request.method == 'POST':
        from app.forms import UserForm
        user_form = UserForm(data=request.POST)
        #user_form.data['username'] = request.session.get('twitter_username', None)
        from app.models import User
        if user_form.is_valid() :
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            new_user = User()
            new_user.username = request.POST['username']
            new_user.email = request.POST['email']
            new_user.save()
            #request.session['message'] = 'registration done please login'
            return redirect("/home_proto")
            #return render(request, 'app/site_layout.html', {'message':'registration done please login'})
        else:
            request.session['error'] = user_form.errors
            #return redirect("/prototype")
            return render(request, 'app/signup.html', {'error':user_form.errors})

def register(request):
    
    if request.method == 'POST':
        from app.forms import UserForm
        user_form = UserForm(data=request.POST)

        if user_form.is_valid() :
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            request.session['message'] = 'registration done please login'
            return redirect("/")
            #return render(request, 'app/site_layout.html', {'message':'registration done please login'})
        else:
            request.session['error'] = user_form.errors
            return redirect("/")
           #return render(request, 'app/site_layout.html', {'error':user_form.errors})
    else:
        return redirect("/")

