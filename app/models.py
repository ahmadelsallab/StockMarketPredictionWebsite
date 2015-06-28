"""
Definition of models.
"""

from django.db import models
import json
from django.http import HttpResponse

class Opinion(models.Model):
    twitter_id = models.CharField(max_length=40)
    user_id = models.CharField(max_length=200)
    user_followers_count = models.IntegerField()
    user_profile_image_url = models.CharField(max_length=500)
    tweeter_name = models.CharField(max_length=100)
    tweeter_sname = models.CharField(max_length=40)
    text = models.CharField(max_length=200)
    created_at = models.CharField(max_length=100)
    pub_date = models.CharField(max_length=100)
    source = models.CharField(max_length=600)
    media_url = models.CharField(max_length=5000)
    stock = models.CharField(max_length=40)
    relevancy = models.CharField(max_length=40)
    relevancy_second = models.CharField(max_length=40)
    relevancy_third = models.CharField(max_length=40)
    sentiment = models.CharField(max_length=40)
    sentiment_second = models.CharField(max_length=40)
    sentiment_third = models.CharField(max_length=40)
    labeled_user = models.CharField(max_length=40)
    labeled_user_second = models.CharField(max_length=40)
    labeled_user_third = models.CharField(max_length=40)
    voted_relevancy = models.CharField(max_length=40)
    voted_sentiment =  models.CharField(max_length=40)
    labeled = models.BooleanField(default=False)
    manual_labeled = models.BooleanField(default=False)
    similarId = models.CharField(max_length=40)
    '''
    def render_to_response(self, context, **response_kwargs):
        #return HttpResponse(json.dumps(list(self.get_queryset().values_list('code', flat=True))),mimetype="application/json")
        return HttpResponse(json.dumps(list(self.get_queryset())), mimetype="application/json")
    '''
class StocksPrices(models.Model):
    stock = models.CharField(max_length=40)
    from django.core.validators import MaxValueValidator, MinValueValidator
    close = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000.0)])
    max = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000.0)])
    min = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000.0)])
    open = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000.0)])
    volume = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000000.0)])
    time = models.DateTimeField()
    '''
    def __str__(self):
        return self.stock_name
    '''
class CorrectionData(models.Model):

    text = models.CharField(max_length=200)
    relevancy = models.CharField(max_length=200)
    sentiment = models.CharField(max_length=200)
    stock = models.CharField(max_length=100)
    
    def __str__(self):
        return self.text

class LabledCounter(models.Model):
    stock = models.CharField(max_length=40)
    counter = models.BigIntegerField(max_length=21)
    
class StockCounter(models.Model):
    stock = models.CharField(max_length=40)
    counter = models.BigIntegerField(max_length=21)

class RelevancyCounter(models.Model):
    stock = models.CharField(max_length=40)
    relevancy = models.CharField(max_length=200)
    counter = models.BigIntegerField(max_length=21)

class SentimentCounter(models.Model):
    stock = models.CharField(max_length=40)
    sentiment = models.CharField(max_length=200)
    counter = models.BigIntegerField(max_length=21)

class DailyPrices(models.Model):
    stock = models.CharField(max_length=40)
    day = models.CharField(max_length=20) 
    min = models.CharField(max_length=20)
    max = models.CharField(max_length=20)
    concat = models.CharField(max_length=800)

class WeeklyPrices(models.Model):
    stock = models.CharField(max_length=40)
    week = models.CharField(max_length=20) 
    min = models.CharField(max_length=20)
    max = models.CharField(max_length=20)
    concat = models.CharField(max_length=3500)

class UserCounter(models.Model):
    stock = models.CharField(max_length=40)
    labeled_user = models.CharField(max_length=40)
    relevancy = models.CharField(max_length=200)
    counter = models.BigIntegerField(max_length=21)

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
