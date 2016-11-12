from datetime import datetime
from app.models import Opinion,Stocks
from django.utils import timezone
from Filter.Filter import Filter
import threading, time
import datetime
import os
import re


import django
django.setup()


def runUpdate(tweet,i_similarId):
    tweet.similarId = i_similarId;
    tweet.save();

while True:
    print("Handling Dublicates")
    for x in Stocks.objects.filter().exclude(stock=None).exclude(stock='none').exclude(stock=''):
        line = x.stock_id
        stock_name = x.stock
        print(stock_name);
        tweetes_to_render = Opinion.objects.filter(stock=line, source = 1, similarId__isnull=True, conversation_reply__isnull=True).values().order_by('-id')[0:5000]
        tweets_dict = {}
        tweets_dict[''] = ''
        i = 1
        x = 0
        while x < len(tweetes_to_render):
            tweet_render=tweetes_to_render[x];
            tweet_render_text=tweet_render.get('text').strip()
            try:
                urls=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet_render_text);
                for i in range(0,len(urls)):
                    rep='r\''+urls[i]+'\''
                    tweet_render_text=re.sub(r""+urls[i]+"", '', tweet_render_text, flags=re.MULTILINE)
            except:
                pass
            
            tweet_render_text=re.sub(r"RT @\w*\w: ", '', tweet_render_text, flags=re.MULTILINE)
            tweet_render_text=re.sub(r"@\w*\w ", '', tweet_render_text, flags=re.MULTILINE)
            tweet_render_text=tweet_render_text.replace("…","")
            #tweet_render_text=re.sub(r'\.\.\.', '', tweet_render_text, flags=re.MULTILINE)
            tweet_render_text=tweet_render_text[0:min(110,len(tweet_render_text))]
    
            if tweet_render_text in tweets_dict.keys() and tweet_render_text != '' :
                tweet = Opinion.objects.filter(stock=line, twitter_id=tweet_render.get('twitter_id'))[0]
                # will update the similarId of the older tweet
                print('---------------------- Will update the similarId of the older tweet')
                print('Older tweet: ' + str(tweet_render.get('twitter_id')))
                print('Newer tweet: ' + str(tweets_dict[tweet_render_text]))
                print(tweet.text)
                print(tweet_render.get('text'))
                d = threading.Thread(target=runUpdate,args=(tweet,tweets_dict[tweet_render_text]))
                time.sleep(0.05)
                d.start()
            else:
                tweets_dict[tweet_render_text] = tweet_render.get('twitter_id')
            x=x+1
    print("sleeping 30 min...")
    time.sleep(1800)

##print("Labeling Dublicates")
##duplicate_tweetes = Opinion.objects.exclude(similarId='');
##for tweet in duplicate_tweetes:
##    parent_tweet =  Opinion.objects.filter(twitter_id = tweet.similarId).values()[0]
##    if parent_tweet['labeled'] == 1:
##        tweet.voted_relevancy = parent_tweet['voted_relevancy']
##        tweet.voted_sentiment = parent_tweet['voted_sentiment']
##        tweet.labeled = True
##        tweet.save()
##
