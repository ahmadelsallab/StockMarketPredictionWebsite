'''
Created on Sep 30, 2013

@author: ASALLAB
'''
from twitter import *
from xml.dom import minidom
import datetime
import time
from random import randrange
import pickle
import csv

class TwitterCrawler(object):
    '''
    classdocs
    '''
    # Dummy value for existing key
    EXIST = 10
      
    # The limit of query in number of words, including operators
    QUERY_LIMIT_WORDS_OPERATORS = 10

    # The limit of query in number characters
    QUERY_LIMIT_CHAR = 100
    
    # The maximum number of returned results per search
    MAX_NUM_RESULTS_PER_SEARCH = 100
    
    # The rate limit is 180 call/15 min, so 5 secs between 2 successive calls
    API_CALL_PENALTY_DURATION = 5
    MAX_NUM_API_CALLS = 180
    
    # Backoff penalty period if no new tweets in secs
    BACKOFF_PENALTY_PERIOD_NO_NEW_TWEETS = 10
    
    # After this limit of no more older tweets, search reverses direction towards waiting new tweets
    LIMIT_NO_OLDER_TWEETS = 10
           
    def __init__(self, configFileName, feedsLogFileName, updateRateFileName, serializationFileName):
        '''
        Constructor
        '''
        
        # Parse the configurations file
        self.ParseConfigFile(configFileName)
        
        # Authenticate twitter API
        # Access token, Access token secret, Consumer key, Consumer secret
        self.t = Twitter(
                         auth=OAuth(self.accessToken, 
                                    self.accessTokenSecret,
                                    self.consumerKey, 
                                    self.consumerSecret)
                         )
        # Open the log file
        if(feedsLogFileName != None):
            self.logFile = open(feedsLogFileName, 'w', encoding='utf-8')    
        
        if(updateRateFileName != None):
            # Open the update rate file
            self.updateRateFile = open(updateRateFileName, 'w', encoding='utf-8')    

        # Save the serialization file name
        self.serializationFileName = serializationFileName
        # Initialize results
        self.results = []
        
        # Each time search returns no new tweets this counter is incremented. After it cross LIMIT_NO_OLDER_TWEETS start searching for more recent instead of older
        self.numberOfNoOlderTweets = 0
        
        self.stock = ''
    # The main crawler    
    def Crawl(self, quiet):
        # Start updates
        sinceId = -1
        
        # Store current time timestamp       
        startTime = time.time()
        
        self.tweetsCtr = 0
        while True:
            # Update the update rate log file with the current time
            self.updateRateFile.write("New crawl started at: " + str(datetime.datetime.now()) + "\n")
            print("New crawl started at: " + str(datetime.datetime.now()) + "\n")
            
            # Reset the call penalty counter
            self.callPenaltyCntr = 0
            
            if(self.numberOfNoOlderTweets < self.LIMIT_NO_OLDER_TWEETS):
                # Search for the required query with the configured options
                # For the first search, use since_id = 0 and don't set max_id, so all results since now are obtained
                resultsCrawl = self.Search(since_id=sinceId)
            else:
                # After this limit of no more older tweets, search reverses direction towards waiting new tweets
                self.updateRateFile.write("Search reversed to wait for recent tweets after " + str(self.LIMIT_NO_OLDER_TWEETS) + " attempts\n")
                print("Search reversed to wait for recent tweets after " + str(self.LIMIT_NO_OLDER_TWEETS) + " attempts\n")
                resultsCrawl = self.SearchRecent(since_id=sinceId)
                
            if (self.inhibitSavingToLocalStruct != "true"):
                # Append the results
                self.results.extend(resultsCrawl)
                
                # You must close and open to append to the binary file
                # Open the serialization file
                self.serializationFile = open(self.serializationFileName, 'wb')
                pickle.dump(self.results, self.serializationFile)
                # Open the serialization file
                self.serializationFile.close()
                # to read
                # f = open(file, 'rb')
                # results = pickle.load(f)             
        
            # The next since_id is the most recent one of the current search
            if(resultsCrawl.__len__() > 0):
                sinceId, temp = self.GetMaxMinId(resultsCrawl)
             
            for result in resultsCrawl:
                self.tweetsCtr += 1
                
                from app.models import Tweet
                from django.utils import timezone
                
                tweet_exist = Tweet.objects.filter(twitter_id=result['id_str']);
                if(len(tweet_exist) == 0):
                    opinion = Tweet(twitter_id=result['id_str'], user_id=result['user']['id'], text=result['text'], created_at=result['created_at'], user_followers_count=result['user']['followers_count'], user_profile_image_url=result['user']['profile_image_url'], pub_date=str(timezone.now()), stock=self.stock, labeled=False)        
                    opinion.save()
                if (self.inhibitLogFileSaving != "true"):
                    # Write to logs file
                    #self.logFile.write(result['text'] + "\n")  
                    self.tabs = ''
                    self.logFile.write(self.Dict2Xml(result, 'Tweet'))
                try:
                    # Print on console
                    try:
                        if not (quiet == "q"):
                            print(result['text'])
                    except IndexError:
                        print(result['text'])
       
                except:
                    continue
           
            # No stop condition in case of "forever" setting
            if not self.updatePeriodStr == "forever" :                
                if (int(time.time() - startTime)) >= self.updatePeriod :
                    break
            # A negative desired size means non-stop
            if self.desiredDataSize > 0:
                # If the results desired size is reached, then break 
                if(self.results.__len__() >= self.desiredDataSize):
                    break 
                
            # Wait for the API call penalty + random backoff due to no new results
            penaltyPeriod = self.callPenaltyCntr * self.API_CALL_PENALTY_DURATION + self.noOlderOrNewerTweets * randrange(1,10) * self.BACKOFF_PENALTY_PERIOD_NO_NEW_TWEETS
                            
            # Increment the counter of no older tweets
            self.numberOfNoOlderTweets += self.noOlderOrNewerTweets
            
            print("Going to sleep for penalty period: " + str(penaltyPeriod) + "\n")
            self.updateRateFile.write("Going to sleep for penalty period: " + str(penaltyPeriod) + "\n")
            time.sleep(penaltyPeriod)
                   
    # Gets the max and min of the id   
    def GetMaxMinId(self, results):
        minId = results[0]['id'];
        maxId = results[0]['id'];
        for result in results:
            if(result['id'] > maxId):
                maxId = result['id']
            if(result['id'] < minId):
                minId = result['id']
        return maxId, minId
    
    # Form array of queries out of long one, each query is only 1000 char
    def FormQueryList(self, queryWordsArray):
        if(len(queryWordsArray) > 0):       
            queryArray = []
            numQueryWordsAndOperators = 0
            
            # Loop on all words and append to the query list at the current index
            for word in  queryWordsArray:
                
                # Add the word to the current query list index if its length will not cross the limit 
                if(len(queryArray) != 0):                              
                    # Form the new query
                    newQuery = queryArray[len(queryArray) - 1] + " OR " + word
                    
                    # Add the new query word and OR operator
                    numQueryWordsAndOperators += 2 
                    
                    # Add it if it doesn't cross the limit
                    if((len(newQuery) <= self.QUERY_LIMIT_CHAR) & (numQueryWordsAndOperators > self.QUERY_LIMIT_WORDS_OPERATORS)):
                        
                        # Add the word to the current query
                        queryArray[len(queryArray) - 1] = newQuery                        

                    else:                        
                        # Start new query
                        queryArray.append(word)

                        # The new query contains now 1 word
                        numQueryWordsAndOperators = 1                                         

                else:
                    # Start new query
                    queryArray.append(word)
                    
                    # The new query contains now 1 word
                    numQueryWordsAndOperators = 1                                         
        return queryArray
    # Encapsulates long query > 1000 char limitation
    def SearchQuery(self, since_id, max_id):
        
        # Initialize the finalResults list
        finalResults = []
        # Initialize the search hash table
        searchHashTbl = {}
        for query in self.queryArray:
            # Log time of calling the API
            self.updateRateFile.write("Call the twitter search API:" + str(datetime.datetime.now()) + "\n")
            print("Call the twitter search API:" + str(datetime.datetime.now()) + "\n")
            try:
                # For each query all the search API
                if(max_id == -1):
                    if(since_id == -1):
                        resultsAPI = self.t.search.tweets(q=query,
                                                          #geocode=self.geocodeStr,
                                                          lang=self.language,
                                                          count=self.resultsPerSearch,
                                                          result_type='recent')
                    else:
                        resultsAPI = self.t.search.tweets(q=query,
                                                          #geocode=self.geocodeStr,
                                                          lang=self.language,
                                                          count=self.resultsPerSearch,
                                                          result_type='recent',
                                                          since_id=since_id)
                        
                else:
                    if(since_id == -1):
                        resultsAPI = self.t.search.tweets(q=query,
                                                          #geocode=self.geocodeStr,
                                                          lang=self.language,
                                                          count=self.resultsPerSearch,
                                                          result_type='recent',
                                                          max_id=max_id)
                    else:
                        resultsAPI = self.t.search.tweets(q=query,
                                                          #geocode=self.geocodeStr,
                                                          lang=self.language,
                                                          count=self.resultsPerSearch,
                                                          result_type='recent',
                                                          since_id=since_id,
                                                          max_id=max_id)                    
            except:
                print("HTTP error, most probably rate\n")
                # Increment the callPenaltyCntr
                self.callPenaltyCntr += 1
            # Increment the callPenaltyCntr
            self.callPenaltyCntr += 1
                
            try:        
                results = resultsAPI['statuses']
            
                # Add the results one by one, unless it already exists in the list
                for result in results:
                    # If the current result doesn't exist in the hash table then add it
                    if not result['text'] in searchHashTbl:
                        # Update hash table
                        searchHashTbl[result['text']] = self.EXIST
                        
                        # Add to final results list
                        finalResults.append(result)
                                           
                        # Update the update rate log file with the current time
                        self.updateRateFile.write("New Tweet at: " + str(datetime.datetime.now()) + "\n")
                        print("New Tweet at: " + str(datetime.datetime.now()) + "\n")
            except:
                print("HTTP error, most probably rate\n")
            # The rate might be already about to be crossed
            if(self.callPenaltyCntr >= (self.MAX_NUM_API_CALLS - 1)):
                # Sleep for some time to handle the rate limitation
                time.sleep(self.callPenaltyCntr * self.API_CALL_PENALTY_DURATION)
                
                print("API Rate is crossed. Going to sleep: " + str(self.callPenaltyCntr))
                
                # Reset the call counter as we already did the wait
                self.callPenaltyCntr = 0        
        return finalResults
    
    # Encapsulates the search iterations to handle more than 100 counts per call    
    def Search(self, since_id):
        resultsQuery = self.SearchQuery(since_id=since_id, max_id=-1)
        results = resultsQuery 
        while ((results.__len__() < int(self.resultsLimit)) & (resultsQuery.__len__() > 0)):
            # The returns are flipped intentionally, so that the new search finds the tweets older than the oldest one in 
            # the current returned results, i.e. with max_id < lowest max_id of the current resultsQuery
            temp, maxId = self.GetMaxMinId(resultsQuery)
            resultsQuery = self.SearchQuery(since_id=since_id, max_id=maxId)
            results += resultsQuery
            
            # The rate might be already about to be crossed
            if(self.callPenaltyCntr >= (self.MAX_NUM_API_CALLS - 1)):
                # Sleep for some time to handle the rate limitation
                time.sleep(self.callPenaltyCntr * self.API_CALL_PENALTY_DURATION)
                
                print("API Rate is crossed. Going to sleep: " + str(self.callPenaltyCntr))
                
                # Reset the call counter as we already did the wait
                self.callPenaltyCntr = 0        
        self.noOlderOrNewerTweets = (results.__len__() == 0)
        return results
    
    # Encapsulates long query > 1000 char limitation
    def SearchQueryAPI(self, query, since_id, max_id):
        
        # Initialize the finalResults list
        finalResults = []
        # Initialize the search hash table
        searchHashTbl = {}
        # Log time of calling the API
        print("Call the twitter search API:" + str(datetime.datetime.now()) + "\n")
        try:
            # For each query all the search API
            if(max_id == -1):
                if(since_id == -1):
                    resultsAPI = self.t.search.tweets(q=query,
                                                      #geocode=self.geocodeStr,
                                                      lang=self.language,
                                                      count=self.resultsPerSearch,
                                                      result_type='recent')
                else:
                    resultsAPI = self.t.search.tweets(q=query,
                                                      #geocode=self.geocodeStr,
                                                      lang=self.language,
                                                      count=self.resultsPerSearch,
                                                      result_type='recent',
                                                      since_id=since_id)
                    
            else:
                if(since_id == -1):
                    resultsAPI = self.t.search.tweets(q=query,
                                                      #geocode=self.geocodeStr,
                                                      lang=self.language,
                                                      count=self.resultsPerSearch,
                                                      result_type='recent',
                                                      max_id=max_id)
                else:
                    resultsAPI = self.t.search.tweets(q=query,
                                                      #sgeocode=self.geocodeStr,
                                                      lang=self.language,
                                                      count=self.resultsPerSearch,
                                                      result_type='recent',
                                                      since_id=since_id,
                                                      max_id=max_id)                    
        except Exception as e:
            print("HTTP error, most probably rate\n")

            
        try:        
            results = resultsAPI['statuses']
        
            # Add the results one by one, unless it already exists in the list
            for result in results:
                # If the current result doesn't exist in the hash table then add it
                if not result['text'] in searchHashTbl:
                    # Update hash table
                    searchHashTbl[result['text']] = self.EXIST
                    
                    # Add to final results list
                    finalResults.append(result)
                                       
                    # Update the update rate log file with the current time
                    print("New Tweet at: " + str(datetime.datetime.now()) + "\n")
        except:
            print("No results returned")
       
        return finalResults     
     
    # Encapsulates the search iterations to handle more than 100 counts per call    
    def SearchRecent(self, since_id):
        resultsQuery = self.SearchQuery(since_id=since_id, max_id=-1)
        results = resultsQuery 
        # The returns are flipped intentionally, so that the new search finds the tweets older than the oldest one in 
        # the current returned results, i.e. with max_id < lowest max_id of the current resultsQuery
        # Register here the most recent tweet (sinceId = maximum id of resultsQuery) so that any more recent tweet is obtained

        while ((results.__len__() < int(self.resultsLimit)) & (resultsQuery.__len__() > 0)):
            sinceId, temp = self.GetMaxMinId(resultsQuery)
            resultsQuery = self.SearchQuery(since_id=sinceId, max_id=-1)
            results += resultsQuery
                       
            # The rate might be already about to be crossed
            if(self.callPenaltyCntr >= (self.MAX_NUM_API_CALLS - 1)):
                # Sleep for some time to handle the rate limitation
                time.sleep(self.callPenaltyCntr * self.API_CALL_PENALTY_DURATION)
                
                print("API Rate is crossed. Going to sleep: " + str(self.callPenaltyCntr))
                
                # Reset the call counter as we already did the wait
                self.callPenaltyCntr = 0        
        # This should also increment here to account for penalty in case of recent search
        self.noOlderOrNewerTweets = (results.__len__() == 0)
        return results    
    # Parse the configurations file
    def ParseConfigFile(self, configDocName):
        # Get the name of configuration file from the cmd line argument
        xmldoc = minidom.parse(configDocName)    
        
        # Parse XML configurations
        # Get OAuth data
        self.accessToken = xmldoc.getElementsByTagName('AccessToken')[0].attributes['accessToken'].value
        self.accessTokenSecret = xmldoc.getElementsByTagName('AccessTokenSecret')[0].attributes['accessTokenSecret'].value
        self.consumerKey = xmldoc.getElementsByTagName('ConsumerKey')[0].attributes['consumerKey'].value
        self.consumerSecret = xmldoc.getElementsByTagName('ConsumerSecret')[0].attributes['consumerSecret'].value
        
        # Get the query words
        wordList = xmldoc.getElementsByTagName('Word') 
        words = []
        for word in wordList :
            words.append(word.attributes['name'].value) 
        
        # For the array of queries
        if(words.__len__() > 0):
            self.queryArray = self.FormQueryList(words)
        
        # Get the geocode words
        geocodeList = xmldoc.getElementsByTagName('GeocodeItem') 
        self.geocodeStr = geocodeList[0].attributes['latitude'].value  + "," + geocodeList[1].attributes['longitude'].value + "," + geocodeList[2].attributes['radius'].value + ","
        
        # Get the language
        self.language = xmldoc.getElementsByTagName('Language')[0].attributes['language'].value

        # Get the update period
        self.updatePeriodStr = xmldoc.getElementsByTagName('UpdatePeriod')[0].attributes['updatePeriod'].value
        if not self.updatePeriodStr == "forever" :
            self.updatePeriod = int(self.updatePeriodStr) * 60
            
        # Get the resultsLimit
        self.resultsLimit = xmldoc.getElementsByTagName('ResultsLimit')[0].attributes['resultsLimit'].value
        
        self.resultsPerSearch = min(int(self.resultsLimit), self.MAX_NUM_RESULTS_PER_SEARCH)  

        # Get the inhibitLogFileSaving
        self.inhibitLogFileSaving = xmldoc.getElementsByTagName('InhibitLogFileSaving')[0].attributes['inhibitLogFileSaving'].value

        # Get the inhibitLogFileSaving
        self.inhibitSavingToLocalStruct = xmldoc.getElementsByTagName('InhibitSavingToLocalStruct')[0].attributes['inhibitSavingToLocalStruct'].value

        # Get the desiredDataSize
        self.desiredDataSize = int(xmldoc.getElementsByTagName('DesiredDataSize')[0].attributes['desiredDataSize'].value)
                
    def Dict2Xml(self, d, root_node=None):
        wrap          =     False if None == root_node or isinstance(d, list) else True
        root          = 'objects' if None == root_node else root_node
        root_singular = root[:-1] if 's' == root[-1] and None == root_node else root
        xml           = ''
        children      = []
        self.tabs += '    '
        param = ''
        # Add the count attribute for the root node tweet
        if(root_node == 'Tweet'):
            xml = ' tweets_count=' + str(self.tweetsCtr) + '\n'
        
        # Add the id if exists
#        if(id != None):
#            xml = ' id=' + id + '\n'
#            d['id'] = id
        if isinstance(d, dict):
            for key, value in dict.items(d):
                try:
                    if isinstance(value, dict):
                        try:                            
                            # Keep foreign key with unique id. Example: user, user_mentions,...etc
                            xml = xml + ' ' + key + '_id="' + str(value['id']) + '"\n'
                            children.append(self.Dict2Xml(value, key))
                        except KeyError:   
                            # If no id in the child, add the parent id                         
                            xml = xml + ' ' + key + '_id="' + str(d['id']) + '"\n'
                            # Add the id as parameter in the child
                            value['id'] = d['id']
                            
                            # Pass the parent id to the child to be added
                            children.append(self.Dict2Xml(value, key))


                    elif isinstance(value, list):
                        try:                            
                            # Keep foreign key with unique id. Example: user, user_mentions,...etc
                            xml = xml + ' ' + key + '_id="' + str(value['id']) + '"\n'
                            children.append(self.Dict2Xml(value, key))
                        except KeyError:   
                            # If no id in the child, add the parent id                         
                            xml = xml + ' ' + key + '_id="' + str(d['id']) + '"\n'
                            # Add the id as parameter in the child
                            value['id'] = d['id']
                            
                            # Pass the parent id to the child to be added
                            children.append(self.Dict2Xml(value, key))
                    else:
                        if not (key == 'source'):                        
                            xml = xml + ' ' + key + '="' + str(value) + '"\n'
                except TypeError:
                    print()
                        
        else:
            for value in d:
                children.append(self.Dict2Xml(value, root_singular))
     
        end_tag = '>\n' if 0 < len(children) else '>\n</' + root + '>\n'
     
        if wrap or isinstance(d, dict):
            xml = '<' + root + xml + end_tag     
        if 0 < len(children):
            for child in children:
                xml = xml + child
     
            if wrap or isinstance(d, dict):
                xml = xml + '</' + root + '>\n'
        return xml        
    
    # Utility to get single tweet
    def GetSingleTweetByID(self, tweetID):
        return self.t.statuses.show(id = tweetID)
    
    def GetTweetsByID(self, csvFileName):
        
        # Open serializaiton file
        if(self.serializationFileName != None):
            serializationFile = open(self.serializationFileName, 'wb')
        
        # Open csv for reading
        csvFile = open(csvFileName, 'r', encoding='UTF-8', newline='')
        
        # Get reader handler
        rows = csv.reader(csvFile, delimiter=',')
        
        
        # Skip the first row
        skip = True
        
        colomns = []
        
        rowNum = 0
        
        # The tweets objects as returned by twitter
        tweets = []
        
        # The tweets label info from csv file
        tweetsLabelData = []
        
        # Read the label from each row
        for row in rows:
            if(skip):
                # Get the folomns names
                for item in row:
                    colomns.append(item.replace('\'', '').strip())
                skip = False 
            else:
                print('Get tweetData ID for row number: ' + str(rowNum))
                
                singleTweetData = {}
                
                # Fill in example colomns from the csv file
                i = 0
                for item in row:
                    singleTweetData[colomns[i]] = item.replace('\'', '').strip()
                    i += 1
                    
                
                try:
                                        
                    # Get the tweet by ID 
                    retrievedTweet = dict(self.GetSingleTweetByID(singleTweetData['tweetID']))
                    
                    # Update the text in the tweet data
                    singleTweetData['tweetText'] = retrievedTweet['text']
                    retrievedTweet['label'] = singleTweetData['Sentiment']
                    
                    # Update the final list of tweets
                    tweets.append(retrievedTweet)
                    tweetsLabelData.append(singleTweetData)
                except Exception as e:
                    # Rate limit exceeded
                    print('Error: ' + str(e)) 
                    if('Twitter sent status 429' in str(e)):
                        # Sleep 15 min, only 180 calls permitted per 15 min
                        time.sleep(900)
                # Add in the results
                
                
            
            rowNum += 1
        
        # Serialize the results
        if(self.serializationFileName != None):
            pickle.dump(tweets, serializationFile)
            pickle.dump(tweetsLabelData, serializationFile)
            serializationFile.close()
        # Close the files   
        csvFile.close()
        
        
