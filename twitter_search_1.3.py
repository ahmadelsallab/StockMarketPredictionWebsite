from twitter import *
from xml.dom import minidom
import datetime
import time
import sys

# Gets the max and min of the id   
def getMaxMinId(results):
    minId = results[0]['id'];
    maxId = results[0]['id'];
    for result in results:
        if(result['id'] > maxId):
            maxId = result['id']
        if(result['id'] < minId):
            minId = result['id']
    return maxId, minId

# Encapsulates the search iterations to handle more than 100 counts per call    
def twitterSearch(query, geocode, language, count, since_id):
    results = []
    sinceId = 0
    resultsAPI = t.search.tweets(q=query, geocode=geocode, lang=language, count=count, until=datetime.date.today(), since_id=since_id)
    results = resultsAPI['statuses'];
    while (results.__len__() < int(count) & results.__len__() > 0):
        # The returns are flipped intentionally
        temp, maxId = getMaxMinId(results)
        resultsAPI = t.search.tweets(q=query, geocode=geocode, lang=language, count=count, until=datetime.date.today(), since_id=since_id, max_id=maxId)
        results += resultsAPI['statuses'];       
    return results



#
# The rate of update in sec
UPDATE_RATE = 1.0

# Get the name of configuration file from the cmd line argument
#xmldoc = minidom.parse(sys.argv[1])    
xmldoc = minidom.parse("Configurations.xml")

# Parse XML configurations
# Get the query words
wordList = xmldoc.getElementsByTagName('Word') 
words = []
for word in wordList :
    words.append(word.attributes['name'].value)
query = ' OR '.join(words)    

# Get the geocode words
geocodeList = xmldoc.getElementsByTagName('GeocodeItem') 
geocodeStr = geocodeList[0].attributes['latitude'].value  + "," + geocodeList[1].attributes['longitude'].value + "," + geocodeList[2].attributes['radius'].value + ","

# Get the language
language = xmldoc.getElementsByTagName('Langurage')[0].attributes['language'].value

# Get the update period
updatePeriodStr = xmldoc.getElementsByTagName('UpdatePeriod')[0].attributes['updatePeriod'].value
if not updatePeriodStr == "forever" :
    updatePeriod = int(updatePeriodStr) / UPDATE_RATE
    
# Get the resultsLimit
resultsLimit = xmldoc.getElementsByTagName('ResultsLimit')[0].attributes['resultsLimit'].value
if(int(resultsLimit) < 100):
    numPages = 1
    resultsPerPage = resultsLimit
else:
    resultsPerPage = 100
    numPages = int(resultsLimit) / 100
    

# Authenticate twitter API
t = Twitter(
          auth=OAuth("1846277677-Sw5vuDcBqQdXOKZ5Pw1zLlDj8gFOfcD1L3VXx8F", "wfeTXOlxNJLXBjKBJqR6WvcD9duIjy8CrvJcsgxoqc",
                     "xNRGvHoz9L4xKGP28m7qbg", "oFv4dhBekboNg7pKa2BS0zztHqusr91SIdmKErDaycI")
          )
# Open the log file
f = open('feeds.log', 'w')

# Start updates
updateCnt = 0
sinceId = 0
while True:
    # Search for the required query with the configured options
    # For the first search, use since_id = 0 and don't set max_id, so all results since now are obtained
    results = twitterSearch(query=query, geocode=geocodeStr, language=language, count=resultsLimit, since_id=sinceId)

    # The next since_id is the most recent one of the current search
    #sinceId = results['search_metadata']['max_id']
    if(results.__len__() > 0):
        sinceId, temp = getMaxMinId(results)
    #temp = getMaxMinId(results)
    for result in results:
        try:
            # Print on console
            try:
                if not (sys.argv[2] == "q"):
                    print(result['text'])
            except IndexError:
                print(result['text'])
          
         
            # Write to logs file
            f.write(result['text'] + "\n")         
        except:
            continue
   
    # No stop condition in case of "forever" setting
    if not updatePeriodStr == "forever" :
        updateCnt += 1
        if updateCnt >= updatePeriod :
            break
   
    # Wait for the update period   
    time.sleep(UPDATE_RATE)


   
