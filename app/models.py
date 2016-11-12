"""
Definition of models.
"""

from django.db import models
import json
from django.http import HttpResponse

class Sectors(models.Model):
    sector_id = models.IntegerField(unique=True)
    sector = models.CharField(max_length=60)

class Sources(models.Model):
    source_id = models.SmallIntegerField(unique=True)
    source = models.CharField(max_length=160)

class Matrix(models.Model):
    item = models.CharField(max_length=300)

class Tweeter(models.Model):
    tweeter_id = models.IntegerField(unique=True)
    tweeter_followers_count = models.IntegerField()
    tweeter_followings_count = models.IntegerField()
    tweeter_profile_image_url = models.CharField(max_length=200)
    tweeter_location = models.CharField(max_length=100)
    tweeter_name = models.CharField(max_length=40)
    tweeter_sname = models.CharField(max_length=40)
    tweeter_default_language = models.CharField(max_length=16)
    tweeter_time_zone = models.CharField(max_length=40)
    tweeter_gender = models.CharField(max_length=20)
    tweeter_age = models.IntegerField()
    tweeter_classification = models.CharField(max_length=30)
    tweeter_block = models.BooleanField(default=None)
    tweeter_statuses_count = models.IntegerField()
    tweeter_likes = models.IntegerField()
    tweeter_created_at = models.DateTimeField()
    tweeter_description = models.CharField(max_length=200)
    tweeter_verified = models.BooleanField(default=False)
    pass

class Stocks(models.Model):
    stock_id = models.SmallIntegerField(unique=True)
    stock = models.CharField(max_length=40)
    symbol = models.IntegerField()
    ISN = models.CharField(max_length=13)
    synonym = models.CharField(max_length=300)
    full_name_arabic = models.CharField(max_length=60)
    full_name_english = models.CharField(max_length=60)
    marketstoday_name = models.CharField(max_length=60)
    sector = models.ForeignKey(Sectors, on_delete=models.CASCADE, to_field='sector_id')
    pass

class Correction(models.Model):
    stock_id = models.SmallIntegerField()
    classifier = models.CharField(max_length=3)
    correction = models.BooleanField(default=False)
    segment = models.SmallIntegerField()
    counter = models.SmallIntegerField()
    stock_count = models.IntegerField()

class Evaluation(models.Model):
    time = models.DateTimeField()
    classifier = models.CharField(max_length=1)
    stock = models.SmallIntegerField()
    evaluation =  models.FloatField()
    stock = models.ForeignKey(Stocks , on_delete=models.CASCADE, to_field='stock_id')
    training_sample = models.IntegerField()

class StocksPrices(models.Model):
    from django.core.validators import MaxValueValidator, MinValueValidator
    close = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000.0)])
    max = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000.0)])
    min = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000.0)])
    open = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000.0)])
    volume = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000000.0)])
    time = models.DateTimeField()
    stock = models.ForeignKey(Stocks , on_delete=models.CASCADE, to_field='stock_id')

    '''
    def __str__(self):
        return self.stock_name
    '''
    pass

class Opinion(models.Model):
    twitter_id = models.BigIntegerField()
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    pub_date = models.CharField(max_length=100)
    media_url = models.CharField(max_length=5000)
    stock = models.SmallIntegerField()
    relevancy = models.CharField(max_length=40)
    relevancy_second = models.CharField(max_length=40)
    relevancy_third = models.CharField(max_length=40)
    sentiment = models.CharField(max_length=40)
    sentiment_second = models.CharField(max_length=40)
    sentiment_third = models.CharField(max_length=40)
    question = models.BooleanField(default=None)
    pricetarget = models.IntegerField()
    labeled_user = models.CharField(max_length=40)
    labeled_user_second = models.CharField(max_length=40)
    labeled_user_third = models.CharField(max_length=40)
    voted_relevancy = models.CharField(max_length=40)
    voted_sentiment =  models.CharField(max_length=40)
    labeled = models.BooleanField(default=False)
    head_opinion = models.BooleanField(default=False)
    similarId = models.BigIntegerField(default=None)
    conversation_reply = models.BigIntegerField()
    p_relevancy = models.CharField(max_length=40,default=None)
    p_sentiment = models.CharField(max_length=40,default=None)
    p_question = models.BooleanField(default=None)
    p_pricetarget = models.IntegerField(default=None)
    r_correction = models.BooleanField(default=None)
    r_correction_time = models.DateTimeField(default=None)
    s_correction = models.BooleanField(default=None)
    s_correction_time = models.DateTimeField(default=None)
    p_correction = models.BooleanField(default=None)
    p_correction_time = models.DateTimeField(default=None)
    q_correction = models.BooleanField(default=None)
    q_correction_time = models.DateTimeField(default=None)
    retweet_original = models.BigIntegerField()
    tweeter = models.ForeignKey(Tweeter, on_delete=models.CASCADE, to_field='tweeter_id')
    stock = models.ForeignKey(Stocks , on_delete=models.CASCADE, to_field='stock_id')
    stocksprices = models.ForeignKey(StocksPrices, on_delete=models.CASCADE, to_field='id')
    source = models.ForeignKey(Sources, on_delete=models.CASCADE, to_field='source_id')

    '''
    def render_to_response(self, context, **response_kwargs):
        #return HttpResponse(json.dumps(list(self.get_queryset().values_list('code', flat=True))),mimetype="application/json")
        return HttpResponse(json.dumps(list(self.get_queryset())), mimetype="application/json")
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
    counter = models.BigIntegerField()
    
class StockCounter(models.Model):
    stock = models.CharField(max_length=40)
    is_original = models.BooleanField(default=False)
    counter = models.BigIntegerField()

class RelevancyCounter(models.Model):
    stock = models.CharField(max_length=40)
    relevancy = models.CharField(max_length=200)
    counter = models.BigIntegerField()

class SentimentCounter(models.Model):
    stock = models.CharField(max_length=40)
    sentiment = models.CharField(max_length=200)
    is_original = models.BooleanField(default=False)
    counter = models.BigIntegerField()
    follower_counter = models.BigIntegerField()

class DailyPrices(models.Model):
    stock = models.CharField(max_length=40)
    day = models.CharField(max_length=20) 
    min = models.CharField(max_length=20)
    max = models.CharField(max_length=20)
    concat = models.CharField(max_length=800)

class PredictionCounter(models.Model):
    stock = models.CharField(max_length=40)
    day = models.CharField(max_length=40)
    classifier = models.CharField(max_length=1)
    prediction = models.CharField(max_length=40)
    counter = models.BigIntegerField()

class WeeklyPrices(models.Model):
    stock = models.CharField(max_length=40)
    week = models.CharField(max_length=20) 
    min = models.CharField(max_length=20)
    max = models.CharField(max_length=20)
    concat = models.CharField(max_length=3500)

class DailySentiment(models.Model):
    stock = models.CharField(max_length=40)
    day = models.DateTimeField()
    sentiment = models.CharField(max_length=40)
    counter = models.BigIntegerField()

class UserCounter(models.Model):
    stock = models.CharField(max_length=40)
    labeled_user = models.CharField(max_length=40)
    relevancy = models.CharField(max_length=200)
    counter = models.BigIntegerField()

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
