'''
Created on Nov 27, 2014

@author: asallab
'''
from TwitterCrawler import TwitterCrawler
#import TwitterCrawler

# Configurations file xml of the crawler
configFileCrawler = "..\\configurations\\Configurations_TwitterCrawler.xml"

# CSV File
csvFileName = "..\\input_data\\V2-GS-R&R-TwitterSentimentCorpus2014-Ar - Short.csv"

# Serialization binary file name
serializatoinFileName = "..\\output_results\\results_tweets.bin"

# Start the TwitterCrawler
#-------------------------
import time

twitterCrawler = TwitterCrawler(configFileCrawler, None, None, serializatoinFileName)

twitterCrawler.GetTweetsByID(csvFileName)