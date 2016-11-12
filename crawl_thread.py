from datetime import datetime
from app.models import Sources, Stocks, Opinion, Tweeter, Matrix
from django.utils import timezone
from Filter.Filter import Filter
import threading, time
import datetime
import unicodedata
import os
from QuestionsModel.QuestionsModel import QuestionsModel

import django
django.setup()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_stock_id(s):
    try:
         r = Stocks.objects.filter(stock=s)[0].stock_id
    except:
         r = 9999
    return r;

qpath = os.path.join('data', 'QuestionsModel')
questions_model = QuestionsModel.load(qpath)
global counter
counter = 0

#def runSearch(que):
def runSearch(que,stock,parent):
    global counter
    counter += 1

    if is_number(que):
        temp = twitter.show_status(id=que)
        twittes = {}
        twittes['statuses']=[temp]
    else:
        twittes = twitter.search(q=que, result_type='recent', show_all_inline_media='true')

    from datetime import datetime, timedelta
    s_id = get_stock_id(stock)
    for tweet in twittes['statuses']:
        item = Opinion()
        item.twitter_id = tweet['id_str']
        item.tweeter_id = tweet['user']['id']
        item.text = tweet['text']
        #item.created_at = tweet['created_at']
        item.created_at =datetime.strptime(tweet['created_at'],'%a %b %d %X %z %Y')
        item.media_url = tweet['entities']
        item.pub_date = timezone.now()
        #item.stock_id = Stocks.objects.filter(stock=stock)[0].stock_id
        item.stock_id = s_id
        try:
            item.retweet_original = tweet['retweeted_status']['id']
            if Opinion.objects.filter(twitter_id=item.retweet_original,stock_id=item.stock_id).exists():
                any_thing = 0;
            else:
                d = threading.Thread(target=runSearch,args=(tweet['retweeted_status']['id'],stock,''))
                d.start()
                time.sleep(2)

        except:
            item.retweet_original = None
        item.source_id = 1
        item.labeled = False
        item.p_relevancy = None
        item.p_sentiment = None
        item.p_question = None
        item.p_pricetarget = None
        item.pricetarget = None
        item.r_correction = None
        item.s_correction = None
        item.q_correction = None
        item.p_correction = None
        print( ' parent is ' + str(parent) )
        if parent == '':
            item.head_opinion = 1;
        else:
            item.head_opinion = 0;

        if ' ﺰﺑ ' in tweet['text'] or ' ﻂﻳﺯ ' in tweet['text'] or ' ﻂﻴﻇ ' in tweet['text'] or 'ﺲﻜﺳ' in tweet['text'] or 'ﺲﻜﺴﻳ' in tweet['text'] or ' ﺲﺣﺎﻗ ' in tweet['text'] or ' ﺞﻨﺳ ' in tweet['text'] or ' ﺏﺯ ' in tweet['text'] or 'ﺏﺯﺍﺯ' in tweet['text'] or ' ﻂﻳﺯ ' in tweet['text'] or ' ﻂﻳﺯ ' in tweet['text'] or ' ﻂﻳﺯ ' in tweet['text'] or ' ﻚﺳ ' in tweet['text'] or ' ﻒﺤﻟ ' in tweet['text'] or ' ﻒﺣﻮﻠﻫ ' in tweet['text'] or ' ﺬﺑ ' in tweet['text'] or ' نيك ' in tweet['text'] or 'شرموط' in tweet['text'] or ' ناك ' in tweet['text'] or 'تتناك' in tweet['text'] or 'نياك' in tweet['text'] or 'زبر' in tweet['text'] or ' نيك' in tweet['text'] or ' كسه' in tweet['text']:
            print("naughty"+tweet['text'])
        else:
            if Tweeter.objects.filter(tweeter_id=tweet['user']['id']).exists():
                item2 = Tweeter.objects.filter(tweeter_id=tweet['user']['id'])[0]
                print(str(tweet['user']['id']) + ' tweeter is updated ')
            else:
                item2 = Tweeter()
                item2.tweeter_id = tweet['user']['id']
                print(str(tweet['user']['id']) + ' tweeter is added')

            item2.tweeter_followers_count = tweet['user']['followers_count']
            item2.tweeter_followings_count = tweet['user']['friends_count']
            item2.tweeter_statuses_count = tweet['user']['statuses_count']
            item2.tweeter_likes = tweet['user']['favourites_count']
            item2.tweeter_created_at = datetime.strptime(tweet['user']['created_at'],'%a %b %d %X %z %Y')
            item2.tweeter_description = tweet['user']['description']
            item2.tweeter_default_language = tweet['user']['lang']
            item2.tweeter_time_zone = tweet['user']['time_zone']
            item2.tweeter_profile_image_url = tweet['user']['profile_image_url']
            item2.tweeter_sname = tweet['user']['screen_name']
            item2.tweeter_verified = tweet['user']['verified']
            item2.tweeter_name = tweet['user']['name']
            item2.tweeter_location = tweet['user']['location']
            item2.save()
            isq = questions_model.isQuestion(item)
            if isq == 2:
                print(item.text , ' is a question...')
                item.p_question=1
            else:
                item.p_question=0

            try:
                item.save()
            except:
                pass 

            if tweet['in_reply_to_status_id'] != None:
                time.sleep(9)
                item.conversation_reply = tweet['in_reply_to_status_id']
                if Opinion.objects.filter(twitter_id=item.conversation_reply,stock_id=item.stock_id).exists():
                    item4 = Opinion.objects.filter(twitter_id=item.conversation_reply,stock_id=item.stock_id)[0]
                    item4.head_opinion = 0;
                    item4.save()
                else:
                    d = threading.Thread(target=runSearch,args=(tweet['in_reply_to_status_id'],stock,item.twitter_id))
                    d.start()

            item.save()
            # it was a bad idea to set similarId like the parent tweet of the conversation
            #if parent != '':
            #    item3 = Opinion.objects.filter(twitter_id = que,stock_id = s_id)[0]
            #    item3.similarId = parent
            #    print("child tweet: "+str(parent)+" parent tweet: "+str(que))
            #    item3.save()

from twython import Twython
twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")
#f_in = open('..//TwitterCrawler//stocks.txt', 'r', encoding='utf-8')
#lines = f_in.readlines()

while True:
    print("startt:" + str(datetime.datetime.now()) )
    stocks = Stocks.objects.filter().exclude(stock_id__in=[1,2,4,5]);
    query_list = Matrix.objects.filter().values_list('item', flat=True)
    for stock in stocks:
        s_id = stock.stock_id
        s_name = stock.stock
        s_fullname = stock.full_name_arabic
        time.sleep(9)
        d = threading.Thread(target=runSearch,args=(s_fullname,s_name,''))
        d.start()
    
    for qo in query_list: 
        print('Matrix: ' + str(qo));
        for stock in stocks:
            query = stock.synonym + qo
            time.sleep(8)
            t = threading.Thread(target=runSearch,args=(query,stock.stock,''))
            t.start()
     
    print("End:" + str(datetime.datetime.now()) )
