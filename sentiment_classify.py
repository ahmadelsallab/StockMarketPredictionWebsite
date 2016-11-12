import os
import threading, time
import datetime
import unicodedata
from datetime import datetime
from django.utils import timezone
import threading, time
from SentimentModel.SentimentModel import SentimentModel
from app.models import Sources, Stocks, Opinion, Tweeter
from django.utils import timezone
from QuestionsModel.QuestionsModel import QuestionsModel


path = os.path.join('data', 'SentimentModel.bin')
m2 = SentimentModel.load(path)

qpath = os.path.join('data', 'QuestionsModel')
questions_model = QuestionsModel.load(qpath)

import django
django.setup()


labels = ['negative', 'positive', 'neutral']

while True:
    #tweets = Opinion.objects.filter(p_sentiment=None).filter(p_relevancy='relevant').filter(conversation_reply__isnull=True).order_by('-created_at')[0:1000];
    #tweets = Opinion.objects.filter(p_sentiment=None).filter(conversation_reply__isnull=True).order_by('-created_at')[0:1000];
    time.sleep(120)
    tweets = Opinion.objects.filter(sentiment = '', p_sentiment = None).filter(head_opinion = True).order_by('-created_at')[0:1000];
    
    arr = []
    for x in range(0,len(tweets)):
        #print("###########################")
        #print(sname)
        arr.append(tweets[x].text)
    
    pred = m2.classify(arr)
    print(x)
    for y in range(0,x):
        #print(tweets[y].text)
        #print(labels[pred[y]-1])
        tweets[y].p_sentiment=labels[pred[y]-1]
        isq = questions_model.isQuestion(tweets[y])
        if isq == 2:
            tweets[y].p_question=1
        else:
            tweets[y].p_question=0

        tweets[y].save()
