'''
Created on Dec 11, 2014

@author: asallab
'''

import os
os.environ["DJANGO_SETTINGS_MODULE"] = "DjangoWebProject1.settings"
#print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx")
#print(os.environ.get("DJANGO_SETTINGS_MODULE"))


from TwitterCrawler.TwitterCrawler import TwitterCrawler
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
configFileName = os.path.join(PROJECT_DIR, 'TwitterCrawler', 'Configurations', 'Configurations.xml')
updateRateFileName = 'update_rate.txt'
f_in = open(os.path.join('.', 'TwitterCrawler', 'stocks.txt'), 'r', encoding='utf-8')
lines = f_in.readlines()
for line in lines:            
    stock = line.strip()
    serializatoinFileName = ".\\TwitterCrawler\\Output\\results_" + stock + ".bin"
    twitterCrawler = TwitterCrawler(configFileName, None, updateRateFileName, serializatoinFileName)
    twitterCrawler.queryArray = []
    twitterCrawler.queryArray.append(stock + " AND (سهم OR اسهم OR أسهم OR تداول OR ارتفع OR ارتفاع OR انخفض OR انخفاض OR هدف OR دعم OR ارتداد OR نسبة OR % OR %)‎")
    twitterCrawler.stock = stock
    twitterCrawler.Crawl("q")