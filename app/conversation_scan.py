from datetime import datetime
from app.models import Opinion,Stocks,Conversation
from django.utils import timezone
from Filter.Filter import Filter
import threading, time
import datetime
import os
import re


import django
django.setup()

l = []

def contains(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

def savee(a,d):
    c = Conversation()
    c.ancestor_id = a;
    c.descendant_id = d;
    #print("save")
    c.save();

def get_child(t,y):
    l.append(t['id'])
    try:
        tweet = Opinion.objects.filter(twitter_id=t['conversation_reply'],stock_id=t['stock_id']).values()[0]
        if tweet['conversation_reply'] != None:
            get_child(tweet,1)
        else:
            l.append(tweet['id'])
    except:
        pass

for s in Stocks.objects.filter().exclude(stock=None).exclude(stock='none').exclude(stock=''):
    line = s.stock_id
    stock_name = s.stock
    #print(stock_name);
    #tweetes_to_render = Opinion.objects.filter(conversation_reply__isnull=False).values().order_by('-id')
    tweetes_to_render = Opinion.objects.filter(stock_id=line, source = 1, similarId__isnull=True).values().order_by('-created_at')
    i = 1
    x = 0
    leng=len(tweetes_to_render)
    print(leng);
    while x < leng:
        l = []
        tweet_render=tweetes_to_render[x];
        get_child(tweet_render,x);
        #d = threading.Thread(target=get_child,args=(tweet_render,x))
        #time.sleep(0.05)
        if not Conversation.objects.values_list('ancestor_id', flat=True).filter(descendant_id=l[0]).exists():
            print(l)
            for m in l:
                d = threading.Thread(target=savee,args=(tweet_render['id'],m))
                time.sleep(0.05)
                d.start()
        else:
            involved_list = Conversation.objects.values_list('ancestor_id', flat=True).filter(descendant_id=l[0])
            len(involved_list)
            ss = involved_list[0]
            con=Conversation.objects.values_list('descendant_id', flat=True).filter(ancestor_id=ss)
            if not contains(l,con):
                print(l)
                for m in l:
                    d = threading.Thread(target=savee,args=(tweet_render['id'],m))
                    time.sleep(0.05)
                    d.start()
                    #savee(tweet_render['id'],x)
            #d.start()
        x=x+1
