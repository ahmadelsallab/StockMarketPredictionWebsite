from django.shortcuts import render
from django.template import RequestContext, loader
from django.views import generic

# Create your views here.
from django.http import HttpResponse
from freeuser.models import Opinion

from TwitterCrawler.TwitterCrawler import  *
twitterCrawler = None
polarityStyle = {'Positive' : 'alert alert-success', 'Negative' : 'alert alert-danger', 'Neutral' : 'alert alert-warning'}
def main(request):
    
    # Handle the query
    #--------------------    
    try:
        # Get the query entered by the user
        query = request.GET['searchbox']
        
        # Start the TwitterCrawler
        import os        
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        configFileCrawler = os.path.join(BASE_DIR, 'TwitterCrawler','Configurations', 'Configurations.xml')
        twitterCrawler = TwitterCrawler(configFileCrawler, None, None, None)
        results = twitterCrawler.SearchQueryAPI(query, -1, -1)
        #showsome(query)
        
        # Update the DB
        for result in results:
            opinion = Opinion(text=result['text'], sentiment=Opinion.Neutral, source_url='https://twitter.com/search?q='+query)        
            opinion.save()
        
    except Exception as e:
        # No query entered
        query = ""
            
    # Render the response
    #--------------------   
            
    # Load the main page template
    template = loader.get_template('freeuser/main.html')
    
    # Fill the query list
    opinion_list = Opinion.objects.order_by('text')[:1000]
    
    # Render with the query
    context = RequestContext(request, {'query': query, 'opinion_list' : opinion_list})
   
    return HttpResponse(template.render(context))

import json
import urllib.request, urllib.parse

def showsome(searchfor):
  query = urllib.parse.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.request.urlopen(url)
  search_results = search_response.read().decode("utf8")
  results = json.loads(search_results)
  data = results['responseData']
  print('Total results: %s' % data['cursor']['estimatedResultCount'])
  hits = data['results']
  print('Top %d hits:' % len(hits))
  for h in hits: print(' ', h['url'])
  print('For more results, see %s' % data['cursor']['moreResultsUrl'])
