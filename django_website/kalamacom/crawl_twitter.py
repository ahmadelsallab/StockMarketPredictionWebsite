'''
Created on Dec 11, 2014

@author: asallab
'''

from TwitterCrawler.TwitterCrawler import TwitterCrawler
import os
print(os.getcwd())
configFileName = ".\\TwitterCrawler\\Configurations\\Configurations.xml"
updateRateFileName = 'update_rate.txt'
twitterCrawler = TwitterCrawler(configFileName, None, updateRateFileName, '')
twitterCrawler.Crawl(True)