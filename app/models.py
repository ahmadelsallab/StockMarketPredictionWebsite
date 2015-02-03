"""
Definition of models.
"""

from django.db import models
import json
from django.http import HttpResponse

class Opinion(models.Model):
    twitter_id = models.CharField(max_length=40)
    user_id = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    created_at = models.CharField(max_length=100)
    user_followers_count = models.IntegerField()
    user_profile_image_url = models.CharField(max_length=500)
    pub_date = models.CharField(max_length=100)
    relevancy = models.CharField(max_length=40)
    sentiment = models.CharField(max_length=40)
    labeled_user = models.CharField(max_length=40)
    stock = models.CharField(max_length=40)
    labeled = models.BooleanField(default=False)
    source = models.CharField(max_length=600)
    '''
    def render_to_response(self, context, **response_kwargs):
        #return HttpResponse(json.dumps(list(self.get_queryset().values_list('code', flat=True))),mimetype="application/json")
        return HttpResponse(json.dumps(list(self.get_queryset())), mimetype="application/json")
    '''
class StocksPrices(models.Model):
    stock_name = models.CharField(max_length=200)
    from django.core.validators import MaxValueValidator, MinValueValidator
    stock_price = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000.0)])
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
