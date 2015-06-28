from datetime import datetime
from app.models import Opinion
from django.utils import timezone
from Filter.Filter import Filter
import threading, time
import datetime
import os
import re


import django
django.setup()



stock_list=[
##'ﺕﺎﺴﻳ',
##'ﺎﻟﺮﻳﺎﺿ',
##'ﺎﻠﺟﺰﻳﺭﺓ',
##'ﺎﺴﺘﺜﻣﺍﺭ',
##'ﺎﻠﺴﻋﻭﺪﻳ ﺎﻠﻫﻮﻠﻧﺪﻳ',
##'ﺎﻠﺴﻋﻭﺪﻳ ﺎﻠﻓﺮﻨﺴﻳ',
##'ﺱﺎﺑ',
##'ﺎﻠﻋﺮﺒﻳ ﺎﻟﻮﻄﻨﻳ',
'ﺱﺎﻤﺑﺍ',
##'ﺎﻟﺭﺎﺠﺤﻳ',
##'ﺎﻠﺑﻻﺩ',
##'ﺍﻺﻨﻣﺍﺀ',
##'ﻚﻴﻣﺎﻧﻮﻟ',
##'ﺐﺗﺭﻮﻜﻴﻣ',
##'ﺱﺎﺒﻛ',
'ﺱﺎﻔﻛﻭ',
##'ﺎﻠﺘﺼﻨﻴﻋ',
##'ﺎﻠﻠﺠﻴﻧ',
##'ﻦﻣﺍﺀ ﻞﻠﻜﻴﻣﺍﻮﻳﺎﺗ',
##'ﺎﻠﻤﺠﻣﻮﻋﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ',
##'ﺎﻠﺼﺣﺭﺍﺀ ﻞﻠﺒﺗﺭﻮﻜﻴﻣﺍﻮﻳﺎﺗ',
'ﻲﻨﺳﺎﺑ',
##'ﺲﺒﻜﻴﻣ ﺎﻠﻋﺎﻠﻤﻳﺓ',
##'ﺎﻠﻤﺘﻗﺪﻣﺓ',
##'ﻚﻳﺎﻧ',
'ﺐﺗﺭﻭ ﺭﺎﺒﻏ',
##'ﺄﺴﻤﻨﺗ ﺡﺎﺌﻟ',
##'ﺄﺴﻤﻨﺗ ﻦﺟﺭﺎﻧ',
##'ﺎﺴﻤﻨﺗ ﺎﻠﻣﺪﻴﻧﺓ',
##'ﺎﺴﻤﻨﺗ ﺎﻠﺸﻣﺎﻠﻳﺓ',
##'ﺍﻼﺴﻤﻨﺗ ﺎﻠﻋﺮﺒﻳﺓ',
##'ﺎﺴﻤﻨﺗ ﺎﻠﻴﻣﺎﻣﺓ',
##'ﺎﺴﻤﻨﺗ ﺎﻠﺴﻋﻭﺪﻴﻫ',
##'ﺎﺴﻤﻨﺗ ﺎﻠﻘﺼﻴﻣ',
##'ﺎﺴﻤﻨﺗ ﺎﻠﺠﻧﻮﺒﻴﻫ',
##'ﺎﺴﻤﻨﺗ ﻲﻨﺒﻋ',
##'ﺎﺴﻤﻨﺗ ﺎﻠﺷﺮﻘﻳﺓ',
##'ﺎﺴﻤﻨﺗ ﺖﺑﻮﻛ',
##'ﺎﺴﻤﻨﺗ ﺎﻠﺟﻮﻓ',
##'ﺄﺳﻭﺎﻗ ﻉ ﺎﻠﻌﺜﻴﻣ',
##'ﺎﻠﻣﻭﺎﺳﺍﺓ',
##'ﺈﻜﺴﺗﺭﺍ',
##'ﺪﻠﻫ ﺎﻠﺼﺤﻳﺓ',
##'ﺮﻋﺎﻳﺓ',
##'ﺱﺎﺴﻛﻭ',
##'ﺚﻣﺍﺭ',
##'ﻢﺠﻣﻮﻋﺓ ﻒﺘﻴﺤﻳ',
##'ﺝﺮﻳﺭ',
##'ﺎﻟﺩﺮﻴﺳ',
##'ﺎﻠﺤﻜﻳﺭ',
##'ﺎﻠﺨﻠﻴﺟ ﻞﻠﺗﺩﺮﻴﺑ',
##'ﺎﻠﻏﺍﺯ ﻭﺎﻠﺘﺼﻨﻴﻋ',
##'ﻚﻫﺮﺑﺍﺀ ﺎﻠﺴﻋﻭﺪﻳﺓ',
##'ﻢﺠﻣﻮﻋﺓ ﺹﺎﻓﻭﻻ',
##'ﺎﻠﻏﺫﺎﺌﻳﺓ',
'ﺱﺩﺎﻔﻛﻭ',
##'ﺎﻠﻣﺭﺎﻌﻳ',
##'ﺄﻨﻋﺎﻣ ﺎﻠﻗﺎﺒﺿﺓ',
##'ﺢﻟﻭﺎﻨﻳ ﺈﺧﻭﺎﻧ',
##'ﻩﺮﻔﻳ ﻝﻸﻏﺬﻳﺓ',
##'ﺎﻠﺘﻣﻮﻴﻧ',
##'ﻥﺍﺪﻛ',
##'ﺎﻠﻘﺼﻴﻣ ﺎﻟﺯﺭﺎﻌﻴﻫ',
##'ﺖﺑﻮﻛ ﺎﻟﺯﺭﺎﻌﻴﻫ',
##'ﺍﻸﺴﻣﺎﻛ',
##'ﺎﻠﺷﺮﻘﻳﺓ ﻞﻠﺘﻨﻤﻳﺓ',
##'ﺎﻠﺟﻮﻓ ﺎﻟﺯﺭﺎﻌﻴﻫ',
##'ﺐﻴﺷﺓ ﺎﻟﺯﺭﺎﻌﻴﻫ',
##'ﺝﺍﺯﺎﻧ ﻞﻠﺘﻨﻤﻳﺓ',
##'ﺍﻼﺘﺻﺍﻼﺗ',
##'ﺎﺘﺣﺍﺩ ﺎﺘﺻﺍﻼﺗ',
##'ﺰﻴﻧ ﺎﻠﺴﻋﻭﺪﻳﺓ',
##'ﻉﺬﻴﺑ ﻝﻼﺘﺻﺍﻼﺗ',
##'ﺎﻠﻤﺘﻛﺎﻤﻟﺓ',
##'ﺎﻠﺘﻋﺍﻮﻨﻳﺓ',
##'ﻡﻻﺫ ﻞﻠﺗﺄﻤﻴﻧ',
'ﻢﻳﺪﻐﻠﻓ ﻞﻠﺗﺄﻤﻴﻧ',
##'ﺄﻠﻳﺎﻧﺯ ﺈﺳ ﺈﻓ',
##'ﺱﻼﻣﺓ',
##'ﻭﻻﺀ ﻞﻠﺗﺄﻤﻴﻧ',
##'ﺎﻟﺩﺮﻋ ﺎﻠﻋﺮﺒﻳ',
##'ﺱﺎﺑ ﺖﻛﺎﻔﻟ',
##'ﺲﻧﺩ',
##'ﺱﺎﻴﻛﻭ',
##'ﻮﻓﺍ ﻞﻠﺗﺄﻤﻴﻧ',
##'ﺈﺘﺣﺍﺩ ﺎﻠﺨﻠﻴﺟ',
##'ﺍﻸﻬﻠﻳ ﻞﻠﺘﻛﺎﻔﻟ',
##'ﺍﻸﻬﻠﻳﺓ',
##'ﺄﺴﻴﺟ',
##'ﺎﻠﺗﺄﻤﻴﻧ ﺎﻠﻋﺮﺒﻳﺓ',
##'ﺍﻼﺘﺣﺍﺩ ﺎﻠﺘﺟﺍﺮﻳ',
##'ﺎﻠﺼﻗﺭ ﻞﻠﺗﺄﻤﻴﻧ',
##'ﺎﻠﻤﺘﺣﺩﺓ ﻞﻠﺗﺄﻤﻴﻧ',
##'ﺍﻺﻋﺍﺩﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ',
##'ﺏﻮﺑﺍ ﺎﻠﻋﺮﺒﻳﺓ',
##'ﻮﻗﺎﻳﺓ ﻞﻠﺘﻛﺎﻔﻟ',
##'ﺖﻛﺎﻔﻟ ﺎﻟﺭﺎﺠﺤﻳ',
##'ﺎﻴﺳ',
##'ﺎﻜﺳﺍ- ﺎﻠﺘﻋﺍﻮﻨﻳﺓ',
##'ﺎﻠﺨﻠﻴﺠﻳﺓ ﺎﻠﻋﺎﻣﺓ',
##'ﺏﺭﻮﺟ ﻞﻠﺗﺄﻤﻴﻧ',
##'ﺎﻠﻋﺎﻠﻤﻳﺓ',
##'ﺱﻮﻠﻳﺩﺮﺘﻳ ﺖﻛﺎﻔﻟ',
##'ﺎﻟﻮﻄﻨﻳﺓ',
##'ﺄﻣﺎﻧﺓ ﻞﻠﺗﺄﻤﻴﻧ',
##'ﻊﻧﺎﻳﺓ',
##'ﺍﻺﻨﻣﺍﺀ ﻁﻮﻜﻳﻭ ﻡ',
##'ﺎﻠﻤﺻﺎﻔﻳ',
##'ﺎﻠﻤﺘﻃﻭﺭﺓ',
##'ﺍﻼﺤﺳﺍﺀ ﻞﻠﺘﻨﻤﻴﻫ',
'ﺲﻴﺴﻛﻭ',
##'ﻊﺴﻳﺭ',
##'ﺎﻠﺑﺎﺣﺓ',
##'ﺎﻠﻤﻤﻠﻛﺓ',
##'ﺖﻛﻮﻴﻧ',
##'ﺏﻯ ﺱﻯ ﺁﻯ',
##'ﻢﻋﺍﺪﻧ',
##'ﺄﺴﺗﺭﺍ ﺎﻠﺼﻧﺎﻌﻳﺓ',
##'ﻢﺠﻣﻮﻋﺓ ﺎﻠﺳﺮﻴﻋ',
##'ﺵﺎﻛﺭ',
##'ﺎﻟﺩﻭﺎﺌﻳﺓ',
##'ﺰﺟﺎﺟ',
##'ﻒﻴﺒﻛﻭ',
##'ﻢﻋﺪﻨﻳﺓ',
##'ﺎﻠﻜﻴﻤﻳﺎﺌﻴﻫ ﺎﻠﺴﻋﻭﺪﻴﻫ',
##'ﺺﻧﺎﻋﺓ ﺎﻟﻭﺮﻗ',
##'ﺎﻠﻌﺑﺩﺎﻠﻠﻄﻴﻓ',
##'ﺎﻠﺻﺍﺩﺭﺎﺗ',
##'ﺄﺳﻼﻛ',
##'ﻢﺠﻣﻮﻋﺓ ﺎﻠﻤﻌﺠﻟ',
##'ﺍﻸﻧﺎﺒﻴﺑ ﺎﻠﺴﻋﻭﺪﻳﺓ',
##'ﺎﻠﺨﺿﺮﻳ',
##'ﺎﻠﺧﺰﻓ',
##'ﺎﻠﺠﺒﺳ',
##'ﺎﻠﻛﺎﺑﻼﺗ',
##'ﺹﺪﻗ',
##'ﺎﻤﻳﺎﻨﺘﻴﺗ',
##'ﺄﻧﺎﺒﻴﺑ',
##'ﺎﻟﺯﺎﻤﻟ ﻞﻠﺼﻧﺎﻋﺓ',
##'ﺎﻠﺑﺎﺒﻄﻴﻧ',
##'ﺎﻠﻔﺧﺍﺮﻳﺓ',
##'ﻢﺴﻛ',
##'ﺎﻠﺒﺣﺭ ﺍﻸﺤﻣﺭ',
##'ﺎﻠﻌﻗﺍﺮﻳﺓ',
##'ﻂﻴﺑﺓ ﻝﻼﺴﺘﺜﻣﺍﺭ',
##'ﻢﻛﺓ ﻝﻼﻨﺷﺍﺀ',
##'ﺎﻠﺘﻌﻤﻳﺭ',
##'ﺈﻌﻣﺍﺭ',
##'ﺞﺒﻟ ﻊﻣﺭ',
##'ﺩﺍﺭ ﺍﻷﺮﻛﺎﻧ',
##'ﻡﺪﻴﻧﺓ ﺎﻠﻤﻋﺮﻓﺓ',
##'ﺎﻠﺒﺣﺮﻳ',
##'ﺎﻠﻨﻘﻟ ﺎﻠﺠﻣﺎﻌﻳ',
##'ﻢﺑﺭﺩ',
##'ﺏﺪﺠﺗ ﺎﻠﺴﻋﻭﺪﻳﺓ',
##'ﺖﻫﺎﻤﻫ ﻝﻼﻋﻼﻧ',
##'ﺍﻸﺒﺣﺎﺛ ﻭ ﺎﻠﺘﺳﻮﻴﻗ',
##'ﻂﺑﺎﻋﺓ ﻮﺘﻐﻠﻴﻓ',
##'ﺎﻠﻄﻳﺍﺭ',
##'ﺎﻠﺤﻜﻳﺭ',
##'دور',
##'ﺶﻤﺳ',
##'البنك الأهلي',
##'الصناعات الكهربائيه',
##'بوان',
##'ﺎﺴﻤﻨﺗ ﺎﻣ ﺎﻠﻗﺭﻯ',
##'ﺄﺳﻭﺎﻗ ﺎﻠﻣﺯﺮﻋﺓ',
##'ﺎﻠﺤﻣﺍﺪﻳ',
##'ﺝﺰﻳﺭﺓ ﺖﻛﺎﻔﻟ',
##'ﺎﻠﻋﺮﺒﻳ ﻞﻠﺗﺄﻤﻴﻧ',
##'ﻢﺠﻣﻮﻋﺓ ﺎﻠﺤﻜﻳﺭ',
##'ميبكو',
##'ساكو',
##'الشركة السعودية للخدمات الأرضية',
];



print("Handling Dublicates")
for line in stock_list:
    print(line);
    tweetes_to_render_temp = Opinion.objects.filter(stock=line, labeled = False, similarId='').values().order_by('-id')
    tweetes_to_render = sorted(tweetes_to_render_temp, key=lambda x: time.strptime(x['created_at'],'%a %b %d %X %z %Y'))
    tweets_dict = {}
    tweets_dict[''] = ''
    i = 1
    x = 0
    while x < len(tweetes_to_render):
        tweet_render=tweetes_to_render[x];
        tweet_render_text=tweet_render.get('text').strip()
        try:
            urls=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet_render_text);
            for i in range(0,len(urls)):
                rep='r\''+urls[i]+'\''
                tweet_render_text=re.sub(r""+urls[i]+"", '', tweet_render_text, flags=re.MULTILINE)
        except:
            pass

        tweet_render_text=re.sub(r"RT @\w*\w: ", '', tweet_render_text, flags=re.MULTILINE)
        tweet_render_text=tweet_render_text.replace("…","")
        #tweet_render_text=re.sub(r'\.\.\.', '', tweet_render_text, flags=re.MULTILINE)
        tweet_render_text=tweet_render_text[0:min(110,len(tweet_render_text))]

        if tweet_render_text in tweets_dict.keys():
            tweet = Opinion.objects.filter(stock=line, twitter_id=tweet_render.get('twitter_id'))[0]
            tweet.similarId = tweets_dict[tweet_render_text]
            tweet.save()
        else:
            tweets_dict[tweet_render_text] = tweet_render.get('twitter_id')
        x=x+1

##print("Labeling Dublicates")
##duplicate_tweetes = Opinion.objects.exclude(similarId='');
##for tweet in duplicate_tweetes:
##    parent_tweet =  Opinion.objects.filter(twitter_id = tweet.similarId).values()[0]
##    if parent_tweet['labeled'] == 1:
##        tweet.voted_relevancy = parent_tweet['voted_relevancy']
##        tweet.voted_sentiment = parent_tweet['voted_sentiment']
##        tweet.labeled = True
##        tweet.save()
##
