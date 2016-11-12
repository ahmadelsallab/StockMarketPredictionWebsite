import os
from QuestionsModel.QuestionsModel import QuestionsModel
from app import models
from twython import Twython

import django
django.setup()

qpath = os.path.join('data', 'QuestionsModel')
questions_model = QuestionsModel.load(qpath)


while True:
    tweets = models.Opinion.objects.filter(question= '',similarId = None, p_question=None).filter(conversation_reply__isnull=True)[1:1000];
    for x in range(0,len(tweets)):
        op = tweets[x]
        isq = questions_model.isQuestion(op)
        if isq == 2:
            op.p_question=1
        else:
            op.p_question=0
    
        op.save();
