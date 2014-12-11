from django.db import models

# Create your models here.

class Opinion(models.Model):
    # Enum for sentiment classes
    Positive = 0
    Negative = 1
    Neutral = 2
    SENTIMENT_CLASSES = ((Positive, 'Positive'),
                        (Negative, 'Negative'),
                        (Neutral, 'Neutral'),)
    
    # The text of the opinion
    text = models.CharField(max_length=1000)
    
    #The sentiment of the opinion
    sentiment = models.IntegerField(max_length=10, choices=SENTIMENT_CLASSES, default=Neutral)
    
    source_url = models.CharField(max_length=100, default='Unknown')
    
    def __str__(self):
        return self.text
