import os
from app import models
from app.models import Opinion,Stocks,StocksPrices, Evaluation,Sources
from SentimentModel.SentimentModel import SentimentModel
import threading, time
import datetime
from django.utils import timezone
import re
import os

m = SentimentModel(modeln=4)
out=m.train(backend=True)
print("out")    ## dictionary accuracy and training samples like relevancy
print(out)
path = os.path.join('data', 'SentimentModel.bin')
m.save(path)
timenow = timezone.now()

item = Evaluation()
item.time = timenow
item.classifier = 's'
item.stock_id = None
item.training_sample = out['training_samples']
item.evaluation = round(out['accuracy'],2)
item.save()

#Tue Sep 27 20:53:23 AST 2016
#Data length:  65672
#(65672, 164239)
#0.566613879076
#out
#{'training_samples': 49254, 'accuracy': 0.55841149957363867}
#Wed Sep 28 03:42:37 AST 2016
