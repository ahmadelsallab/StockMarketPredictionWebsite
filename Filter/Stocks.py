"""
stocks = ['لازوردي']
"""

from app import models
stocks = [s.stock_id for s in models.Stocks.objects.filter()]