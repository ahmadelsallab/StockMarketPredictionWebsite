import os
from QuestionsModel.QuestionsModel import QuestionsModel
from app.models import Opinion,Stocks,StocksPrices, Evaluation,Sources
from twython import Twython
import datetime
from django.utils import timezone


timenow = timezone.now()
path = os.path.join('data', 'QuestionsModel')

m = QuestionsModel()
eval = m.train()
#print(eval)
m.save(path)

item = Evaluation()
item.time = timenow
item.classifier = 'q'
item.stock_id = None
item.evaluation = round(eval[1],2)
item.training_sample = eval[0]
item.save()

