from Filter import FilterStocks
import unicodedata
from datetime import datetime
from app.models import Opinion,Stocks,StocksPrices, Evaluation,Sources
from django.utils import timezone
from Filter.Filter import Filter
import threading, time
import datetime
from django.utils import timezone
import re
import os


import django
django.setup()

save_path = 'data'
f1 = FilterStocks.Filter.init(save_path)
evalutaions = FilterStocks.Filter.evaluate(save_path)
timenow = timezone.now()

for x in Stocks.objects.exclude(stock_id__in=[1,2,4,5]):
    line = x.stock_id
    stock_name = x.stock
    #tweetes_to_render = Opinion.objects.filter(stock=line,created_at__isnull=False,stocksprices_id__isnull=True).order_by('-created_at');
    #month_ago = timezone.now() - timedelta(days=30)
    item = Evaluation()
    item.time = timenow
    item.stock_id = line
    item.classifier = 'r'
    try:
        item.evaluation = evalutaions[x.stock_id]['accuracy']
        item.training_sample = evalutaions[x.stock_id]['training_samples']
    except:
        item.evaluation = 0
    item.save()

