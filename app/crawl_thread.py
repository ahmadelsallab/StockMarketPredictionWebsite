from datetime import datetime
from app.models import Opinion
from django.utils import timezone
from Filter.Filter import Filter
import threading, time
import datetime
import os

import django
django.setup()



stock_list=[
'ﺕﺎﺴﻳ',
'ﺎﻟﺮﻳﺎﺿ',
'ﺎﻠﺟﺰﻳﺭﺓ',
'ﺎﺴﺘﺜﻣﺍﺭ',
'ﺎﻠﺴﻋﻭﺪﻳ ﺎﻠﻫﻮﻠﻧﺪﻳ',
'ﺎﻠﺴﻋﻭﺪﻳ ﺎﻠﻓﺮﻨﺴﻳ',
'ﺱﺎﺑ',
'ﺎﻠﻋﺮﺒﻳ ﺎﻟﻮﻄﻨﻳ',
#'ﺱﺎﻤﺑﺍ',
'ﺎﻟﺭﺎﺠﺤﻳ',
'ﺎﻠﺑﻻﺩ',
'ﺍﻺﻨﻣﺍﺀ',
'ﻚﻴﻣﺎﻧﻮﻟ',
'ﺐﺗﺭﻮﻜﻴﻣ',
'ﺱﺎﺒﻛ',
#'ﺱﺎﻔﻛﻭ',
'ﺎﻠﺘﺼﻨﻴﻋ',
'ﺎﻠﻠﺠﻴﻧ',
'ﻦﻣﺍﺀ ﻞﻠﻜﻴﻣﺍﻮﻳﺎﺗ',
'ﺎﻠﻤﺠﻣﻮﻋﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﺎﻠﺼﺣﺭﺍﺀ ﻞﻠﺒﺗﺭﻮﻜﻴﻣﺍﻮﻳﺎﺗ',
#'ﻲﻨﺳﺎﺑ',
'ﺲﺒﻜﻴﻣ ﺎﻠﻋﺎﻠﻤﻳﺓ',
'ﺎﻠﻤﺘﻗﺪﻣﺓ',
'ﻚﻳﺎﻧ',
#'ﺐﺗﺭﻭ ﺭﺎﺒﻏ',
'ﺄﺴﻤﻨﺗ ﺡﺎﺌﻟ',
'ﺄﺴﻤﻨﺗ ﻦﺟﺭﺎﻧ',
'ﺎﺴﻤﻨﺗ ﺎﻠﻣﺪﻴﻧﺓ',
'ﺎﺴﻤﻨﺗ ﺎﻠﺸﻣﺎﻠﻳﺓ',
'ﺍﻼﺴﻤﻨﺗ ﺎﻠﻋﺮﺒﻳﺓ',
'ﺎﺴﻤﻨﺗ ﺎﻠﻴﻣﺎﻣﺓ',
'ﺎﺴﻤﻨﺗ ﺎﻠﺴﻋﻭﺪﻴﻫ',
'ﺎﺴﻤﻨﺗ ﺎﻠﻘﺼﻴﻣ',
'ﺎﺴﻤﻨﺗ ﺎﻠﺠﻧﻮﺒﻴﻫ',
'ﺎﺴﻤﻨﺗ ﻲﻨﺒﻋ',
'ﺎﺴﻤﻨﺗ ﺎﻠﺷﺮﻘﻳﺓ',
'ﺎﺴﻤﻨﺗ ﺖﺑﻮﻛ',
'ﺎﺴﻤﻨﺗ ﺎﻠﺟﻮﻓ',
'ﺄﺳﻭﺎﻗ ﻉ ﺎﻠﻌﺜﻴﻣ',
'ﺎﻠﻣﻭﺎﺳﺍﺓ',
'ﺈﻜﺴﺗﺭﺍ',
'ﺪﻠﻫ ﺎﻠﺼﺤﻳﺓ',
'ﺮﻋﺎﻳﺓ',
'ﺱﺎﺴﻛﻭ',
'ﺚﻣﺍﺭ',
'ﻢﺠﻣﻮﻋﺓ ﻒﺘﻴﺤﻳ',
'ﺝﺮﻳﺭ',
'ﺎﻟﺩﺮﻴﺳ',
'ﺎﻠﺤﻜﻳﺭ',
'ﺎﻠﺨﻠﻴﺟ ﻞﻠﺗﺩﺮﻴﺑ',
'ﺎﻠﻏﺍﺯ ﻭﺎﻠﺘﺼﻨﻴﻋ',
'ﻚﻫﺮﺑﺍﺀ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﻢﺠﻣﻮﻋﺓ ﺹﺎﻓﻭﻻ',
'ﺎﻠﻏﺫﺎﺌﻳﺓ',
#'ﺱﺩﺎﻔﻛﻭ',
'ﺎﻠﻣﺭﺎﻌﻳ',
'ﺄﻨﻋﺎﻣ ﺎﻠﻗﺎﺒﺿﺓ',
'ﺢﻟﻭﺎﻨﻳ ﺈﺧﻭﺎﻧ',
'ﻩﺮﻔﻳ ﻝﻸﻏﺬﻳﺓ',
'ﺎﻠﺘﻣﻮﻴﻧ',
'ﻥﺍﺪﻛ',
'ﺎﻠﻘﺼﻴﻣ ﺎﻟﺯﺭﺎﻌﻴﻫ',
'ﺖﺑﻮﻛ ﺎﻟﺯﺭﺎﻌﻴﻫ',
'ﺍﻸﺴﻣﺎﻛ',
'ﺎﻠﺷﺮﻘﻳﺓ ﻞﻠﺘﻨﻤﻳﺓ',
'ﺎﻠﺟﻮﻓ ﺎﻟﺯﺭﺎﻌﻴﻫ',
'ﺐﻴﺷﺓ ﺎﻟﺯﺭﺎﻌﻴﻫ',
'ﺝﺍﺯﺎﻧ ﻞﻠﺘﻨﻤﻳﺓ',
'ﺍﻼﺘﺻﺍﻼﺗ',
'ﺎﺘﺣﺍﺩ ﺎﺘﺻﺍﻼﺗ',
'ﺰﻴﻧ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﻉﺬﻴﺑ ﻝﻼﺘﺻﺍﻼﺗ',
'ﺎﻠﻤﺘﻛﺎﻤﻟﺓ',
'ﺎﻠﺘﻋﺍﻮﻨﻳﺓ',
'ﻡﻻﺫ ﻞﻠﺗﺄﻤﻴﻧ',
##'ﻢﻳﺪﻐﻠﻓ ﻞﻠﺗﺄﻤﻴﻧ',
'ﺄﻠﻳﺎﻧﺯ ﺈﺳ ﺈﻓ',
'ﺱﻼﻣﺓ',
'ﻭﻻﺀ ﻞﻠﺗﺄﻤﻴﻧ',
'ﺎﻟﺩﺮﻋ ﺎﻠﻋﺮﺒﻳ',
'ﺱﺎﺑ ﺖﻛﺎﻔﻟ',
'ﺲﻧﺩ',
'ﺱﺎﻴﻛﻭ',
'ﻮﻓﺍ ﻞﻠﺗﺄﻤﻴﻧ',
'ﺈﺘﺣﺍﺩ ﺎﻠﺨﻠﻴﺟ',
'ﺍﻸﻬﻠﻳ ﻞﻠﺘﻛﺎﻔﻟ',
'ﺍﻸﻬﻠﻳﺓ',
'ﺄﺴﻴﺟ',
'ﺎﻠﺗﺄﻤﻴﻧ ﺎﻠﻋﺮﺒﻳﺓ',
'ﺍﻼﺘﺣﺍﺩ ﺎﻠﺘﺟﺍﺮﻳ',
'ﺎﻠﺼﻗﺭ ﻞﻠﺗﺄﻤﻴﻧ',
'ﺎﻠﻤﺘﺣﺩﺓ ﻞﻠﺗﺄﻤﻴﻧ',
'ﺍﻺﻋﺍﺩﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﺏﻮﺑﺍ ﺎﻠﻋﺮﺒﻳﺓ',
'ﻮﻗﺎﻳﺓ ﻞﻠﺘﻛﺎﻔﻟ',
'ﺖﻛﺎﻔﻟ ﺎﻟﺭﺎﺠﺤﻳ',
'ﺎﻴﺳ',
##'ﺎﻜﺳﺍ- ﺎﻠﺘﻋﺍﻮﻨﻳﺓ',
'ﺎﻠﺨﻠﻴﺠﻳﺓ ﺎﻠﻋﺎﻣﺓ',
'ﺏﺭﻮﺟ ﻞﻠﺗﺄﻤﻴﻧ',
'ﺎﻠﻋﺎﻠﻤﻳﺓ',
'ﺱﻮﻠﻳﺩﺮﺘﻳ ﺖﻛﺎﻔﻟ',
'ﺎﻟﻮﻄﻨﻳﺓ',
'ﺄﻣﺎﻧﺓ ﻞﻠﺗﺄﻤﻴﻧ',
'ﻊﻧﺎﻳﺓ',
'ﺍﻺﻨﻣﺍﺀ ﻁﻮﻜﻳﻭ ﻡ',
'ﺎﻠﻤﺻﺎﻔﻳ',
'ﺎﻠﻤﺘﻃﻭﺭﺓ',
'ﺍﻼﺤﺳﺍﺀ ﻞﻠﺘﻨﻤﻴﻫ',
##'ﺲﻴﺴﻛﻭ',
'ﻊﺴﻳﺭ',
'ﺎﻠﺑﺎﺣﺓ',
'ﺎﻠﻤﻤﻠﻛﺓ',
'ﺖﻛﻮﻴﻧ',
'ﺏﻯ ﺱﻯ ﺁﻯ',
'ﻢﻋﺍﺪﻧ',
'ﺄﺴﺗﺭﺍ ﺎﻠﺼﻧﺎﻌﻳﺓ',
'ﻢﺠﻣﻮﻋﺓ ﺎﻠﺳﺮﻴﻋ',
'ﺵﺎﻛﺭ',
'ﺎﻟﺩﻭﺎﺌﻳﺓ',
'ﺰﺟﺎﺟ',
'ﻒﻴﺒﻛﻭ',
'ﻢﻋﺪﻨﻳﺓ',
'ﺎﻠﻜﻴﻤﻳﺎﺌﻴﻫ ﺎﻠﺴﻋﻭﺪﻴﻫ',
'ﺺﻧﺎﻋﺓ ﺎﻟﻭﺮﻗ',
'ﺎﻠﻌﺑﺩﺎﻠﻠﻄﻴﻓ',
'ﺎﻠﺻﺍﺩﺭﺎﺗ',
'ﺄﺳﻼﻛ',
'ﻢﺠﻣﻮﻋﺓ ﺎﻠﻤﻌﺠﻟ',
'ﺍﻸﻧﺎﺒﻴﺑ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﺎﻠﺨﺿﺮﻳ',
'ﺎﻠﺧﺰﻓ',
'ﺎﻠﺠﺒﺳ',
'ﺎﻠﻛﺎﺑﻼﺗ',
'ﺹﺪﻗ',
'ﺎﻤﻳﺎﻨﺘﻴﺗ',
'ﺄﻧﺎﺒﻴﺑ',
'ﺎﻟﺯﺎﻤﻟ ﻞﻠﺼﻧﺎﻋﺓ',
'ﺎﻠﺑﺎﺒﻄﻴﻧ',
'ﺎﻠﻔﺧﺍﺮﻳﺓ',
'ﻢﺴﻛ',
'ﺎﻠﺒﺣﺭ ﺍﻸﺤﻣﺭ',
'ﺎﻠﻌﻗﺍﺮﻳﺓ',
'ﻂﻴﺑﺓ ﻝﻼﺴﺘﺜﻣﺍﺭ',
'ﻢﻛﺓ ﻝﻼﻨﺷﺍﺀ',
'ﺎﻠﺘﻌﻤﻳﺭ',
'ﺈﻌﻣﺍﺭ',
'ﺞﺒﻟ ﻊﻣﺭ',
'ﺩﺍﺭ ﺍﻷﺮﻛﺎﻧ',
'ﻡﺪﻴﻧﺓ ﺎﻠﻤﻋﺮﻓﺓ',
'ﺎﻠﺒﺣﺮﻳ',
'ﺎﻠﻨﻘﻟ ﺎﻠﺠﻣﺎﻌﻳ',
'ﻢﺑﺭﺩ',
'ﺏﺪﺠﺗ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﺖﻫﺎﻤﻫ ﻝﻼﻋﻼﻧ',
'ﺍﻸﺒﺣﺎﺛ ﻭ ﺎﻠﺘﺳﻮﻴﻗ',
'ﻂﺑﺎﻋﺓ ﻮﺘﻐﻠﻴﻓ',
'ﺎﻠﻄﻳﺍﺭ',
'ﺎﻠﺤﻜﻳﺭ',
'دور',
'ﺶﻤﺳ',
'البنك الأهلي',
'الصناعات الكهربائيه',
'بوان',
'ﺎﺴﻤﻨﺗ ﺎﻣ ﺎﻠﻗﺭﻯ',
'ﺄﺳﻭﺎﻗ ﺎﻠﻣﺯﺮﻋﺓ',
'ﺎﻠﺤﻣﺍﺪﻳ',
'ﺝﺰﻳﺭﺓ ﺖﻛﺎﻔﻟ',
'ﺎﻠﻋﺮﺒﻳ ﻞﻠﺗﺄﻤﻴﻧ',
'ﻢﺠﻣﻮﻋﺓ ﺎﻠﺤﻜﻳﺭ',
'ميبكو',
'ساكو',
'مبكو',
'الخدمات الأرضية',
];


synonyms = {
'ﺕﺎﺴﻳ': '(ﺕﺎﺴﻳ OR ﺕﺎﺳﻯ)',
'ﺎﻟﺮﻳﺎﺿ': '(ﺐﻨﻛ+ﺎﻟﺮﻳﺎﺿ OR ﻢﺻﺮﻓ+ﺎﻟﺮﻳﺎﺿ)',
'ﺎﻠﺟﺰﻳﺭﺓ': '(ﺐﻨﻛ+ﺎﻠﺟﺰﻳﺮﻫ OR ﺐﻨﻛ+ﺎﻠﺟﺰﻳﺭﺓ OR ﻢﺻﺮﻓ+ﺎﻠﺟﺰﻳﺭﺓ OR ﻢﺻﺮﻓ+ﺎﻠﺟﺰﻳﺮﻫ OR ﻢﺻﺮﻓ+ﺎﻠﺟﺰﻳﺮﻫ OR ﻢﺻﺮﻓ+ﺎﻠﺟﺰﻳﺭ OR ﺐﻨﻛ+ﺎﻠﺟﺰﻳﺭ)',
'ﺎﺴﺘﺜﻣﺍﺭ': '(ﺐﻨﻛ+ﺍﻼﺴﺘﺜﻣﺍﺭ OR ﻢﺻﺮﻓ+ﺍﻼﺴﺘﺜﻣﺍﺭ OR ﺐﻨﻛ+ﺍﻸﺴﺘﺜﻣﺍﺭ OR ﻢﺻﺮﻓ+ﺍﻸﺴﺘﺜﻣﺍﺭ)',
'ﺎﻠﺴﻋﻭﺪﻳ ﺎﻠﻫﻮﻠﻧﺪﻳ': '(ﺎﻠﺒﻨﻛ+ﺎﻠﻫﻮﻠﻧﺪﻳ OR ﺎﻠﺒﻨﻛ+ﺎﻠﻫﻮﻠﻧﺩﻯ OR ﻢﺻﺮﻓ+ﺎﻠﻫﻮﻠﻧﺪﻳ OR ﻢﺻﺮﻓ+ﺎﻠﻫﻮﻠﻧﺩﻯ OR ﺎﻠﺴﻋﻭﺪﻳ+ﺎﻠﻫﻮﻠﻧﺪﻳ OR ﺎﻠﺴﻋﻭﺩﻯ+ﺎﻠﻫﻮﻠﻧﺩﻯ OR ﺎﻠﺴﻋﻭﺩﻯ+ﺎﻠﻫﻮﻠﻧﺪﻳ OR ﺎﻠﺴﻋﻭﺪﻳ+ﺎﻠﻫﻮﻠﻧﺩﻯ)',
'ﺎﻠﺴﻋﻭﺪﻳ ﺎﻠﻓﺮﻨﺴﻳ': '(ﺎﻠﺒﻨﻛ+ﺎﻠﻓﺮﻨﺴﻳ OR ﺎﻠﺒﻨﻛ+ﺎﻠﻓﺮﻨﺳﻯ OR ﻢﺻﺮﻓ+ﺎﻠﻓﺮﻨﺴﻳ OR ﻢﺻﺮﻓ+ﺎﻠﻓﺮﻨﺳﻯ OR ﺎﻠﺴﻋﻭﺪﻳ+ﺎﻠﻓﺮﻨﺴﻳ OR ﺎﻠﺴﻋﻭﺩﻯ+ﺎﻠﻓﺮﻨﺳﻯ OR ﺎﻠﺴﻋﻭﺩﻯ+ﺎﻠﻓﺮﻨﺴﻳ OR ﺎﻠﺴﻋﻭﺪﻳ+ﺎﻠﻓﺮﻨﺳﻯ)',
'ﺱﺎﺑ': '(ﻢﺻﺮﻓ+ﺱﺎﺑ OR ﺐﻨﻛ+ﺱﺎﺑ OR ﺕﺎﺴﻳ+ﺱﺎﺑ)',
'ﺎﻠﻋﺮﺒﻳ ﺎﻟﻮﻄﻨﻳ': '(ﺎﻠﺒﻨﻛ+ﺎﻟﻮﻄﻨﻳ+ﺎﻠﻋﺮﺒﻳ OR ﺎﻠﺒﻨﻛ+ﺎﻟﻮﻄﻧﻯ+ﺎﻠﻋﺮﺑﻯ OR ﺐﻨﻛ+ﺎﻠﻋﺮﺒﻳ+ﺎﻟﻮﻄﻨﻳ OR ﺐﻨﻛ+ﺎﻠﻋﺮﺑﻯ+ﺎﻟﻮﻄﻧﻯ OR ﻢﺻﺮﻓ+ﺎﻠﻋﺮﺒﻳ+ﺎﻟﻮﻄﻨﻳ OR ﻢﺻﺮﻓ+ﺎﻠﻋﺮﺑﻯ+ﺎﻟﻮﻄﻧﻯ)',
'ﺱﺎﻤﺑﺍ': '(ﺱﺎﻤﺑﺍ)',
'ﺎﻟﺭﺎﺠﺤﻳ': '(ﺐﻨﻛ+ﺎﻠﺟﺍﺮﺤﻳ OR ﺐﻨﻛ+ﺎﻠﺟﺍﺮﺤﻳ OR ﻢﺻﺮﻓ+ﺎﻠﺟﺍﺮﺤﻳ OR ﻢﺻﺮﻓ+ﺎﻠﺟﺍﺮﺤﻳ)',
'ﺎﻠﺑﻻﺩ': '(ﺐﻨﻛ+ﺎﻠﺑﻻﺩ OR ﻢﺻﺮﻓ+ﺎﻠﺑﻻﺩ)',
'ﺍﻺﻨﻣﺍﺀ': '(ﺐﻨﻛ+ﺍﻼﻨﻣﺍﺀ OR ﻢﺻﺮﻓ+ﺍﻼﻨﻣﺍﺀ OR ﺐﻨﻛ+ﺍﻺﻨﻣﺍﺀ OR ﻢﺻﺮﻓ+ﺍﻸﻨﻣﺍﺀ OR ﺐﻨﻛ+ﺍﻸﻨﻣﺍﺀ OR ﻢﺻﺮﻓ+ﺍﻺﻨﻣﺍﺀ OR ﺍﻼﻨﻣﺍﺀ+ﺕﺎﺴﻳ OR ﺍﻺﻨﻣﺍﺀ+ﺕﺎﺴﻳ)',
'ﻚﻴﻣﺎﻧﻮﻟ': '(ﻚﻴﻣﺎﻧﻮﻟ OR ﻚﻣﺎﻧﻮﻟ)',
'ﺐﺗﺭﻮﻜﻴﻣ': '(ﺐﺗﺭﻮﻜﻴﻣ OR ﺐﻴﺗﺭﻮﻜﻴﻣ)',
'ﺱﺎﺒﻛ': '(ﺱﺎﺒﻛ)',
'ﺱﺎﻔﻛﻭ': '(ﺱﺎﻔﻛﻭ)',
'ﺎﻠﺘﺼﻨﻴﻋ': '(ﺎﻠﺘﺼﻨﻴﻋ OR ﺵﺮﻛﺓ+ﺖﺼﻨﻴﻋ OR ﺵﺮﻜﻫ+ﺖﺼﻨﻴﻋ)',
'ﺎﻠﻠﺠﻴﻧ': '(ﺎﻠﻠﺠﻴﻧ)',
'ﻦﻣﺍﺀ ﻞﻠﻜﻴﻣﺍﻮﻳﺎﺗ': '(ﻦﻣﺍﺀ+ﻞﻠﻜﻴﻣﺍﻮﻳﺎﺗ OR ﻦﻣﺍﺀ+ﺎﻠﻜﻴﻣﺍﻮﻳﺎﺗ OR ﻦﻣﺍﺀ)',
'ﺎﻠﻤﺠﻣﻮﻋﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ': '(ﺎﻠﻤﺠﻣﻮﻋﺓ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺎﻠﻤﺠﻣﻮﻋﺓ+ﺎﻠﺴﻋﻭﺪﻴﻫ OR ﺎﻠﻤﺠﻣﻮﻌﻫ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺎﻠﻤﺠﻣﻮﻌﻫ+ﺎﻠﺴﻋﻭﺪﻴﻫ)',
'ﺎﻠﺼﺣﺭﺍﺀ ﻞﻠﺒﺗﺭﻮﻜﻴﻣﺍﻮﻳﺎﺗ': '(ﺎﻠﺼﺣﺭﺍﺀ+ﻞﻠﺒﺗﺭﻮﻜﻴﻣﺍﻮﻳﺎﺗ OR ﺎﻠﺼﺣﺭﺍﺀ+ﺐﺗﺭﻮﻜﻴﻣﺍﻮﻳﺎﺗ OR ﺎﻠﺼﺣﺭﺍ+ﻞﻠﺒﺗﺭﻮﻜﻴﻣﺍﻮﻳﺎﺗ OR ﺎﻠﺼﺣﺭﺍ+ﺐﺗﺭﻮﻜﻴﻣﺍﻮﻳﺎﺗ OR ﺎﻠﺼﺣﺭﺍﺀ)',
'ﻲﻨﺳﺎﺑ': '(ﻲﻨﺳﺎﺑ)',
'ﺲﺒﻜﻴﻣ ﺎﻠﻋﺎﻠﻤﻳﺓ': '(ﺲﺒﻜﻴﻣ)',
'ﺎﻠﻤﺘﻗﺪﻣﺓ': '(ﺎﻠﻤﺘﻗﺪﻣﺓ OR ﺎﻠﻤﺘﻗﺪﻤﻫ)',
'ﻚﻳﺎﻧ': '(ﻚﻳﺎﻧ)',
'ﺐﺗﺭﻭ ﺭﺎﺒﻏ': '(ﺐﺗﺭﻭ+ﺭﺎﺒﻏ OR ﺐﻴﺗﺭﻭ+ﺭﺎﺒﻏ OR ﺐﺗﺭﻭﺭﺎﺒﻏ OR ﺐﻴﺗﺭﻭﺭﺎﺒﻏ)',
'ﺄﺴﻤﻨﺗ ﺡﺎﺌﻟ': '(ﺄﺴﻤﻨﺗ+ﺡﺎﺌﻟ OR ﺎﺴﻤﻨﺘﺣﺎﺌﻟ OR ﺲﻤﻨﺗ+ﺡﺎﺌﻟ OR ﺱ+ﺡﺎﺌﻟ)',
'ﺄﺴﻤﻨﺗ ﻦﺟﺭﺎﻧ': '(ﺄﺴﻤﻨﺗ+ﻦﺟﺭﺎﻧ OR ﺎﺴﻤﻨﺗ+ﻦﺟﺭﺎﻧ OR ﺲﻤﻨﺗ+ﻦﺟﺭﺎﻧ OR ﺱ+ﻦﺟﺭﺎﻧ)',
'ﺎﺴﻤﻨﺗ ﺎﻠﻣﺪﻴﻧﺓ': '(ﺎﺴﻤﻨﺗ+ﺎﻠﻣﺪﻴﻨﻫ OR ﺎﺴﻤﻨﺗ+ﺎﻠﻣﺪﻴﻧﺓ OR ﺄﺴﻤﻨﺗ+ﺎﻠﻣﺪﻴﻨﻫ OR ﺄﺴﻤﻨﺗ+ﺎﻠﻣﺪﻴﻧﺓ OR ﺲﻤﻨﺗ+ﺎﻠﻣﺪﻴﻨﻫ OR ﺲﻤﻤﻨﺗ+ﺎﻠﻣﺪﻴﻧﺓ OR ﺱ+ﺎﻠﻣﺪﻴﻨﻫ OR ﺱ+ﺎﻠﻣﺪﻴﻧﺓ)',
'ﺎﺴﻤﻨﺗ ﺎﻠﺸﻣﺎﻠﻳﺓ': '(ﺎﺴﻤﻨﺗ+ﺎﻠﺸﻣﺎﻠﻳﺓ OR ﺎﺴﻤﻨﺗ+ﺎﻠﺸﻣﺎﻠﻴﻫ OR ﺄﺴﻤﻨﺗ+ﺎﻠﺸﻣﺎﻠﻳﺓ OR ﺄﺴﻤﻨﺗ+ﺎﻠﺸﻣﺎﻠﻴﻫ OR ﺲﻤﻨﺗ+ﺎﻠﺸﻣﺎﻠﻴﻫ OR ﺲﻤﻨﺗ+ﺎﻠﺸﻣﺎﻠﻳﺓ OR ﺱ+ﺎﻠﺸﻣﺎﻠﻴﻫ OR ﺱ+ﺎﻠﺸﻣﺎﻠﻳﺓ)',
'ﺍﻼﺴﻤﻨﺗ ﺎﻠﻋﺮﺒﻳﺓ': '(ﺍﻼﺴﻤﻨﺗ+ﺎﻠﻋﺮﺒﻳﺓ OR ﺍﻸﺴﻤﻨﺗ+ﺎﻠﻋﺮﺒﻳﺓ OR ﺎﺴﻤﻨﺗ+ﺎﻠﻋﺮﺒﻳﺓ OR ﺄﺴﻤﻨﺗ+ﺎﻠﻋﺮﺒﻳﺓ OR ﺍﻼﺴﻤﻨﺗ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺍﻸﺴﻤﻨﺗ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺎﺴﻤﻨﺗ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺄﺴﻤﻨﺗ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺲﻤﻨﺗ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺲﻤﻨﺗ+ﺎﻠﻋﺮﺒﻳﺓ OR ﺱ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺱ+ﺎﻠﻋﺮﺒﻳﺓ)',
'ﺎﺴﻤﻨﺗ ﺎﻠﻴﻣﺎﻣﺓ': '(ﺎﺴﻤﻨﺗ+ﺎﻠﻴﻣﺎﻣﺓ OR ﺎﺴﻤﻨﺗ+ﺎﻠﻴﻣﺎﻤﻫ OR ﺄﺴﻤﻨﺗ+ﺎﻠﻴﻣﺎﻣﺓ OR ﺄﺴﻤﻨﺗ+ﺎﻠﻴﻣﺎﻤﻫ OR ﺲﻤﻨﺗ+ﺎﻠﻴﻣﺎﻤﻫ OR ﺲﻤﻨﺗ+ﺎﻠﻴﻣﺎﻣﺓ OR ﺲﻤﻨﺗ+ﺎﻠﻴﻣﺎﻤﻫ OR ﺱ+ﺎﻠﻴﻣﺎﻤﻫ OR ﺱ+ﺎﻠﻴﻣﺎﻣﺓ)',
'ﺎﺴﻤﻨﺗ ﺎﻠﺴﻋﻭﺪﻴﻫ': '(ﺎﺴﻤﻨﺗ+ﺎﻠﺴﻋﻭﺪﻴﻫ OR ﺄﺴﻤﻨﺗ+ﺎﻠﺴﻋﻭﺪﻴﻫ OR ﺎﺴﻤﻨﺗ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺄﺴﻤﻨﺗ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺲﻤﻨﺗ+ﺎﻠﺴﻋﻭﺪﻴﻫ OR ﺲﻤﻨﺗ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺱ+ﺎﻠﺴﻋﻭﺪﻴﻫ OR ﺱ+ﺎﻠﺴﻋﻭﺪﻳﺓ)',
'ﺎﺴﻤﻨﺗ ﺎﻠﻘﺼﻴﻣ': '(ﺎﺴﻤﻨﺗ+ﺎﻠﻘﺼﻴﻣ OR ﺄﺴﻤﻨﺗ+ﺎﻠﻘﺼﻴﻣ OR ﺲﻤﻨﺗ+ﺎﻠﻘﺼﻴﻣ OR ﺎﺴﻤﻨﺗ+ﺎﻠﻘﺼﻴﻣ OR ﺱ+ﺎﻠﻘﺼﻴﻣ)',
'ﺎﺴﻤﻨﺗ ﺎﻠﺠﻧﻮﺒﻴﻫ': '(ﺎﺴﻤﻨﺗ+ﺎﻠﺠﻧﻮﺒﻴﻫ OR ﺎﺴﻤﻨﺗ+ﺎﻠﺠﻧﻮﺒﻳﺓ OR ﺄﺴﻤﻨﺗ+ﺎﻠﺠﻧﻮﺒﻴﻫ OR ﺄﺴﻤﻨﺗ+ﺎﻠﺠﻧﻮﺒﻳﺓ OR ﺲﻤﻨﺗ+ﺎﻠﺠﻧﻮﺒﻴﻫ OR ﺲﻤﻨﺗ+ﺎﻠﺠﻧﻮﺒﻳﺓ OR ﺱ+ﺎﻠﺠﻧﻮﺒﻳﺓ OR ﺱ+ﺎﻠﺠﻧﻮﺒﻴﻫ)',
'ﺎﺴﻤﻨﺗ ﻲﻨﺒﻋ': '(ﺎﺴﻤﻨﺗ+ﻲﻨﺒﻋ OR ﺄﺴﻤﻨﺗ+ﻲﻨﺒﻋ OR ﺲﻤﻨﺗ+ﻲﻨﺒﻋ OR ﺱ+ﻲﻨﺒﻋ)',
'ﺎﺴﻤﻨﺗ ﺎﻠﺷﺮﻘﻳﺓ': '(ﺎﺴﻤﻨﺗ+ﺎﻠﺷﺮﻘﻳﺓ OR ﺎﺴﻤﻨﺗ+ﺎﻠﺷﺮﻘﻴﻫ OR ﺄﺴﻤﻨﺗ+ﺎﻠﺷﺮﻘﻴﻫ OR ﺄﺴﻤﻨﺗ+ﺎﻠﺷﺮﻘﻳﺓ OR ﺲﻤﻨﺗ+ﺎﻠﺷﺮﻘﻴﻫ OR ﺲﻤﻨﺗ+ﺎﻠﺷﺮﻘﻳﺓ OR ﺱ+ﺎﻠﺷﺮﻘﻴﻫ OR ﺱ+ﺎﻠﺷﺮﻘﻴﻫ)',
'ﺎﺴﻤﻨﺗ ﺖﺑﻮﻛ': '(ﺄﺴﻤﻨﺗ+ﺖﺑﻮﻛ OR ﺎﺴﻤﻨﺗ+ﺖﺑﻮﻛ OR ﺲﻤﻨﺗ+ﺖﺑﻮﻛ OR ﺱ+ﺖﺑﻮﻛ)',
'ﺎﺴﻤﻨﺗ ﺎﻠﺟﻮﻓ': '(ﺎﺴﻤﻨﺗ+ﺎﻠﺟﻮﻓ OR ﺄﺴﻤﻨﺗ+ﺎﻠﺟﻮﻓ OR ﺲﻤﻨﺗ+ﺎﻠﺟﻮﻓ OR ﺱ+ﺎﻠﺟﻮﻓ)',
'ﺄﺳﻭﺎﻗ ﻉ ﺎﻠﻌﺜﻴﻣ': '(ﺎﺳﻭﺎﻗ+ﺎﻠﻌﺜﻴﻣ OR ﺄﺳﻭﺎﻗ+ﺎﻠﻌﺜﻴﻣ OR ﺱﻮﻗ+ﺎﻠﻌﺜﻴﻣ OR ﺵﺮﻜﻫ+ﺎﻠﻌﺜﻴﻣ)',
'ﺎﻠﻣﻭﺎﺳﺍﺓ': '(ﺎﻠﻣﻭﺎﺳﺍﺓ OR ﺎﻠﻣﻭﺎﺳﺎﻫ OR ﻡﻭﺎﺳﺎﻫ OR ﻡﻭﺎﺳﺍﺓ)',
'ﺈﻜﺴﺗﺭﺍ': '(ﺄﻜﺴﺗﺭﺍ OR ﺈﻜﺴﺗﺭﺍ OR ﺎﻜﺴﺗﺭﺍ)',
'ﺪﻠﻫ ﺎﻠﺼﺤﻳﺓ': '(ﺪﻠﻫ+ﺎﻠﺼﺤﻴﻫ OR ﺪﻠﻫ+ﺎﻠﺼﺤﻳﺓ OR ﺪﻟﺓ+ﺎﻠﺼﺤﻴﻫ OR ﺪﻟﺓ+ﺎﻠﺼﺤﻳﺓ OR تاسى+ﺪﻠﻫ OR تاسي+ﺪﻟﺓ OR ﻢﺠﻣﻮﻋﺓ+ﺪﻠﻫ OR ﻢﺠﻣﻮﻋﺓ+ﺪﻟﺓ)',
'ﺮﻋﺎﻳﺓ': '(ﺮﻋﺎﻴﻫ OR ﺮﻋﺎﻳﺓ)',
'ﺱﺎﺴﻛﻭ': '(ﺱﺎﺴﻛﻭ)',
'ﺚﻣﺍﺭ': '(ﺚﻣﺍﺭ)',
'ﻢﺠﻣﻮﻋﺓ ﻒﺘﻴﺤﻳ': '(ﻒﺘﻴﺣﻯ OR ﻒﺘﻴﺤﻳ)',
'ﺝﺮﻳﺭ': '(ﺝﺮﻳﺭ)',
'ﺎﻟﺩﺮﻴﺳ': '(ﺎﻟﺩﺮﻴﺳ)',
'ﺎﻠﺤﻜﻳﺭ': '(ﺎﻠﺤﻜﻳﺭ)',
'ﺎﻠﺨﻠﻴﺟ ﻞﻠﺗﺩﺮﻴﺑ': '(ﺎﻠﺨﻠﻴﺟ+ﻞﻠﺗﺩﺮﻴﺑ OR ﺎﻠﺨﻠﻴﺟ+ﺎﻠﺗﺩﺮﻴﺑ OR ﺎﻠﺨﻠﻴﺟ+ﺕﺩﺮﻴﺑ OR ﺦﻠﻴﺟ+ﻞﻠﺗﺩﺮﻴﺑ)',
'ﺎﻠﻏﺍﺯ ﻭﺎﻠﺘﺼﻨﻴﻋ': '(ﺎﻠﻏﺍﺯ+ﺎﻠﺘﺼﻨﻴﻋ OR ﺎﻠﻏﺍﺯ)',
'ﻚﻫﺮﺑﺍﺀ ﺎﻠﺴﻋﻭﺪﻳﺓ': '(ﻚﻫﺮﺑﺍﺀ+ﺎﻠﺴﻋﻭﺪﻴﻫ OR ﻚﻫﺮﺑﺍﺀ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺲﻬﻣ+ﺎﻠﻜﻫﺮﺑﺍﺀ)',
'ﻢﺠﻣﻮﻋﺓ ﺹﺎﻓﻭﻻ': '(ﺹﺎﻓﻭﻻ)',
'ﺎﻠﻏﺫﺎﺌﻳﺓ': '(ﺎﻠﻏﺫﺎﺌﻴﻫ OR ﺎﻠﻏﺫﺎﺌﻳﺓ OR ﻮﻓﺮﻫ OR ﻮﻓﺭﺓ)',
'ﺱﺩﺎﻔﻛﻭ': '(ﺱﺩﺎﻔﻛﻭ)',
'ﺎﻠﻣﺭﺎﻌﻳ': '(ﺎﻠﻣﺭﺎﻋﻯ OR ﺎﻠﻣﺭﺎﻌﻳ)',
'ﺄﻨﻋﺎﻣ ﺎﻠﻗﺎﺒﺿﺓ': '(ﺄﻨﻋﺎﻣ+ﺎﻠﻗﺎﺒﺿﺓ OR ﺎﻨﻋﺎﻣﺎﻠﻗﺎﺒﺿﺓ OR ﺄﻨﻋﺎﻣﺎﻠﻗﺎﺒﻀﻫ OR ﺎﻨﻋﺎﻣﺎﻠﻗﺎﺒﻀﻫ OR ﺎﻨﻋﺎﻣ+ﺕﺎﺴﻳ OR ﺄﻨﻋﺎﻣ+ﺕﺎﺴﻳ)',
'ﺢﻟﻭﺎﻨﻳ ﺈﺧﻭﺎﻧ': '(ﺢﻟﻭﺎﻨﻳ OR ﺎﺧﻭﺎﻧ OR ﺄﺧﻭﺎﻧ OR ﺈﺧﻭﺎﻧ OR ﺎﺧﻭﺎﻧ OR ﺢﻟﻭﺎﻧﻯ )',
'ﻩﺮﻔﻳ ﻝﻸﻏﺬﻳﺓ': '(ﻩﺮﻔﻳ OR ﻩﺮﻓﻯ)',
'ﺎﻠﺘﻣﻮﻴﻧ': '(ﺎﻠﺘﻣﻮﻴﻧ)',
'ﻥﺍﺪﻛ': '(ﻥﺍﺪﻛ)',
'ﺎﻠﻘﺼﻴﻣ ﺎﻟﺯﺭﺎﻌﻴﻫ': '(ﺎﻠﻘﺼﻴﻣ+ﺎﻟﺯﺭﺎﻌﻴﻫ OR ﺎﻠﻘﺼﻴﻣ+ﺎﻟﺯﺭﺎﻌﻳﺓ OR ﻖﺼﻴﻣ+ﺯ OR ﺎﻠﻘﺼﻴﻣ+ﺯ OR ﻖﺼﻴﻣ+ﺎﻟﺯﺭﺎﻌﻳﺓ OR ﻖﺼﻴﻣ+ﺎﻟﺯﺭﺎﻌﻴﻫ)',
'ﺖﺑﻮﻛ ﺎﻟﺯﺭﺎﻌﻴﻫ': '(ﺖﺑﻮﻛ+ﺎﻟﺯﺭﺎﻌﻴﻫ OR ﺖﺑﻮﻛ+ﺎﻟﺯﺭﺎﻌﻳﺓ OR ﺖﺑﻮﻛ+ﺯ)',
'ﺍﻸﺴﻣﺎﻛ': '(ﺍﻸﺴﻣﺎﻛ OR ﺍﻼﺴﻣﺎﻛ)',
'ﺎﻠﺷﺮﻘﻳﺓ ﻞﻠﺘﻨﻤﻳﺓ': '(ﺎﻠﺷﺮﻘﻳﺓ+ﻞﻠﺘﻨﻤﻳﺓ OR ﺎﻠﺷﺮﻘﻳﺓ+ﻞﻠﺘﻨﻤﻴﻫ OR ﺎﻠﺷﺮﻘﻴﻫ+ﻞﻠﺘﻨﻤﻳﺓ OR ﺎﻠﺷﺮﻘﻴﻫ+ﻞﻠﺘﻨﻤﻴﻫ OR ﺲﻬﻣ+ﺎﻠﺷﺮﻘﻴﻫ OR ﺲﻬﻣ+ﺎﻠﺷﺮﻘﻳﺓ OR ﺎﻠﺷﺮﻘﻴﻫ+ﺯ OR ﺎﻠﺷﺮﻘﻳﺓ+ﺯ)',
'ﺎﻠﺟﻮﻓ ﺎﻟﺯﺭﺎﻌﻴﻫ': '(ﺎﻠﺟﻮﻓ+ﺎﻟﺯﺭﺎﻌﻴﻫ OR ﺎﻠﺟﻮﻓ+ﺎﻟﺯﺭﺎﻌﻳﺓ OR ﺎﻠﺟﻮﻓ+ﺯ)',
'ﺐﻴﺷﺓ ﺎﻟﺯﺭﺎﻌﻴﻫ': '(ﺐﻴﺸﻫ+ﺎﻟﺯﺭﺎﻌﻴﻫ OR ﺐﻴﺷﺓ+ﺎﻟﺯﺭﺎﻌﻴﻫ OR ﺐﻴﺷﺓ+ﺎﻟﺯﺭﺎﻌﻳﺓ OR ﺐﻴﺸﻫ+ﺎﻟﺯﺭﺎﻌﻳﺓ OR ﺐﻴﺸﻫ+ﺎﻟﺯﺭﺎﻌﻴﻫ OR ﺐﻴﺸﻫ+ﺯ OR ﺐﻴﺷﺓ+ﺯ OR ﺲﻬﻣ+ﺐﻴﺸﻫ OR ﺲﻬﻣ+ﺐﻴﺷﺓ)',
'ﺝﺍﺯﺎﻧ ﻞﻠﺘﻨﻤﻳﺓ': '(ﺝﺍﺯﺎﻧ)',
'ﺍﻼﺘﺻﺍﻼﺗ': '(ﺍﻼﺘﺻﺍﻼﺗ OR ﺍﻸﺘﺻﺍﻼﺗ OR STC)',
'ﺎﺘﺣﺍﺩ ﺎﺘﺻﺍﻼﺗ': '(ﺎﺘﺣﺍﺩ+ﺎﺘﺻﺍﻼﺗ OR ﺈﺘﺣﺍﺩ+ﺎﺘﺻﺍﻼﺗ OR ﺎﺘﺣﺍﺩ+ﺄﺘﺻﺍﻼﺗ OR ﺈﺘﺣﺍﺩ+ﺄﺘﺻﺍﻼﺗ OR ﺄﺘﺣﺍﺩ+ﺎﺘﺻﺍﻼﺗ OR ﺄﺘﺣﺍﺩ+ﺎﺘﺻﺍﻼﺗ OR سهم+موبايلي OR  سهم+موبايلى)',
'ﺰﻴﻧ ﺎﻠﺴﻋﻭﺪﻳﺓ': '(ﺰﻴﻧ+ﺎﻠﺴﻋﻭﺪﻴﻫ OR ﺰﻴﻧ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺲﻬﻣ+ﺰﻴﻧ)',
'ﻉﺬﻴﺑ ﻝﻼﺘﺻﺍﻼﺗ': '(ﻉﺬﻴﺑ)',
'ﺎﻠﻤﺘﻛﺎﻤﻟﺓ': '(ﺎﻠﻤﺘﻛﺎﻤﻠﻫ OR ﺎﻠﻤﺘﻛﺎﻤﻟﺓ OR ﺎﻠﻤﺘﻛﺎﻤﻠﻫ)',
'ﺎﻠﺘﻋﺍﻮﻨﻳﺓ': '(ﺎﻠﺘﻋﺍﻮﻨﻴﻫ OR ﺎﻠﺘﻋﺍﻮﻨﻳﺓ OR ﺎﻠﺘﻋﺍﻮﻨﻴﻫ)',
'ﻡﻻﺫ ﻞﻠﺗﺄﻤﻴﻧ': '(ﻡﻻﺫ+ﻞﻠﺗﺄﻤﻴﻧ OR ﻡﻻﺫ+ﻞﻠﺗﺄﻤﻴﻧ OR ﻡﻻﺫ+ﺕﺎﺴﻳ OR ﺲﻬﻣ+ﻡﻻﺫ)',
'ﻢﻳﺪﻐﻠﻓ ﻞﻠﺗﺄﻤﻴﻧ': '( ﻢﻳﺪﻐﻠﻓ OR ﻢﻳﺪﻘﻠﻓ OR ﻢﻳﺩ+ﻎﻠﻓ OR ﻢﻳﺩ+ﻖﻠﻓ OR ميدغيلف OR مدغلف )',
'ﺄﻠﻳﺎﻧﺯ ﺈﺳ ﺈﻓ': '(ﺎﻠﻳﺎﻧﺯ+ﺎﺳ+ﺎﻓ OR ﺈﺳ+ﺈﻓ OR ﺎﻠﻳﺎﻧﺯ+ﺕﺎﺴﻳ OR ﺈﻠﻳﺎﻧﺯ+ﺕﺎﺴﻳ)',
'ﺱﻼﻣﺓ': '(ﺲﻬﻣ+ﺱﻼﻤﻫ OR ﺲﻬﻣ+ﺱﻼﻣﺓ OR ﺕﺎﺴﻳ+ﺱﻼﻤﻫ OR ﺕﺎﺴﻳ+ﺱﻼﻤﻫ OR ﺱﻼﻣﺓ+ ﻞﻠﺗﺄﻤﻴﻧ OR ﺱﻼﻤﻫ+ ﻞﻠﺗﺄﻤﻴﻧ)',
'ﻭﻻﺀ ﻞﻠﺗﺄﻤﻴﻧ': '(ﻭﻻﺀ+ﻞﻠﺗﺄﻤﻴﻧ OR ﻭﻻﺀ+ﻞﻠﺗﺎﻤﻴﻧ OR ﻭﻻﺀ+ﺕﺎﺴﻳ OR ﺲﻬﻣ+ﻭﻻﺀ)',
'ﺎﻟﺩﺮﻋ ﺎﻠﻋﺮﺒﻳ': '(ﺎﻟﺩﺮﻋ+ﺎﻠﻋﺮﺒﻳ OR ﺎﻟﺩﺮﻋ+ﺎﻠﻋﺮﺑﻯ OR ﺎﻟﺩﺮﻋ+ﺕﺎﺴﻳ OR ﺎﻟﺩﺮﻋ+ﺕﺎﻤﻴﻧ OR ﺎﻟﺩﺮﻋ+ﺲﻬﻣ)',
'ﺱﺎﺑ ﺖﻛﺎﻔﻟ': '(ﺱﺎﺑ+ﺖﻛﺎﻔﻟ OR ﺱﺎﺑ+ﺕﺎﺴﻳ OR ﺱﺎﺑ+ﺲﻬﻣ)',
'ﺲﻧﺩ': '(ﺲﻧﺩ+ﺲﻬﻣ OR ﺲﻧﺩ+ﺕﺎﻤﻴﻧ OR ﺲﻧﺩ+ﻞﻠﺗﺎﻤﻴﻧ OR ﺲﻧﺩ+ﺕﺎﺴﻳ OR ﺲﻧﺩ+ﺕﺎﺳﻯ)',
'ﺱﺎﻴﻛﻭ': '(ﺱﺎﻴﻛﻭ OR ﺱﺎﻴﻛﻭ+ﺕﺎﻤﻴﻧ OR ﺱﺎﻴﻛﻭ+ﻞﻠﺗﺎﻤﻴﻧ)',
'ﻮﻓﺍ ﻞﻠﺗﺄﻤﻴﻧ': '(ﻮﻓﺍ+ﻞﻠﺗﺄﻤﻴﻧ OR ﻮﻓﺍ+ﻞﻠﺗﺎﻤﻴﻧ OR ﻮﻓﺍﺀ+ﻞﻠﺗﺎﻤﻴﻧ OR ﻮﻓﺍﺀ+ﻞﻠﺗﺄﻤﻴﻧ OR ﻮﻓﺍﺀ+ﺲﻬﻣ OR ﻮﻓﺍﺀ+ﺕﺎﺴﻳ OR ﻮﻓﺍﺀ+ﺕﺎﺴﻳ)',
'ﺈﺘﺣﺍﺩ ﺎﻠﺨﻠﻴﺟ': '(ﺈﺘﺣﺍﺩ+ﺎﻠﺨﻠﻴﺟ OR ﺄﺘﺣﺍﺩ+ﺎﻠﺨﻠﻴﺟ OR ﺎﺘﺣﺍﺩ+ﺎﻠﺨﻠﻴﺟ)',
'ﺍﻸﻬﻠﻳ ﻞﻠﺘﻛﺎﻔﻟ': '(ﺍﻸﻬﻠﻳ+ﻞﻠﺘﻛﺎﻔﻟ OR ﺍﻼﻬﻠﻳ+ﻞﻠﺘﻛﺎﻔﻟ OR ﺍﻸﻬﻠﻳ+ﺖﻛﺎﻔﻟ OR ﺍﻼﻬﻠﻳ+ﺖﻛﺎﻔﻟ)',
'ﺍﻸﻬﻠﻳﺓ': '( ﺍﻸﻬﻠﻳﺓ OR ﺍﻼﻬﻠﻴﻫ )',
'ﺄﺴﻴﺟ': '(ﺄﺴﻴﺟ OR ﺎﺴﻴﺟ OR ﺈﺴﻴﺟ)',
'ﺎﻠﺗﺄﻤﻴﻧ ﺎﻠﻋﺮﺒﻳﺓ': '(ﺎﻠﺗﺄﻤﻴﻧ+ﺎﻠﻋﺮﺒﻳﺓ OR ﺎﻠﺗﺄﻤﻴﻧ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺎﻠﺗﺎﻤﻴﻧ+ﺎﻠﻋﺮﺒﻳﺓ OR ﺎﻠﺗﺎﻤﻴﻧ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺕ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺕ+ﺎﻠﻋﺮﺒﻳﺓ)',
'ﺍﻼﺘﺣﺍﺩ ﺎﻠﺘﺟﺍﺮﻳ': '(ﺍﻼﺘﺣﺍﺩ+ﺎﻠﺘﺟﺍﺮﻳ OR ﺍﻼﺘﺣﺍﺩ+ﺎﻠﺘﺟﺍﺭﻯ OR ﺍﻸﺘﺣﺍﺩ+ﺎﻠﺘﺟﺍﺭﻯ OR ﺍﻸﺘﺣﺍﺩ+ﺎﻠﺘﺟﺍﺮﻳ OR ﺍﻺﺘﺣﺍﺩ+ﺎﻠﺘﺟﺍﺭﻯ OR ﺍﻺﺘﺣﺍﺩ+ﺎﻠﺘﺟﺍﺮﻳ OR ﺍﻼﺘﺣﺍﺩ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺕ+ﺍﻼﺘﺣﺍﺩ OR ﺕ+ﺍﻸﺘﺣﺍﺩ)',
'ﺎﻠﺼﻗﺭ ﻞﻠﺗﺄﻤﻴﻧ': '(ﺎﻠﺼﻗﺭ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺎﻠﺼﻗﺭ+ﻞﻠﺗﺎﻤﻴﻧ OR ﺲﻬﻣ+ﺎﻠﺼﻗﺭ OR ﺎﻠﺼﻗﺭ+ﺕﺎﺴﻳ)',
'ﺎﻠﻤﺘﺣﺩﺓ ﻞﻠﺗﺄﻤﻴﻧ': '(ﺎﻠﻤﺘﺣﺩﺓ OR ﺎﻠﻤﺘﺣﺪﻫ )',
'ﺍﻺﻋﺍﺩﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ': '(ﺍﻺﻋﺍﺩﺓ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺍﻺﻋﺍﺪﻫ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺎﻋﺍﺪﻫ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺄﻋﺍﺪﻫ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺍﻼﻋﺍﺩﺓ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺍﻸﻋﺍﺩﺓ+ﻞﻠﺗﺄﻤﻴﻧ OR سهم+إعاده OR سهم+إعادة OR سهم+اعاده OR سهم+اعادة)',
'ﺏﻮﺑﺍ ﺎﻠﻋﺮﺒﻳﺓ': '(ﺏﻮﺑﺍ)',
'ﻮﻗﺎﻳﺓ ﻞﻠﺘﻛﺎﻔﻟ': '(ﻮﻗﺎﻳﺓ OR ﻮﻗﺎﻴﻫ )',
'ﺖﻛﺎﻔﻟ ﺎﻟﺭﺎﺠﺤﻳ': '(ﺖﻛﺎﻔﻟ+ﺎﻟﺭﺎﺠﺤﻳ OR ﺖﻛﺎﻔﻟ+ﺎﻟﺭﺎﺠﺣﻯ OR ﺕ+ﺎﻟﺭﺎﺠﺤﻳ OR ﺕ+ﺎﻟﺭﺎﺠﺣﻯ)',
'ﺎﻴﺳ': '(ﺎﻴﺳ OR ﺄﻴﺳ OR ﺄﻴﺳ+ﻞﻠﺗﺄﻤﻴﻧ  OR ﺎﻴﺳ+ﻞﻠﺗﺄﻤﻴﻧ )',
'ﺎﻜﺳﺍ- ﺎﻠﺘﻋﺍﻮﻨﻳﺓ': '(ﺎﻜﺳﺍ OR ﺈﻜﺳﺍ OR ﺄﻜﺳﺍ OR اكسا-+التعاونية OR اكسا-+التعاونيه )',
'ﺎﻠﺨﻠﻴﺠﻳﺓ ﺎﻠﻋﺎﻣﺓ': '(ﺎﻠﺨﻠﻴﺠﻳﺓ+ﺎﻠﻋﺎﻣﺓ OR ﺎﻠﺨﻠﻴﺠﻴﻫ+ﺎﻠﻋﺎﻤﻫ OR ﺎﻠﺨﻠﻴﺠﻳﺓ+ﺎﻠﻋﺎﻤﻫ OR ﺎﻠﺨﻠﻴﺠﻴﻫ+ﺎﻠﻋﺎﻣﺓ OR ﺲﻬﻣ+ﺎﻠﺨﻠﻴﺠﻴﻫ OR ﺕﺎﺴﻳ+ﺎﻠﺨﻠﻴﺠﻴﻫ OR ﺕﺎﺴﻳ+ﺎﻠﺨﻠﻴﺠﻳﺓ OR ﺕﺎﺳﻯ+ﺎﻠﺨﻠﻴﺠﻴﻫ OR ﺕﺎﺳﻯ+ﺎﻠﺨﻠﻴﺠﻳﺓ)',
'ﺏﺭﻮﺟ ﻞﻠﺗﺄﻤﻴﻧ': '(ﺏﺭﻮﺟ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺏﺭﻮﺟ+ﻞﻠﺗﺎﻤﻴﻧ OR ﺏﺭﻮﺟ)',
'ﺎﻠﻋﺎﻠﻤﻳﺓ': '(ﺎﻠﻋﺎﻠﻤﻳﺓ+سهم OR سهم+العالميه OR تاسي+العالميه OR ﺎﻠﻋﺎﻠﻤﻴﻫ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺎﻠﻋﺎﻠﻤﻳﺓ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺎﻠﻋﺎﻠﻤﻴﻫ+ﺎﻠﺘﻋﺍﻮﻨﻳ OR ﺎﻠﻋﺎﻠﻤﻳﺓ+ﺎﻠﺘﻋﺍﻮﻨﻳ)',
'ﺱﻮﻠﻳﺩﺮﺘﻳ ﺖﻛﺎﻔﻟ': '(ﺱﻮﻠﻳﺩﺮﺘﻳ OR ﺱﻮﻠﻳﺩﺮﺗﻯ OR ﺱﻮﻟﺩﺮﺘﻳ OR ﺱﻮﻟﺩﺮﺗﻯ)',
'ﺎﻟﻮﻄﻨﻳﺓ': '(ﺎﻟﻮﻄﻨﻳﺓ+سهم OR ﺎﻟﻮﻄﻨﻴﻫ+سهم OR الوطنيه+تاسي OR الوطنية+تاسى OR الوطنيه+تاسى OR الوطنية+تاسي OR ﺎﻟﻮﻄﻨﻳﺓ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺎﻟﻮﻄﻨﻴﻫ+ﻞﻠﺗﺄﻤﻴﻧ)',
'ﺄﻣﺎﻧﺓ ﻞﻠﺗﺄﻤﻴﻧ': '(ﺄﻣﺎﻧﺓ OR ﺎﻣﺎﻧﺓ OR ﺄﻣﺎﻨﻫ OR امانه )',
'ﻊﻧﺎﻳﺓ': '(ﻊﻧﺎﻴﻫ OR ﻊﻧﺎﻳﺓ OR ﻊﻧﺎﻴﻫ+ﻞﻠﺗﺎﻤﻴﻧ OR ﻊﻧﺎﻳﺓ+ﻞﻠﺗﺎﻤﻴﻧ OR ﻊﻧﺎﻴﻫ+ﻞﻠﺗﺄﻤﻴﻧ OR ﻊﻧﺎﻳﺓ+ﻞﻠﺗﺄﻤﻴﻧ)',
'ﺍﻺﻨﻣﺍﺀ ﻁﻮﻜﻳﻭ ﻡ': '(ﺍﻺﻨﻣﺍﺀ+ﻁﻮﻜﻳﻭ OR ﺍﻼﻨﻣﺍﺀ+ﻁﻮﻜﻳﻭ  OR ﻁﻮﻜﻳﻭ+سصهم OR  ﻁﻮﻜﻳﻭ+تاسي )',
'ﺎﻠﻤﺻﺎﻔﻳ': '(ﺎﻠﻤﺻﺎﻔﻳ OR ﺎﻠﻤﺻﺎﻓﻯ)',
'ﺎﻠﻤﺘﻃﻭﺭﺓ': '(ﺲﻬﻣ+ﺎﻠﻤﺘﻃﻭﺮﻫ OR ﺲﻬﻣ+ﺎﻠﻤﺘﻃﻭﺭﺓ OR ﺕﺎﺴﻳ+ﺎﻠﻤﺘﻃﻭﺮﻫ OR ﺕﺎﺳﻯ+ﺎﻠﻤﺘﻃﻭﺮﻫ OR ﺕﺎﺳﻯ+ﺎﻠﻤﺘﻃﻭﺭﺓ OR ﺕﺎﺴﻳ+ﺎﻠﻤﺘﻃﻭﺭﺓ)',
'ﺍﻼﺤﺳﺍﺀ ﻞﻠﺘﻨﻤﻴﻫ': '(ﺍﻼﺤﺳﺍﺀ+ﻞﻠﺘﻨﻤﻴﻫ OR ﺍﻸﺤﺳﺍﺀ+ﻞﻠﺘﻨﻤﻴﻫ OR ﺍﻼﺤﺳﺍﺀ+ﻞﻠﺘﻨﻤﻳﺓ OR ﺍﻸﺤﺳﺍﺀ+ﻞﻠﺘﻨﻤﻳﺓ OR ﺲﻬﻣ+ﺍﻸﺤﺳﺍﺀ OR ﺲﻬﻣ+ﺍﻼﺤﺳﺍﺀ OR ﺕﺎﺴﻳ+ﺍﻸﺤﺳﺍﺀ OR ﺕﺎﺴﻳ+ﺍﻼﺤﺳﺍﺀ OR ﺕﺎﺳﻯ+ﺍﻼﺤﺳﺍﺀ OR ﺕﺎﺳﻯ+ﺍﻸﺤﺳﺍﺀ)',
'ﺲﻴﺴﻛﻭ': 'ﺲﻴﺴﻛﻭ',
'ﻊﺴﻳﺭ': '(ﺲﻬﻣ+ﻊﺴﻳﺭ OR ﺕﺎﺴﻳ+ﻊﺴﻳﺭ OR ﺕﺎﺳﻯ+ﻊﺴﻳﺭ)',
'ﺎﻠﺑﺎﺣﺓ': '(ﺲﻬﻣ+ﺎﻠﺑﺎﺤﻫ OR ﺲﻬﻣ+ﺎﻠﺑﺎﺣﺓ OR ﺕﺎﺴﻳ+ﺎﻠﺑﺎﺤﻫ OR ﺕﺎﺳﻯ+ﺎﻠﺑﺎﺤﻫ OR ﺕﺎﺳﻯ+ﺎﻠﺑﺎﺣﺓ OR ﺕﺎﺴﻳ+ﺎﻠﺑﺎﺣﺓ)',
'ﺎﻠﻤﻤﻠﻛﺓ': '(ﺲﻬﻣ+ﺎﻠﻤﻤﻠﻜﻫ OR ﺲﻬﻣ+ﺎﻠﻤﻤﻠﻛﺓ OR ﺕﺎﺴﻳ+ﺎﻠﻤﻤﻠﻜﻫ OR ﺕﺎﺴﻳ+ﺎﻠﻤﻤﻠﻛﺓ OR ﺕﺎﺳﻯ+ﺎﻠﻤﻤﻠﻛﺓ OR ﺕﺎﺳﻯ+ﺎﻠﻤﻤﻠﻜﻫ)',
'ﺖﻛﻮﻴﻧ': '(ﺖﻛﻮﻴﻧ)',
'ﺏﻯ ﺱﻯ ﺁﻯ': '(ﺏﻯ+ﺱﻯ+ﺁﻯ OR ﺏﻯ+ﺱﻯ+ﺍﻯ OR ﺐﻳ+ﺲﻳ+ﺂﻳ OR ﺐﻳ+ﺲﻳ+ﺎﻳ)',
'ﻢﻋﺍﺪﻧ': '(ﻢﻋﺍﺪﻧ)',
'ﺄﺴﺗﺭﺍ ﺎﻠﺼﻧﺎﻌﻳﺓ': '(ﺄﺴﺗﺭﺍ OR ﺎﺴﺗﺭﺍ)',
'ﻢﺠﻣﻮﻋﺓ ﺎﻠﺳﺮﻴﻋ': '(ﻢﺠﻣﻮﻋﺓ+ﺎﻠﺳﺮﻴﻋ OR ﻢﺠﻣﻮﻌﻫ+ﺎﻠﺳﺮﻴﻋ)',
'ﺵﺎﻛﺭ': '(ﺲﻬﻣ+ﺵﺎﻛﺭ OR ﺕﺎﺴﻳ+ﺵﺎﻛﺭ OR ﺕﺎﺳﻯ+ﺵﺎﻛﺭ)',
'ﺎﻟﺩﻭﺎﺌﻳﺓ': '(ﺲﻬﻣ+ﺎﻟﺩﻭﺎﺌﻳﺓ OR ﺲﻬﻣ+ﺎﻟﺩﻭﺎﺌﻴﻫ)',
'ﺰﺟﺎﺟ': '(ﺰﺟﺎﺟ)',
'ﻒﻴﺒﻛﻭ': '(ﻒﻴﺒﻛﻭ OR ﻒﺒﻛﻭ)',
'ﻢﻋﺪﻨﻳﺓ': '(ﻢﻋﺪﻨﻳﺓ OR ﻢﻋﺪﻨﻴﻫ)',
'ﺎﻠﻜﻴﻤﻳﺎﺌﻴﻫ ﺎﻠﺴﻋﻭﺪﻴﻫ': '(ﺎﻠﻜﻴﻤﻳﺎﺌﻴﻫ+ﺎﻠﺴﻋﻭﺪﻴﻫ OR ﺎﻠﻜﻴﻤﻳﺎﺌﻳﺓ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺎﻠﻜﻴﻤﻳﺎﺌﻴﻫ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺎﻠﻜﻴﻤﻳﺎﺌﻳﺓ+ﺎﻠﺴﻋﻭﺪﻴﻫ OR ﺎﻠﻜﻴﻤﻳﺎﺌﻴﻫ OR ﺎﻠﻜﻴﻤﻳﺎﺌﻳﺓ)',
'ﺺﻧﺎﻋﺓ ﺎﻟﻭﺮﻗ': '(ﺺﻧﺎﻋﺓ+ﺎﻟﻭﺮﻗ OR ﺺﻧﺎﻌﻫ+ﺎﻟﻭﺮﻗ OR ﺲﻬﻣ+ﺎﻟﻭﺮﻗ OR ﺕﺎﺴﻳ+ﺎﻟﻭﺮﻗ OR ﺕﺎﺳﻯ+ﺎﻟﻭﺮﻗ)',
'ﺎﻠﻌﺑﺩﺎﻠﻠﻄﻴﻓ': '(ﺎﻠﻌﺑﺩﺎﻠﻠﻄﻴﻓ OR ﺎﻠﻌﺑﺩ+ﺎﻠﻠﻄﻴﻓ OR ﻊﺑﺩﺎﻠﻠﻄﻴﻓ OR ﻊﺑﺩ+ﺎﻠﻠﻄﻴﻓ OR ﻉ+ﺎﻠﻠﻄﻴﻓ)',
'ﺎﻠﺻﺍﺩﺭﺎﺗ': '(ﺲﻬﻣ+ﺎﻠﺻﺍﺩﺭﺎﺗ OR ﺕﺎﺴﻳ+ﺎﻠﺻﺍﺩﺭﺎﺗ OR ﺕﺎﺳﻯ+ﺎﻠﺻﺍﺩﺭﺎﺗ)',
'ﺄﺳﻼﻛ': '(ﺄﺳﻼﻛ OR ﺎﺳﻼﻛ )',
'ﻢﺠﻣﻮﻋﺓ ﺎﻠﻤﻌﺠﻟ': '(ﻢﺠﻣﻮﻋﺓ+ﺎﻠﻤﻌﺠﻟ OR ﻢﺠﻣﻮﻌﻫ+ﺎﻠﻤﻌﺠﻟ OR ﺲﻬﻣ+ﺎﻠﻤﻌﺠﻟ)',
'ﺍﻸﻧﺎﺒﻴﺑ ﺎﻠﺴﻋﻭﺪﻳﺓ': '(ﺍﻸﻧﺎﺒﻴﺑ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺍﻸﻧﺎﺒﻴﺑ+ﺎﻠﺴﻋﻭﺪﻴﻫ OR ﺍﻼﻧﺎﺒﻴﺑ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺍﻼﻧﺎﺒﻴﺑ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺄﻧﺎﺒﻴﺑ+ﺎﻠﺴﻋﻭﺪﻳﺓ OR ﺄﻧﺎﺒﻴﺑ+ﺎﻠﺴﻋﻭﺪﻴﻫ)',
'ﺎﻠﺨﺿﺮﻳ': '(ﺎﻠﺨﺿﺮﻳ OR ﺎﻠﺨﺿﺭﻯ)',
'ﺎﻠﺧﺰﻓ': '( الزخف )',
'ﺎﻠﺠﺒﺳ': '( الجبس+سهم OR تاسي+الجبس OR تاسى+الجبس )',
'ﺎﻠﻛﺎﺑﻼﺗ': '( سهم+الكابلات OR تاسي+الكابلات OR تاسى+الكابلات )',
'ﺹﺪﻗ': '( صدق+سهم OR صدق+تاسي OR صدق+تاسى OR صدق+الصناعيه OR صدق+الصناعية )',
'ﺎﻤﻳﺎﻨﺘﻴﺗ': '(ﺎﻤﻳﺎﻨﺘﻴﺗ)',
'ﺄﻧﺎﺒﻴﺑ': '(ﺲﻬﻣ+ﺄﻧﺎﺒﻴﺑ OR ﺲﻬﻣ+ﺎﻧﺎﺒﻴﺑ OR ﺎﻧﺎﺒﻴﺑ+ﺎﻠﻋﺮﺒﻳﺓ OR ﺄﻧﺎﺒﻴﺑ+ﺎﻠﻋﺮﺒﻳﺓ OR ﺎﻧﺎﺒﻴﺑ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺄﻧﺎﺒﻴﺑ+ﺎﻠﻋﺮﺒﻴﻫ OR ﺕﺎﺴﻳ+ﺄﻧﺎﺒﻴﺑ OR ﺕﺎﺳﻯ+ﺄﻧﺎﺒﻴﺑ OR ﺕﺎﺴﻳ+ﺎﻧﺎﺒﻴﺑ OR ﺕﺎﺳﻯ+ﺎﻧﺎﺒﻴﺑ)',
'ﺎﻟﺯﺎﻤﻟ ﻞﻠﺼﻧﺎﻋﺓ': '(ﺎﻟﺯﺎﻤﻟ+ﻞﻠﺼﻧﺎﻋﺓ OR ﺎﻟﺯﺎﻤﻟ+ﻞﻠﺼﻧﺎﻌﻫ OR ﺎﻟﺯﺎﻤﻟ)',
'ﺎﻠﺑﺎﺒﻄﻴﻧ': '(ﺎﻠﺑﺎﺒﻄﻴﻧ OR ﺏﺎﺒﻄﻴﻧ)',
'ﺎﻠﻔﺧﺍﺮﻳﺓ': '(ﺎﻠﻔﺧﺍﺮﻳﺓ OR ﺎﻠﻔﺧﺍﺮﻴﻫ)',
'ﻢﺴﻛ': '(ﻢﺴﻛ)',
'ﺎﻠﺒﺣﺭ ﺍﻸﺤﻣﺭ': '(ﺎﻠﺒﺣﺭ+ﺍﻸﺤﻣﺭ OR ﺎﻠﺒﺣﺭ+ﺍﻼﺤﻣﺭ)',
'ﺎﻠﻌﻗﺍﺮﻳﺓ': '(ﺎﻠﻌﻗﺍﺮﻴﻫ+سهم OR ﺎﻠﻌﻗﺍﺮﻳﺓ+سهم OR العقاريه+تاسي OR العقارة+تاسي OR العقاريه+تاسى OR العقارية+تاسى)',
'ﻂﻴﺑﺓ ﻝﻼﺴﺘﺜﻣﺍﺭ': '(ﻂﻴﺑﺓ+ﻝﻼﺴﺘﺜﻣﺍﺭ OR ﻂﻴﺒﻫ+ﻝﻼﺴﺘﺜﻣﺍﺭ OR ﻂﻴﺑﺓ+ﻝﻸﺴﺘﺜﻣﺍﺭ OR ﻂﻴﺒﻫ+ﻝﻸﺴﺘﺜﻣﺍﺭ OR ﻂﻴﺑﺓ+ﻝﻺﺴﺘﺜﻣﺍﺭ OR ﻂﻴﺒﻫ+ﻝﻺﺴﺘﺜﻣﺍﺭ OR ﺲﻬﻣ+ﻂﻴﺒﻫ OR ﺲﻬﻣ+ﻂﻴﺑﺓ OR ﺕﺎﺴﻳ+ﻂﻴﺒﻫ OR ﺕﺎﺳﻯ+ﻂﻴﺒﻫ)',
'ﻢﻛﺓ ﻝﻼﻨﺷﺍﺀ': '(ﻢﻛﺓ+ﻝﻼﻨﺷﺍﺀ OR ﻢﻜﻫ+ﻝﻼﻨﺷﺍﺀ OR ﻢﻛﺓ+ﻝﻸﻨﺷﺍﺀ OR ﻢﻜﻫ+ﻝﻸﻨﺷﺍﺀ OR ﻢﻛﺓ+ﻝﻺﻨﺷﺍﺀ OR ﻢﻜﻫ+ﻝﻺﻨﺷﺍﺀ OR ﺲﻬﻣ+ﻢﻜﻫ OR ﺕﺎﺴﻳ+ﻢﻜﻫ OR ﺕﺎﺳﻯ+ﻢﻜﻫ)',
'ﺎﻠﺘﻌﻤﻳﺭ': '(ﺲﻬﻣ+ﺎﻠﺘﻌﻤﻳﺭ OR ﺕﺎﺴﻳ+ﺎﻠﺘﻌﻤﻳﺭ OR ﺕﺎﺳﻯ+ﺎﻠﺘﻌﻤﻳﺭ)',
'ﺈﻌﻣﺍﺭ': '(ﺲﻬﻣ+ﺈﻌﻣﺍﺭ OR ﺲﻬﻣ+ﺄﻌﻣﺍﺭ OR ﺲﻬﻣ+ﺎﻌﻣﺍﺭ OR ﺕﺎﺴﻳ+ﺈﻌﻣﺍﺭ OR ﺕﺎﺴﻳ+ﺄﻌﻣﺍﺭ OR ﺕﺎﺴﻳ+ﺎﻌﻣﺍﺭ OR ﺕﺎﺳﻯ+ﺈﻌﻣﺍﺭ OR ﺕﺎﺳﻯ+ﺄﻌﻣﺍﺭ OR ﺕﺎﺳﻯ+ﺎﻌﻣﺍﺭ)',
'ﺞﺒﻟ ﻊﻣﺭ': '(ﺞﺒﻟ+ﻊﻣﺭ)',
'ﺩﺍﺭ ﺍﻷﺮﻛﺎﻧ': '(ﺩﺍﺭ+ﺍﻻﺮﻛﺎﻧ OR ﺩﺍﺭ+ﺍﻹﺮﻛﺎﻧ)',
'ﻡﺪﻴﻧﺓ ﺎﻠﻤﻋﺮﻓﺓ': '(ﻡﺪﻴﻧﺓ+ﺎﻠﻤﻋﺮﻓﺓ OR ﻡﺪﻴﻨﻫ+ﺎﻠﻤﻋﺮﻔﻫ OR ﻡﺪﻴﻧﺓ+ﺎﻠﻤﻋﺮﻔﻫ OR ﻡﺪﻴﻨﻫ+ﺎﻠﻤﻋﺮﻓﺓ OR ﺲﻬﻣ+ﺎﻠﻤﻋﺮﻔﻫ OR ﺲﻬﻣ+ﺎﻠﻤﻋﺮﻓﺓ OR ﺕﺎﺴﻳ+ﺎﻠﻤﻋﺮﻔﻫ OR ﺕﺎﺳﻯ+ﺎﻠﻤﻋﺮﻔﻫ OR ﺕﺎﺴﻳ+ﺎﻠﻤﻋﺮﻓﺓ OR ﺕﺎﺳﻯ+ﺎﻠﻤﻋﺮﻓﺓ)',
'ﺎﻠﺒﺣﺮﻳ': '(ﺲﻬﻣ+ﺎﻠﺒﺣﺮﻳ OR ﺲﻬﻣ+ﺎﻠﺒﺣﺭﻯ OR ﺕﺎﺴﻳ+ﺎﻠﺒﺣﺮﻳ OR ﺕﺎﺳﻯ+ﺎﻠﺒﺣﺮﻳ OR ﺕﺎﺴﻳ+ﺎﻠﺒﺣﺭﻯ OR ﺕﺎﺳﻯ+ﺎﻠﺒﺣﺭﻯ)',
'ﺎﻠﻨﻘﻟ ﺎﻠﺠﻣﺎﻌﻳ': '(ﺎﻠﻨﻘﻟ+ﺎﻠﺠﻣﺎﻋﻯ OR ﺎﻠﻨﻘﻟ+ﺎﻠﺠﻣﺎﻌﻳ OR ﺲﻬﻣ+ﺎﻠﺠﻣﺎﻌﻳ OR ﺲﻬﻣ+ﺎﻠﺠﻣﺎﻋﻯ OR ﺕﺎﺴﻳ+ﺎﻠﺠﻣﺎﻌﻳ OR ﺕﺎﺳﻯ+ﺎﻠﺠﻣﺎﻌﻳ OR ﺕﺎﺳﻯ+ﺎﻠﺠﻣﺎﻋﻯ OR ﺕﺎﺳﻯ+ﺎﻠﺠﻣﺎﻋﻯ)',
'ﻢﺑﺭﺩ': '(ﻢﺑﺭﺩ)',
'ﺏﺪﺠﺗ ﺎﻠﺴﻋﻭﺪﻳﺓ': '(ﺏﺪﺠﺗ)',
'ﺖﻫﺎﻤﻫ ﻝﻼﻋﻼﻧ': '(ﺖﻫﺎﻤﻫ+ﻝﻼﻋﻼﻧ OR ﺖﻫﺎﻣﺓ+ﻝﻼﻋﻼﻧ OR ﺖﻫﺎﻤﻫ+ﻝﻸﻋﻼﻧ OR ﺖﻫﺎﻣﺓ+ﻝﻸﻋﻼﻧ OR ﺲﻬﻣ+ﺖﻫﺎﻤﻫ OR ﺲﻬﻣ+ﺖﻫﺎﻣﺓ OR ﺕﺎﺴﻳ+ﺖﻫﺎﻣﺓ OR ﺕﺎﺳﻯ+ﺖﻫﺎﻤﻫ OR ﺕﺎﺴﻳ+ﺖﻫﺎﻤﻫ OR ﺕﺎﺳﻯ+ﺖﻫﺎﻣﺓ)',
'ﺍﻸﺒﺣﺎﺛ ﻭ ﺎﻠﺘﺳﻮﻴﻗ': '(ﺍﻸﺒﺣﺎﺛ+ﺎﻠﺘﺳﻮﻴﻗ OR ﺍﻼﺒﺣﺎﺛ+ﺎﻠﺘﺳﻮﻴﻗ OR ﺎﺒﺣﺎﺛ+ﺖﺳﻮﻴﻗ OR ﺄﺒﺣﺎﺛ+ﺖﺳﻮﻴﻗ OR ﺲﻬﻣ+ﺍﻼﺒﺣﺎﺛ OR ﺲﻬﻣ+ﺍﻸﺒﺣﺎﺛ OR ﺕﺎﺴﻳ+ﺍﻸﺒﺣﺎﺛ OR ﺕﺎﺴﻳ+ﺍﻼﺒﺣﺎﺛ OR ﺕﺎﺳﻯ+ﺍﻸﺒﺣﺎﺛ OR ﺕﺎﺳﻯ+ﺍﻼﺒﺣﺎﺛ)',
#'ﻂﺑﺎﻋﺓ ﻮﺘﻐﻠﻴﻓ': '(ﻂﺑﺎﻌﻫ+ﺖﻐﻠﻴﻓ OR ﻂﺑﺎﻋﺓ+ﺖﻐﻠﻴﻓ OR ﻂﺑﺎﻌﻫ+ﺲﻬﻣ OR ﻂﺑﺎﻋﺓ+ﺲﻬﻣ OR ﺕﺎﺳﻯ+ﻂﺑﺎﻌﻫ OR ﺕﺎﺴﻳ+ﻂﺑﺎﻋﺓ OR ﺕﺎﺳﻯ+ﻂﺑﺎﻋﺓ)',
'ﻂﺑﺎﻋﺓ ﻮﺘﻐﻠﻴﻓ': '( ﻂﺑﺎﻌﻫ+ﺖﻐﻠﻴﻓ OR ﻂﺑﺎﻋﺓ+ﺖﻐﻠﻴﻓ OR ﻂﺑﺎﻌﻫ+ﺲﻬﻣ OR ﻂﺑﺎﻋﺓ+ﺲﻬﻣ OR ﺕﺎﺴﻳ+ﻂﺑﺎﻌﻫ OR ﺕﺎﺴﻳ+ﻂﺑﺎﻋﺓ OR ﺕﺎﺳﻯ+ﻂﺑﺎﻌﻫ OR ﺕﺎﺳﻯ+ﻂﺑﺎﻋﺓ )',
'ﺎﻠﻄﻳﺍﺭ': '(ﺲﻬﻣ+ﺎﻠﻄﻳﺍﺭ OR ﺕﺎﺴﻳ+ﺎﻠﻄﻳﺍﺭ OR ﺕﺎﺳﻯ+ﺎﻠﻄﻳﺍﺭ)',
'ﺎﻠﺤﻜﻳﺭ': '(الحكير)',
'دور': '(ﺩﻭﺭ+ﻞﻠﻀﻳﺎﻓﺓ OR ﺩﻭﺭ+ﻞﻠﻀﻳﺎﻔﻫ OR ﺩﻭﺭ+ﺲﻬﻣ OR ﺕﺎﺴﻳ+ﺩﻭﺭ OR ﺕﺎﺳﻯ+ﺩﻭﺭ OR ﺲﻬﻣ+ﺎﻠﻔﻧﺍﺪﻗ OR ﺕﺎﺴﻳ+ﺎﻠﻔﻧﺍﺪﻗ OR ﺕﺎﺳﻯ+ﺎﻠﻔﻧﺍﺪﻗ)',
'ﺶﻤﺳ': '(ﺲﻬﻣ+ﺶﻤﺳ OR ﺕﺎﺳﻯ+ﺶﻤﺳ OR ﺕﺎﺳﻯ+ﺶﻤﺳ)',
'البنك الأهلي': '(ﺎﻠﺒﻨﻛ+ﺍﻼﻬﻠﻳ OR ﺐﻨﻛ+ﺍﻼﻬﻠﻳ OR ﺲﻬﻣ+ﺍﻼﻬﻠﻳ OR ﺎﻠﺒﻨﻛ+ﺍﻼﻬﻟﻯ OR ﺐﻨﻛ+ﺍﻼﻬﻟﻯ OR ﺲﻬﻣ+ﺍﻼﻬﻟﻯ OR ﺎﻠﺒﻨﻛ+ﺍﻸﻬﻠﻳ OR ﺎﻠﺒﻨﻛ+ﺍﻸﻬﻟﻯ OR ﺐﻨﻛ+ﺍﻸﻬﻟﻯ OR ﺕﺎﺳﻯ+ﺍﻼﻬﻟﻯ)',
'الصناعات الكهربائيه': '( ﺎﻠﺼﻧﺎﻋﺎﺗ+ﺎﻠﻜﻫﺮﺑﺎﺌﻳﺓ OR  ﺎﻠﺼﻧﺎﻋﺎﺗ+ﺎﻠﻜﻫﺮﺑﺎﺌﻴﻫ)',
'بوان': 'بوان',
'ﺎﺴﻤﻨﺗ ﺎﻣ ﺎﻠﻗﺭﻯ': '( ﺎﺴﻤﻨﺗ+ﺎﻣ+ﺎﻠﻗﺭﻯ OR ﺎﺴﻤﻨﺗ+ﺎﻣ+ﺎﻠﻗﺮﻳ OR ﺎﺴﻤﻨﺗ+ﺄﻣ+ﺎﻠﻗﺮﻳ OR ﺎﺴﻤﻨﺗ+ﺄﻣ+ﺎﻠﻗﺭﻯ OR ﺄﺴﻤﻨﺗ+ﺎﻣ+ﺎﻠﻗﺭﻯ OR ﺄﺴﻤﻨﺗ+ﺎﻣ+ﺎﻠﻗﺮﻳ OR ﺄﺴﻤﻨﺗ+ﺄﻣ+ﺎﻠﻗﺮﻳ OR ﺄﺴﻤﻨﺗ+ﺄﻣ+ﺎﻠﻗﺭﻯ )',
'ﺄﺳﻭﺎﻗ ﺎﻠﻣﺯﺮﻋﺓ': '( ﺄﺳﻭﺎﻗ+ﺎﻠﻣﺯﺮﻌﻫ OR ﺄﺳﻭﺎﻗ+ﺎﻠﻣﺯﺮﻋﺓ OR ﺎﺳﻭﺎﻗ+ﺎﻠﻣﺯﺮﻌﻫ OR ﺎﺳﻭﺎﻗ+ﺎﻠﻣﺯﺮﻋﺓ  )',
'ﺎﻠﺤﻣﺍﺪﻳ': '( ﺎﻠﺤﻣﺍﺪﻳ OR ﺎﻠﺤﻣﺍﺩﻯ  OR ﺢﻣﺍﺪﻳ OR ﺢﻣﺍﺩﻯ)',
'ﺝﺰﻳﺭﺓ ﺖﻛﺎﻔﻟ': '( ﺝﺰﻳﺮﻫ+ﺖﻛﺎﻘﻟ OR ﺝﺰﻳﺭﺓ+ﺖﻛﺎﻔﻟ )',
'ﺎﻠﻋﺮﺒﻳ ﻞﻠﺗﺄﻤﻴﻧ': '(  ﺎﻠﻋﺮﺒﻳ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺎﻠﻋﺮﺑﻯ+ﻞﻠﺗﺄﻤﻴﻧ OR ﺎﻠﻋﺮﺒﻳ+ﻞﻠﺗﺎﻤﻴﻧ OR ﺎﻠﻋﺮﺑﻯ+ﻞﻠﺗﺎﻤﻴﻧ)',
'ﻢﺠﻣﻮﻋﺓ ﺎﻠﺤﻜﻳﺭ': '( ﺎﻠﺤﻜﻳﺭ )',
'ميبكو': '( الشرق+الاوسط+تاسي OR الشرق+الورق+تاسي OR تاسي+الشرق OR الاوسط+تاسي OR ميبكو+سهم OR سهم+الأوسط OR سهم+الاوسط )',
'ساكو': '( ساكو OR SACO OR عدد+أدوات OR عدد+ادوات )',
'مبكو':'(مبكو OR الشركة+السعودية+للخدمات+الأرضيةi)',
'الخدمات الأرضية': '(الخدمات+الأرضية  OR الخدمات+الارضية OR الخدمات الأرضيه OR ﺎﻠﺧﺪﻣﺎﺗ+ﺍﻻﺮﻀﻳه OR ﺎﻠﺧﺪﻣﺎﺗ+الأرضية )',
};


full_name = {
'ﺕﺎﺴﻳ': 'ﺕﺎﺴﻳ',
'ﺎﺴﻤﻨﺗ ﺎﻣ ﺎﻠﻗﺭﻯ': 'شركه ﺎﺴﻤﻨﺗ ﺎﻣ ﺎﻠﻗﺭﻯ',
'ﺄﺳﻭﺎﻗ ﺎﻠﻣﺯﺮﻋﺓ': 'ﺎﻠﺷﺮﻛﺓ السعوديه للتسويق',
'ﺎﻠﺤﻣﺍﺪﻳ':'ﺵﺮﻛﺓ ﺎﻠﺤﻣﺍﺪﻳ ﻞﻠﺘﻨﻤﻳﺓ ﻭﺍﻼﺴﺘﺜﻣﺍﺭ',                   
'ﺝﺰﻳﺭﺓ ﺖﻛﺎﻔﻟ':'ﺵﺮﻛﺓ ﺎﻠﺟﺰﻳﺭﺓ ﺖﻛﺎﻔﻟ ﺖﻋﺍﻮﻨﻳ',
'ﺎﻠﻋﺮﺒﻳ ﻞﻠﺗﺄﻤﻴﻧ': 'ﺵﺮﻛﺓ ﻢﺗﻼﻴﻓ ﻭﺎﻴﻫ ﺄﻳ ﺞﻳ ﻭﺎﻠﺒﻨﻛ ﺎﻠﻋﺮﺒﻳ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﻢﺠﻣﻮﻋﺓ ﺎﻠﺤﻜﻳﺭ': 'ﻢﺠﻣﻮﻋﺓ ﺎﻠﺤﻜﻳﺭ',
'ﺎﻟﺮﻳﺎﺿ': 'ﺐﻨﻛ+ﺎﻟﺮﻳﺎﺿ',
'ﺎﻠﺟﺰﻳﺭﺓ': 'ﺵﺮﻛﺓ+ﺎﻠﺟﺰﻳﺭﺓ+ﺖﻛﺎﻔﻟ+ﺖﻋﺍﻮﻨﻳ',
'ﺎﺴﺘﺜﻣﺍﺭ': 'ﺎﻠﺒﻨﻛ+ﺎﻠﺴﻋﻭﺪﻳ+ﻝﻼﺴﺘﺜﻣﺍﺭ',
'ﺎﻠﺴﻋﻭﺪﻳ ﺎﻠﻫﻮﻠﻧﺪﻳ': 'ﺎﻠﺒﻨﻛ+ﺎﻠﺴﻋﻭﺪﻳ+ﺎﻠﻫﻮﻠﻧﺪﻳ',
'ﺎﻠﺴﻋﻭﺪﻳ ﺎﻠﻓﺮﻨﺴﻳ': 'ﺎﻠﺒﻨﻛ+ﺎﻠﺴﻋﻭﺪﻳ+ﺎﻠﻓﺮﻨﺴﻳ',
'ﺱﺎﺑ': 'البنك+السعودي+البريطاني',
'ﺎﻠﻋﺮﺒﻳ ﺎﻟﻮﻄﻨﻳ': 'ﺎﻠﺒﻨﻛ ﺎﻠﻋﺮﺒﻳ ﺎﻟﻮﻄﻨﻳ',
'ﺱﺎﻤﺑﺍ': 'ﻢﺠﻣﻮﻋﺓ ﺱﺎﻤﺑﺍ ﺎﻠﻣﺎﻠﻳﺓ',
'ﺎﻟﺭﺎﺠﺤﻳ': 'ﻢﺻﺮﻓ ﺎﻟﺭﺎﺠﺤﻳ',
'ﺎﻠﺑﻻﺩ': 'ﺐﻨﻛ ﺎﻠﺑﻻﺩ',
'ﺍﻺﻨﻣﺍﺀ': 'ﻢﺻﺮﻓ ﺍﻺﻨﻣﺍﺀ',
'ﻚﻴﻣﺎﻧﻮﻟ': 'ﺵﺮﻛﺓ ﺖﻛﻮﻴﻧ ﺎﻠﻤﺘﻃﻭﺭﺓ ﻞﻠﺼﻧﺎﻋﺎﺗ',
'ﺐﺗﺭﻮﻜﻴﻣ': 'ﺵﺮﻛﺓ ﺎﻠﺼﺣﺭﺍﺀ ﻞﻠﺒﺗﺭﻮﻜﻴﻣﺍﻮﻳﺎﺗ',
'ﺱﺎﺒﻛ': 'ﺵﺮﻛﺓ ﺎﻠﺼﻧﺎﻋﺎﺗ ﺎﻠﻜﻴﻤﻳﺎﺌﻳﺓ ﺍﻸﺳﺎﺴﻳﺓ',
'ﺱﺎﻔﻛﻭ': 'شركة الأسمدة العربية السعودية',
'ﺎﻠﺘﺼﻨﻴﻋ': 'شركة التصنيع الوطنية',
'ﺎﻠﻠﺠﻴﻧ': 'شركة اللجين',
'ﻦﻣﺍﺀ ﻞﻠﻜﻴﻣﺍﻮﻳﺎﺗ': 'ﺵﺮﻛﺓ ﻦﻣﺍﺀ ﻞﻠﻜﻴﻣﺍﻮﻳﺎﺗ',
'ﺎﻠﻤﺠﻣﻮﻋﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ': 'ﺎﻠﻤﺠﻣﻮﻋﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻝﻺﺴﺘﺜﻣﺍﺭ ﺎﻠﺼﻧﺎﻌﻳ',
'ﺎﻠﺼﺣﺭﺍﺀ ﻞﻠﺒﺗﺭﻮﻜﻴﻣﺍﻮﻳﺎﺗ': 'ﺵﺮﻛﺓ ﺎﻠﺼﺣﺭﺍﺀ ﻞﻠﺒﺗﺭﻮﻜﻴﻣﺍﻮﻳﺎﺗ',
'ﻲﻨﺳﺎﺑ': 'شركة ينبع الوطنية للبتروكيماويات',
'ﺲﺒﻜﻴﻣ ﺎﻠﻋﺎﻠﻤﻳﺓ': 'الشركة السعودية العالمية للبتروكيماويات',
'ﺎﻠﻤﺘﻗﺪﻣﺓ': 'الشركة المتقدمة للبتروكيماويات',
'ﻚﻳﺎﻧ': 'شركة كيان السعودية للبتروكيماويات',
'ﺐﺗﺭﻭ ﺭﺎﺒﻏ': 'شركة رابغ للتكرير و البتروكيماويات',
'ﺄﺴﻤﻨﺗ ﺡﺎﺌﻟ': 'ﺵﺮﻛﺓ ﺄﺴﻤﻨﺗ ﺡﺎﺌﻟ',
'ﺄﺴﻤﻨﺗ ﻦﺟﺭﺎﻧ': 'ﺵﺮﻛﺓ ﺄﺴﻤﻨﺗ ﻦﺟﺭﺎﻧ',
'ﺎﺴﻤﻨﺗ ﺎﻠﻣﺪﻴﻧﺓ': 'ﺵﺮﻛﺓ ﺎﺴﻤﻨﺗ ﺎﻠﻣﺪﻴﻧﺓ',
'ﺎﺴﻤﻨﺗ ﺎﻠﺸﻣﺎﻠﻳﺓ': 'ﺵﺮﻛﺓ ﺄﺴﻤﻨﺗ ﺎﻠﻤﻨﻄﻗﺓ ﺎﻠﺸﻣﺎﻠﻳﺓ',
'ﺍﻼﺴﻤﻨﺗ ﺎﻠﻋﺮﺒﻳﺓ': 'ﺵﺮﻛﺓ ﺍﻼﺴﻤﻨﺗ ﺎﻠﻋﺮﺒﻳﺓ',
'ﺎﺴﻤﻨﺗ ﺎﻠﻴﻣﺎﻣﺓ': 'ﺵﺮﻛﺓ ﺎﺴﻤﻨﺗ ﺎﻠﻴﻣﺎﻣﺓ',
'ﺎﺴﻤﻨﺗ ﺎﻠﺴﻋﻭﺪﻴﻫ': 'ﺵﺮﻛﺓ ﺍﻸﺴﻤﻨﺗ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﺎﺴﻤﻨﺗ ﺎﻠﻘﺼﻴﻣ': 'ﺵﺮﻛﺓ ﺎﺴﻤﻨﺗ ﺎﻠﻘﺼﻴﻣ',
'ﺎﺴﻤﻨﺗ ﺎﻠﺠﻧﻮﺒﻴﻫ': 'ﺵﺮﻛﺓ ﺎﺴﻤﻨﺗ ﺎﻠﻤﻨﻄﻗﺓ ﺎﻠﺠﻧﻮﺒﻴﻫ',
'ﺎﺴﻤﻨﺗ ﻲﻨﺒﻋ': 'ﺵﺮﻛﺓ ﺎﺴﻤﻨﺗ ﻲﻨﺒﻋ',
'ﺎﺴﻤﻨﺗ ﺎﻠﺷﺮﻘﻳﺓ': 'ﺵﺮﻛﺓ ﺎﺴﻤﻨﺗ ﺎﻠﻤﻨﻄﻗﺓ ﺎﻠﺷﺮﻘﻳﺓ',
'ﺎﺴﻤﻨﺗ ﺖﺑﻮﻛ': 'ﺵﺮﻛﺓ ﺎﺴﻤﻨﺗ ﺖﺑﻮﻛ',
'ﺎﺴﻤﻨﺗ ﺎﻠﺟﻮﻓ': 'ﺵﺮﻛﺓ ﺎﺴﻤﻨﺗ ﺎﻠﺟﻮﻓ',
'ﺄﺳﻭﺎﻗ ﻉ ﺎﻠﻌﺜﻴﻣ': 'ﺵﺮﻛﺓ ﺄﺳﻭﺎﻗ ﻊﺑﺩﺎﻠﻠﻫ ﺎﻠﻌﺜﻴﻣ',
'ﺎﻠﻣﻭﺎﺳﺍﺓ': 'ﺵﺮﻛﺓ ﺎﻠﻣﻭﺎﺳﺍﺓ ﻞﻠﺧﺪﻣﺎﺗ ﺎﻠﻄﺒﻳﺓ',
'ﺈﻜﺴﺗﺭﺍ': 'الشركة المتحدة للإلكترونيات',
'ﺪﻠﻫ ﺎﻠﺼﺤﻳﺓ': 'ﺵﺮﻛﺓ ﺪﻠﻫ ﻞﻠﺧﺪﻣﺎﺗ ﺎﻠﺼﺤﻳﺓ ﺎﻠﻗﺎﺒﺿﺓ',
'ﺮﻋﺎﻳﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻟﻮﻄﻨﻳﺓ ﻞﻟﺮﻋﺎﻳﺓ ﺎﻠﻄﺒﻳﺓ',
'ﺱﺎﺴﻛﻭ': 'الشركة السعودية لخدمات السيارات والمعدات',
'ﺚﻣﺍﺭ': 'الشركة الوطنية للتسويق الزراعي',
'ﻢﺠﻣﻮﻋﺓ ﻒﺘﻴﺤﻳ': 'ﻢﺠﻣﻮﻋﺓ ﻒﺘﻴﺤﻳ ﺎﻠﻗﺎﺒﺿﺓ',
'ﺝﺮﻳﺭ': 'ﺵﺮﻛﺓ ﺝﺮﻳﺭ ﻞﻠﺘﺳﻮﻴﻗ',
'ﺎﻟﺩﺮﻴﺳ': 'ﺵﺮﻛﺓ ﺎﻟﺩﺮﻴﺳ ﻞﻠﺧﺪﻣﺎﺗ ﺎﻠﺒﺗﺭﻮﻠﻳﺓ ﻭ ﺎﻠﻨﻘﻠﻳﺎﺗ',
'ﺎﻠﺤﻜﻳﺭ': 'ﺵﺮﻛﺓ ﻑﻭﺍﺯ ﻊﺑﺩﺎﻠﻋﺰﻳﺯ ﺎﻠﺤﻜﻳﺭ ﻮﺷﺮﻛﺎﻫ',
'ﺎﻠﺨﻠﻴﺟ ﻞﻠﺗﺩﺮﻴﺑ': 'ﺵﺮﻛﺓ ﺎﻠﺨﻠﻴﺟ ﻞﻠﺗﺩﺮﻴﺑ ﻭ ﺎﻠﺘﻌﻠﻴﻣ',
'ﺎﻠﻏﺍﺯ ﻭﺎﻠﺘﺼﻨﻴﻋ': 'ﺵﺮﻛﺓ ﺎﻠﻏﺍﺯ ﻭﺎﻠﺘﺼﻨﻴﻋ ﺍﻼﻬﻠﻳﺓ',
'ﻚﻫﺮﺑﺍﺀ ﺎﻠﺴﻋﻭﺪﻳﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻞﻠﻜﻫﺮﺑﺍﺀ',
'ﻢﺠﻣﻮﻋﺓ ﺹﺎﻓﻭﻻ': 'ﻢﺠﻣﻮﻋﺓ ﺹﺎﻓﻭﻻ',
'ﺎﻠﻏﺫﺎﺌﻳﺓ': 'شركة وفرة للصناعة والتنمية',
'ﺱﺩﺎﻔﻛﻭ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻞﻤﻨﺘﺟﺎﺗ ﺍﻸﻠﺑﺎﻧ ﻭﺍﻸﻏﺬﻳﺓ (ﺱﺩﺎﻔﻛﻭ)',
'ﺎﻠﻣﺭﺎﻌﻳ': 'ﺵﺮﻛﺓ ﺎﻠﻣﺭﺎﻌﻳ',
'ﺄﻨﻋﺎﻣ ﺎﻠﻗﺎﺒﺿﺓ': 'ﺵﺮﻛﺓ ﻢﺠﻣﻮﻋﺓ ﺄﻨﻋﺎﻣ ﺎﻟﺩﻮﻠﻳﺓ ﺎﻠﻗﺎﺒﺿﺓ',
'ﺢﻟﻭﺎﻨﻳ ﺈﺧﻭﺎﻧ': 'ﺢﻟﻭﺎﻨﻳ ﺈﺧﻭﺎﻧ',
'ﻩﺮﻔﻳ ﻝﻸﻏﺬﻳﺓ': 'ﺵﺮﻛﺓ ﻩﺮﻔﻳ ﻞﻠﺧﺪﻣﺎﺗ ﺎﻠﻏﺫﺎﺌﻳﺓ',
'ﺎﻠﺘﻣﻮﻴﻧ': 'ﺵﺮﻛﺓ ﺎﻠﺨﻃﻮﻃ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻞﻠﺘﻣﻮﻴﻧ',
'ﻥﺍﺪﻛ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻟﻮﻄﻨﻳﺓ ﻞﻠﺘﻨﻤﻳﺓ ﺎﻟﺯﺭﺎﻌﻳﺓ',
'ﺎﻠﻘﺼﻴﻣ ﺎﻟﺯﺭﺎﻌﻴﻫ': 'ﺵﺮﻛﺓ ﺎﻠﻘﺼﻴﻣ ﺎﻟﺯﺭﺎﻌﻳﺓ',
'ﺖﺑﻮﻛ ﺎﻟﺯﺭﺎﻌﻴﻫ': 'ﺵﺮﻛﺓ ﺖﺑﻮﻛ ﻞﻠﺘﻨﻤﻳﺓ ﺎﻟﺯﺭﺎﻌﻳﺓ',
'ﺍﻸﺴﻣﺎﻛ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻝﻸﺴﻣﺎﻛ',
'ﺎﻠﺷﺮﻘﻳﺓ ﻞﻠﺘﻨﻤﻳﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺷﺮﻘﻳﺓ ﻞﻠﺘﻨﻤﻳﺓ',
'ﺎﻠﺟﻮﻓ ﺎﻟﺯﺭﺎﻌﻴﻫ': 'ﺵﺮﻛﺓ ﺎﻠﺟﻮﻓ ﺎﻟﺯﺭﺎﻌﻳﺓ',
'ﺐﻴﺷﺓ ﺎﻟﺯﺭﺎﻌﻴﻫ': 'ﺵﺮﻛﺓ ﺐﻴﺷﺓ ﻞﻠﺘﻨﻤﻳﺓ ﺎﻟﺯﺭﺎﻌﻳﺓ',
'ﺝﺍﺯﺎﻧ ﻞﻠﺘﻨﻤﻳﺓ': 'ﺵﺮﻛﺓ ﺝﺍﺯﺎﻧ ﻞﻠﺘﻨﻤﻳﺓ',
'ﺍﻼﺘﺻﺍﻼﺗ': 'ﺵﺮﻛﺓ ﺍﻼﺘﺻﺍﻼﺗ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﺎﺘﺣﺍﺩ ﺎﺘﺻﺍﻼﺗ': 'ﺵﺮﻛﺓ ﺈﺘﺣﺍﺩ ﺈﺘﺻﺍﻼﺗ',
'ﺰﻴﻧ ﺎﻠﺴﻋﻭﺪﻳﺓ': 'ﺵﺮﻛﺓ ﺍﻼﺘﺻﺍﻼﺗ ﺎﻠﻤﺘﻨﻘﻟﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﻉﺬﻴﺑ ﻝﻼﺘﺻﺍﻼﺗ': 'ﺵﺮﻛﺓ ﺈﺘﺣﺍﺩ ﻉﺬﻴﺑ ﻝﻼﺘﺻﺍﻼﺗ',
'ﺎﻠﻤﺘﻛﺎﻤﻟﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻝﻺﺘﺻﺍﻼﺗ ﺎﻠﻤﺘﻛﺎﻤﻟﺓ',
'ﺎﻠﺘﻋﺍﻮﻨﻳﺓ': 'ﺵﺮﻛﺓ ﺎﻠﺘﻋﺍﻮﻨﻳﺓ ﻞﻠﺗﺄﻤﻴﻧ',
'ﻡﻻﺫ ﻞﻠﺗﺄﻤﻴﻧ': 'شركة ملاذ للتأمين وإعادة التأمين التعاوني',
'ﻢﻳﺪﻐﻠﻓ ﻞﻠﺗﺄﻤﻴﻧ': 'شركة متلايف وايه أي جي والبنك العربي للتأمين التعاوني',
'ﺄﻠﻳﺎﻧﺯ ﺈﺳ ﺈﻓ': 'شركة أليانز السعودي الفرنسي للتأمين التعاوني',
'ﺱﻼﻣﺓ': 'ﺵﺮﻛﺓ ﺱﻼﻣﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﻭﻻﺀ ﻞﻠﺗﺄﻤﻴﻧ': 'الشركة السعودية المتحدة للتأمين التعاوني',
'ﺎﻟﺩﺮﻋ ﺎﻠﻋﺮﺒﻳ': 'ﺵﺮﻛﺓ ﺎﻟﺩﺮﻋ ﺎﻠﻋﺮﺒﻳ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺱﺎﺑ ﺖﻛﺎﻔﻟ': 'ﺱﺎﺑ ﻞﻠﺘﻛﺎﻔﻟ',
'ﺲﻧﺩ': 'ﺵﺮﻛﺓ ﺲﻧﺩ ﻞﻠﺗﺄﻤﻴﻧ ﻭ ﺈﻋﺍﺩﺓ ﺎﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺱﺎﻴﻛﻭ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﻋﺮﺒﻳﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﻮﻓﺍ ﻞﻠﺗﺄﻤﻴﻧ': 'الشركة السعودية الهندية للتأمين التعاوني',
'ﺈﺘﺣﺍﺩ ﺎﻠﺨﻠﻴﺟ': 'ﺵﺮﻛﺓ ﺈﺘﺣﺍﺩ ﺎﻠﺨﻠﻴﺟ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺍﻸﻬﻠﻳ ﻞﻠﺘﻛﺎﻔﻟ': 'ﺵﺮﻛﺓ ﺍﻸﻬﻠﻳ ﻞﻠﺘﻛﺎﻔﻟ',
'ﺍﻸﻬﻠﻳﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺍﻸﻬﻠﻳﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺄﺴﻴﺟ': 'ﺎﻠﻤﺠﻣﻮﻋﺓ ﺎﻠﻤﺘﺣﺩﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺎﻠﺗﺄﻤﻴﻧ ﺎﻠﻋﺮﺒﻳﺓ': 'ﺵﺮﻛﺓ ﺎﻠﺗﺄﻤﻴﻧ ﺎﻠﻋﺮﺒﻳﺓ ﺎﻠﺘﻋﺍﻮﻨﻳﺓ',
'ﺍﻼﺘﺣﺍﺩ ﺎﻠﺘﺟﺍﺮﻳ': 'ﺵﺮﻛﺓ ﺍﻼﺘﺣﺍﺩ ﺎﻠﺘﺟﺍﺮﻳ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺎﻠﺼﻗﺭ ﻞﻠﺗﺄﻤﻴﻧ': 'ﺵﺮﻛﺓ ﺎﻠﺼﻗﺭ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺎﻠﻤﺘﺣﺩﺓ ﻞﻠﺗﺄﻤﻴﻧ': 'ﺎﻠﻤﺠﻣﻮﻋﺓ ﺎﻠﻤﺘﺣﺩﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺍﻺﻋﺍﺩﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻺﻋﺍﺩﺓ ﺎﻠﺗﺄﻤﻴﻧ(ﺈﻋﺍﺩﺓ) ﺎﻠﺘﻋﺍﻮﻨﻳﺓ',
'ﺏﻮﺑﺍ ﺎﻠﻋﺮﺒﻳﺓ': 'ﺏﻮﺑﺍ ﺎﻠﻋﺮﺒﻳﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﻮﻗﺎﻳﺓ ﻞﻠﺘﻛﺎﻔﻟ': 'ﺵﺮﻛﺓ ﻮﻗﺎﻳﺓ ﻞﻠﺗﺄﻤﻴﻧ ﻭ ﺈﻋﺍﺩﺓ ﺎﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻛﺎﻔﻠﻳ',
'ﺖﻛﺎﻔﻟ ﺎﻟﺭﺎﺠﺤﻳ': 'ﺵﺮﻛﺓ ﺎﻟﺭﺎﺠﺤﻳ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺎﻴﺳ': 'ﺵﺮﻛﺓ ﺄﻴﺳ ﺎﻠﻋﺮﺒﻳﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺎﻜﺳﺍ- ﺎﻠﺘﻋﺍﻮﻨﻳﺓ': 'ﺵﺮﻛﺓ ﺎﻜﺳﺍ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺎﻠﺨﻠﻴﺠﻳﺓ ﺎﻠﻋﺎﻣﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺨﻠﻴﺠﻳﺓ ﺎﻠﻋﺎﻣﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺏﺭﻮﺟ ﻞﻠﺗﺄﻤﻴﻧ': 'ﺵﺮﻛﺓ ﺏﺭﻮﺟ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺎﻠﻋﺎﻠﻤﻳﺓ': 'ﺵﺮﻛﺓ ﺎﻠﻋﺎﻠﻤﻳﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺱﻮﻠﻳﺩﺮﺘﻳ ﺖﻛﺎﻔﻟ': 'ﺵﺮﻛﺓ ﺱﻮﻠﻳﺩﺮﺘﻳ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻞﻠﺘﻛﺎﻔﻟ',
'ﺎﻟﻮﻄﻨﻳﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻟﻮﻄﻨﻳﺓ ﻞﻠﺗﺄﻤﻴﻧ',
'ﺄﻣﺎﻧﺓ ﻞﻠﺗﺄﻤﻴﻧ': 'ﺵﺮﻛﺓ ﺄﻣﺎﻧﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﻊﻧﺎﻳﺓ': 'ﺵﺮﻛﺓ ﻊﻧﺎﻳﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻞﻠﺗﺄﻤﻴﻧ ﺎﻠﺘﻋﺍﻮﻨﻳ',
'ﺍﻺﻨﻣﺍﺀ ﻁﻮﻜﻳﻭ ﻡ': 'ﺵﺮﻛﺓ ﺍﻺﻨﻣﺍﺀ ﻁﻮﻜﻳﻭ ﻡﺍﺮﻴﻧ',
'ﺎﻠﻤﺻﺎﻔﻳ': 'ﺵﺮﻛﺓ ﺎﻠﻤﺻﺎﻔﻳ ﺎﻠﻋﺮﺒﻳﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﺎﻠﻤﺘﻃﻭﺭﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻞﻠﺼﻧﺎﻋﺎﺗ ﺎﻠﻤﺘﻃﻭﺭﺓ',
'ﺍﻼﺤﺳﺍﺀ ﻞﻠﺘﻨﻤﻴﻫ': 'ﺵﺮﻛﺓ ﺍﻼﺤﺳﺍﺀ ﻞﻠﺘﻨﻤﻳﺓ',
'ﺲﻴﺴﻛﻭ': 'الشركة السعودية للخدمات الصناعية',
'ﻊﺴﻳﺭ': 'ﺵﺮﻛﺓ ﻊﺴﻳﺭ ﻞﻠﺘﺟﺍﺭﺓ ﻭﺎﻠﺴﻳﺎﺣﺓ ﻭﺎﻠﺼﻧﺎﻋﺓ',
'ﺎﻠﺑﺎﺣﺓ': 'ﺵﺮﻛﺓ ﺎﻠﺑﺎﺣﺓ ﻝﻺﺴﺘﺜﻣﺍﺭ ﻭﺎﻠﺘﻨﻤﻳﺓ',
'ﺎﻠﻤﻤﻠﻛﺓ': 'ﺵﺮﻛﺓ ﺎﻠﻤﻤﻠﻛﺓ ﺎﻠﻗﺎﺒﺿﺓ',
'ﺖﻛﻮﻴﻧ': 'ﺵﺮﻛﺓ ﺖﻛﻮﻴﻧ ﺎﻠﻤﺘﻃﻭﺭﺓ ﻞﻠﺼﻧﺎﻋﺎﺗ',
'ﺏﻯ ﺱﻯ ﺁﻯ': 'شركة الصناعات الكيميائية الأساسية',
'ﻢﻋﺍﺪﻧ': 'شركة التعدين العربية السعودية',
'ﺄﺴﺗﺭﺍ ﺎﻠﺼﻧﺎﻌﻳﺓ': 'ﻢﺠﻣﻮﻋﺓ ﺄﺴﺗﺭﺍ ﺎﻠﺼﻧﺎﻌﻳﺓ',
'ﻢﺠﻣﻮﻋﺓ ﺎﻠﺳﺮﻴﻋ': 'ﺵﺮﻛﺓ ﻢﺠﻣﻮﻋﺓ ﺎﻠﺳﺮﻴﻋ ﺎﻠﺘﺟﺍﺮﻳﺓ ﺎﻠﺼﻧﺎﻌﻳﺓ',
'ﺵﺎﻛﺭ': 'ﺵﺮﻛﺓ ﺎﻠﺤﺴﻧ ﻍﺍﺰﻳ ﺈﺑﺭﺎﻬﻴﻣ ﺵﺎﻛﺭ',
'ﺎﻟﺩﻭﺎﺌﻳﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻞﻠﺼﻧﺎﻋﺎﺗ ﺎﻟﺩﻭﺎﺌﻳﺓ ﻭﺎﻠﻤﺴﺘﻟﺰﻣﺎﺗ ﺎﻠﻄﺒﻳﺓ',
'ﺰﺟﺎﺟ': 'ﺵﺮﻛﺓ ﺎﻠﺼﻧﺎﻋﺎﺗ ﺎﻟﺰﺟﺎﺠﻳﺓ ﺎﻟﻮﻄﻨﻳﺓ',
'ﻒﻴﺒﻛﻭ': 'شركة تصنيع مواد التعبئة والتغليف',
'ﻢﻋﺪﻨﻳﺓ': 'الشركة الوطنية لتصنيع وسبك المعادن',
'ﺎﻠﻜﻴﻤﻳﺎﺌﻴﻫ ﺎﻠﺴﻋﻭﺪﻴﻫ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﻜﻴﻤﻳﺎﺌﻳﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﺺﻧﺎﻋﺓ ﺎﻟﻭﺮﻗ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻞﺼﻧﺎﻋﺓ ﺎﻟﻭﺮﻗ',
'ﺎﻠﻌﺑﺩﺎﻠﻠﻄﻴﻓ': 'ﺵﺮﻛﺓ ﺎﻠﻌﺑﺩﺎﻠﻠﻄﻴﻓ ﻝﻼﺴﺘﺜﻣﺍﺭ ﺎﻠﺼﻧﺎﻌﻳ',
'ﺎﻠﺻﺍﺩﺭﺎﺗ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻞﻠﺻﺍﺩﺭﺎﺗ ﺎﻠﺼﻧﺎﻌﻳﺓ',
'ﺄﺳﻼﻛ': 'ﺵﺮﻛﺓ ﺈﺘﺣﺍﺩ ﻢﺻﺎﻨﻋ ﺍﻸﺳﻼﻛ',
'ﻢﺠﻣﻮﻋﺓ ﺎﻠﻤﻌﺠﻟ': 'ﺵﺮﻛﺓ ﻢﺠﻣﻮﻋﺓ ﻢﺤﻣﺩ ﺎﻠﻤﻌﺠﻟ',
'ﺍﻸﻧﺎﺒﻴﺑ ﺎﻠﺴﻋﻭﺪﻳﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻸﻧﺎﺒﻴﺑ ﺎﻠﺼﻠﺑ',
'ﺎﻠﺨﺿﺮﻳ': 'ﺵﺮﻛﺓ ﺄﺒﻧﺍﺀ ﻊﺑﺩﺎﻠﻠﻫ ﻊﺑﺩﺎﻠﻤﺤﺴﻧ ﺎﻠﺨﺿﺮﻳ',
'ﺎﻠﺧﺰﻓ': 'ﺵﺮﻛﺓ ﺎﻠﺧﺰﻓ ﺎﻠﺴﻋﻭﺪﻳ',
'ﺎﻠﺠﺒﺳ': 'ﺵﺮﻛﺓ ﺎﻠﺠﺒﺳ ﺍﻸﻬﻠﻳﺓ',
'ﺎﻠﻛﺎﺑﻼﺗ': 'ﺵﺮﻛﺓ ﺎﻠﻛﺎﺑﻼﺗ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﺹﺪﻗ': 'الشركة السعودية للتنمية الصناعية',
'ﺎﻤﻳﺎﻨﺘﻴﺗ': 'ﺵﺮﻛﺓ ﺎﻤﻳﺎﻨﺘﻴﺗ ﺎﻠﻋﺮﺒﻳﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ',
'ﺄﻧﺎﺒﻴﺑ': 'الشركة العربية للأنابيب',
'ﺎﻟﺯﺎﻤﻟ ﻞﻠﺼﻧﺎﻋﺓ': 'ﺵﺮﻛﺓ ﺎﻟﺯﺎﻤﻟ ﻝﻼﺴﺘﺜﻣﺍﺭ ﺎﻠﺼﻧﺎﻌﻳ',
'ﺎﻠﺑﺎﺒﻄﻴﻧ': 'ﺵﺮﻛﺓ ﺎﻠﺑﺎﺒﻄﻴﻧ ﻞﻠﻃﺎﻗﺓ ﻭ ﺍﻼﺘﺻﺍﻼﺗ',
'ﺎﻠﻔﺧﺍﺮﻳﺓ': 'ﺎﻠﺷﺮﻛﺓ ﺎﻠﺴﻋﻭﺪﻳﺓ ﻺﻨﺗﺎﺟ ﺍﻸﻧﺎﺒﻴﺑ ﺎﻠﻔﺧﺍﺮﻳﺓ',
'ﻢﺴﻛ': 'شركة الشرق الأوسط للكابلات المتخصصة',
'ﺎﻠﺒﺣﺭ ﺍﻸﺤﻣﺭ': 'ﺎﻠﺒﺣﺭ ﺍﻸﺤﻣﺭ',
'ﺎﻠﻌﻗﺍﺮﻳﺓ': 'الشركة العقارية السعودية',
'ﻂﻴﺑﺓ ﻝﻼﺴﺘﺜﻣﺍﺭ': 'شركة طيبة القابضة',
'ﻢﻛﺓ ﻝﻼﻨﺷﺍﺀ': 'شركة مكة للإنشاء والتعمير',
'ﺎﻠﺘﻌﻤﻳﺭ': 'شركة الرياض للتعمير',
'ﺈﻌﻣﺍﺭ': 'إعمار المدينة الإقتصادية',
'ﺞﺒﻟ ﻊﻣﺭ': 'شركة جبل عمر للتطوير',
'ﺩﺍﺭ ﺍﻷﺮﻛﺎﻧ': 'شركة دار الأركان للتطوير العقاري',
'ﻡﺪﻴﻧﺓ ﺎﻠﻤﻋﺮﻓﺓ': 'شركة مدينة المعرفة الإقتصادية',
'ﺎﻠﺒﺣﺮﻳ': 'الشركة الوطنية السعودية للنقل البحري',
'ﺎﻠﻨﻘﻟ ﺎﻠﺠﻣﺎﻌﻳ': 'الشركة السعودية للنقل الجماعي ( سابتكو )',
'ﻢﺑﺭﺩ': 'الشركة السعودية للنقل والاستثمار',
'ﺏﺪﺠﺗ ﺎﻠﺴﻋﻭﺪﻳﺓ': 'الشركة المتحدة الدولية للمواصلات',
'ﺖﻫﺎﻤﻫ ﻝﻼﻋﻼﻧ': 'شركة تهامه للاعلان والعلاقات العامة',
'ﺍﻸﺒﺣﺎﺛ ﻭ ﺎﻠﺘﺳﻮﻴﻗ': 'المجموعة السعودية للأبحاث و التسويق',
'ﻂﺑﺎﻋﺓ ﻮﺘﻐﻠﻴﻓ': 'الشركة السعودية للطباعة والتغليف',
'ﺎﻠﻄﻳﺍﺭ': 'مجموعة الطيار للسفر القابضة',
'ﺎﻠﻔﻧﺍﺪﻗ': 'ﺎﻠﻔﻧﺍﺪﻗ',
'ﺎﻠﺤﻜﻳﺭ': 'ﺵﺮﻛﺓ ﻢﺠﻣﻮﻋﺓ ﻊﺑﺩﺎﻠﻤﺤﺴﻧ ﺎﻠﺤﻜﻳﺭ ﻞﻠﺴﻳﺎﺣﺓ ﻭﺎﻠﺘﻨﻤﻳﺓ',
'دور': 'شركة دور للضيافة',
'ﺶﻤﺳ': 'شركة المشروعات السياحية',
'البنك الأهلي': 'البنك الاهلي التجاري',
'الصناعات الكهربائيه': 'ﺎﻠﺼﻧﺎﻋﻼﺗ ﺎﻠﻜﻫﺭﺎﺌﻴﻫ',
'بوان': 'ﺵﺮﻛﺓ ﺏﻭﺎﻧ',
'ميبكو': 'الشرق الاوسط لصناعه وانتاج الورق',
'ساكو': 'الشركة السعودية للعدد والأدوات',
'مبكو':'الشركة السعودية للخدمات الأرضية',
'الخدمات الأرضية': 'الشركة السعودية للخدمات الأرضية',
}


query_list = []
######################################
# Matrix 1
######################################
query_temp=" AND (الرياض OR الجزيره OR استثمار OR هولندي OR فرنسي OR سـاب OR راجحي OR عربي OR سامبا OR الراجحي)"
query_list.append(query_temp)
query_temp=" AND (آستثمار OR الإستثمار OR الفرنسي OR العربي OR الهولندي OR جزيره OR لجين OR تصنيع OR نماء OR المجموعهة)"
query_list.append(query_temp)
query_temp=" AND (البلاد OR انماء OR كيمانول OR بتروكيم OR سافكو OR نما OR التصنيع OR اللجين OR نماء OR المجموعه)"
query_list.append(query_temp)
query_temp=" AND (الصحراء OR ينساب OR سبكيم OR المتقدمه OR كيان OR المتقدمة OR الصحرا OR حائل OR نجران OR مجموعه)"
query_list.append(query_temp)
query_temp=" AND (الشماليه OR اليمامه OR القصيم OR الجنوبيه OR ينبع OR الشرقيه OR تبوك OR الجوف OR العثيم OR المواسا)"
query_list.append(query_temp)
query_temp=" AND (المواساة OR الشرقية OR شرقية OR شرقيه OR الجنوبية OR اليمامة OR الشمالية OR مجموعة )"
query_list.append(query_temp)
query_temp=" AND (إكسترا OR دلة OR الصحيه OR رعايه OR ساسكو OR ثمار OR فتيحي OR جرير OR الدريس OR الحكير)"
query_list.append(query_temp)
query_temp=" AND (انعام OR غذائيه OR كهرباء OR تصنيع OR اكسترا OR للتنمية OR الزراعية OR الأسماك OR الاسماك OR تموين)"
query_list.append(query_temp)
query_temp=" AND (للتدريب OR الغاز OR التصنيع OR كهربا OR صافولا OR الغذائيه OR سدافكو OR المراعي OR أنعام OR حلواني)"
query_list.append(query_temp)
query_temp=" AND (هرفي OR التموين OR نادك OR الزراعيه OR تبوك OR أسماك OR للتنميه OR الجوف OR بيشه OR جازان)"
query_list.append(query_temp)
query_temp=" AND (بيشة OR اليانز OR التعاونية OR المتكامله OR انماء OR نماء OR سلامة OR اعاده OR أعاده OR المتحدة)"
query_list.append(query_temp)
query_temp=" AND (الاتصالات OR اتحاد OR زين OR عذيب OR المتكاملة OR التعاونيه OR ملاذ OR الأتصالات OR ميدغلف OR أليانز)"
query_list.append(query_temp)
query_temp=" AND (سلامه OR ولاء OR الدرع OR تكافل OR سند OR إنماء OR سايكو OR وفا OR إتحاد OR اتحاد)"
query_list.append(query_temp)
query_temp=" AND (الأهلي OR تكافل OR أسيج OR اسيج OR التجاري OR صقر OR المتحده OR إعادة OR اعادة OR بوبا)"
query_list.append(query_temp)
query_temp=" AND (الاهلي OR امانه OR المتطورة OR الاحساء OR الباحة OR المملكة OR صادرات OR بابطين OR بابطين OR أميانتيت)"
query_list.append(query_temp)
query_temp=" AND (وقايه OR ايس OR اكسا OR الخليجيه OR بروج OR العالميه OR سوليدرتي OR سوسو OR أمانه OR عنايه)"
query_list.append(query_temp)
query_temp=" AND (تكوين OR المملكه OR اكسترا OR الباحه OR عسير OR سيسكو OR الاحسا OR المتطوره OR المصافي OR انما)"
query_list.append(query_temp)
query_temp=" AND (زجاج OR الدوائيه OR شاكر OR السريع OR استرا OR أسترا OR معادن OR الدوائية OR معدنية OR معدنيه)"
query_list.append(query_temp)
query_temp=" AND (انابيب OR أنابيب OR المعجل OR اسلاك OR أسلاك OR الصادرات OR الكيميائية OR الورق OR الكيميائيه OR فيبكو)"
query_list.append(query_temp)
query_temp=" AND (البابطين OR الزامل OR انابيب OR أنابيب OR اميانتيت OR صدق OR كابلات OR الجبس OR الخزف OR الخضري)"
query_list.append(query_temp)
query_temp=" AND (طيبة OR العقارية OR إعمار OR التعمير OR مكه OR طيبه OR العقاريه OR مكة OR مسك OR الفخاريه)"
query_list.append(query_temp)
query_temp=" AND (الطيار OR تهامة OR الأبحاث OR تهامه OR بدجت OR مبرد OR بحري OR البحري OR المعرفه OR الابحاث)"
query_list.append(query_temp)
query_temp=" AND (أسمنت OR سمنت OR اسمنت OR الفخارية OR اعمار OR خضري OR الكابلات OR 2010 OR شمس OR الفنادق)"
query_list.append(query_temp)
query_temp=" AND (تأمين OR تامين OR تاسي OR ﺪﻠﻫ OR ﺮﻋﺎﻳﺓ OR اسلاك )"
query_list.append(query_temp)
query_temp=" AND (لتدريب+الخليج OR المعرفه+مدينه OR المعرفة+مدينه OR المعرفه+مدينة OR المعرفة+مدينة)"
query_list.append(query_temp)
query_temp=" AND (رابغ+بترو OR اللطيف+عبد OR الجماعي+النقل OR الجماعي+نقل OR عمر+جبل)"
query_list.append(query_temp)
query_temp=" AND (الأركان+دار OR الاركان+دار OR وتغليف+طباعه OR وتغليف+طباعة OR سى+بى)"
query_list.append(query_temp)
query_temp=" AND (الأحمر+البحر OR الاحمر+البحر OR والتسويق+الأبحاث OR والتسويق+الابحاث)"
query_list.append(query_temp)

##########################################
##### Matrix 2
##########################################
query_temp=" AND (سهم OR اسهم OR أسهم OR تداول OR ارتفع OR ارتفاع OR انخفض OR انخفاض OR هدف )"
query_list.append(query_temp)
query_temp=" AND (احمر OR الايجابيه OR أحمر OR حركة OR رأس  OR نمو OR فني OR متماسك OR نجح OR توصياتي)"
query_list.append(query_temp)
query_temp=" AND (اختراق OR التذبذب OR أعلى OR حلال OR ربح OR هامش OR فني  OR محور OR نذل OR توصيتنا)"
query_list.append(query_temp)
query_temp=" AND (اختراقة OR التوصيه OR أكتتاب OR حمراء OR رجع OR هنت OR فيبو OR مركات OR نزل OR توصيه)"
query_list.append(query_temp)
query_temp=" AND (اختراقه OR الحركة OR باغلاق OR خبر OR رش OR وقف OR قفال OR مسار OR نصب OR جمع)"
query_list.append(query_temp)
query_temp=" AND (اخضر OR الطلوع OR تجاوز OR خرج OR ريال OR ومتوقع OR قفل OR مشتراي OR نصبه OR جني)"
query_list.append(query_temp)
query_temp=" AND (ادني OR الغزال OR تحذير OR خروج OR سريع OR يتفاعل OR قمم OR مشتري OR نقاط OR حذارى)"
query_list.append(query_temp)
query_temp=" AND (ارباح OR الفائد OR تحسن OR خسائر OR سعر OR يحافظ OR قوي OR مضارب OR نقطة OR حذرت)"
query_list.append(query_temp)
query_temp=" AND (ارتداد OR الفني OR تحليل OR خسران OR سهم OR يخاف OR قيمته OR مضاربه OR نقطه OR حرام)"
query_list.append(query_temp)
query_temp=" AND (اعلى OR الكميات OR تداول OR خشاش OR سهمنا OR يرتد OR قيمته OR معلومة OR نقي OR حراميه)"
query_list.append(query_temp)
query_temp=" AND (اغلاق OR المسار OR تذبذب OR خضراء OR شارت OR يسال OR كابيتال OR معلومه OR طلوع OR حرك)"
query_list.append(query_temp)
query_temp=" AND (اقفال OR انعكاس OR ترويج OR خفيف OR شال OR يسأل OR كاسب OR مقاومة OR عرض OR موجه)"
query_list.append(query_temp)
query_temp=" AND (اكتتاب OR انهيار OR تصحيح OR دخل OR شراء OR يسألون OR كسر OR مقاومه OR عروض OR مؤكد)"
query_list.append(query_temp)
query_temp=" AND (توصي OR ايجابي OR تصرف OR دخلنا OR شيل OR يستهدف OR كسر OR ممتاز OR غزال OR مؤكده)"
query_list.append(query_temp)
query_temp=" AND (دوجي OR ايجابية OR تصريف OR دخول OR صرف OR يستهدف OR كميات OR موجة OR لمحور OR نايم)"
query_list.append(query_temp)
query_temp=" AND (توزيع OR ايجابيه OR تقرير OR دعم OR صعود OR يطالبون OR كويس OR ينجح OR مبروك OR طلب)"
query_list.append(query_temp)
query_temp=" AND (إقفال OR إغلاق OR توزع OR دوجو OR ضغط OR يملك OR لاهنت OR ينزل OR متعلق OR راس )"
query_list.append(query_temp)
query_temp=" AND (الرهان+فرس OR ﺪﻌﻣ OR ﺍﺮﺗﺩﺍﺩ OR ﻦﺴﺑﺓ OR احتيال OR غش OR تدليس OR تلاعب OR المضاربين OR تداولات )"
query_list.append(query_temp)
#query_temp="1010 AND (الرياض OR بنك)"
#query_list.append(query_temp)

query_temp=" AND (ﺲﻬﻣ OR ﺎﺴﻬﻣ OR ﺄﺴﻬﻣ OR ﺕﺩﺍﻮﻟ OR ﺍﺮﺘﻔﻋ OR ﺍﺮﺘﻓﺎﻋ OR ﺎﻨﺨﻔﺿ OR ﺎﻨﺨﻓﺎﺿ OR ﻩﺪﻓ OR ﺪﻌﻣ OR ﺍﺮﺗﺩﺍﺩ OR ﻦﺴﺑﺓ OR % OR %)"
query_list.append(query_temp)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


#global counter
counter = 0

#def runSearch(que):
def runSearch(que,stock,parent):
    #print("###########################################################################" + que);
    global counter
    counter += 1
    print(counter)
    #print(que)

    if is_number(que):
        temp = twitter.show_status(id=que)
        twittes = {}
        twittes['statuses']=[temp]
    else:
        twittes = twitter.search(q=que, result_type='recent', show_all_inline_media='true')

    for tweet in twittes['statuses']:
        try:
            item = Opinion()
            item.twitter_id = tweet['id_str']
            item.user_id = tweet['user']['id']
            item.text = tweet['text']
            item.created_at = tweet['created_at']
            item.user_followers_count = tweet['user']['followers_count']
            item.user_profile_image_url = tweet['user']['profile_image_url']
            item.media_url = tweet['entities']
            item.tweeter_sname = tweet['user']['screen_name']
            item.tweeter_name = tweet['user']['name']
            item.pub_date = timezone.now()
            item.stock = stock
            item.source = "twitter.com"
            item.labeled = False
            print("--------")
            print(item.text)
            if ' ﺰﺑ ' in tweet['text'] or ' ﻂﻳﺯ ' in tweet['text'] or ' ﻂﻴﻇ ' in tweet['text'] or 'ﺲﻜﺳ' in tweet['text'] or 'ﺲﻜﺴﻳ' in tweet['text'] or ' ﺲﺣﺎﻗ ' in tweet['text'] or ' ﺞﻨﺳ ' in tweet['text'] or ' ﺏﺯ ' in tweet['text'] or 'ﺏﺯﺍﺯ' in tweet['text'] or ' ﻂﻳﺯ ' in tweet['text'] or ' ﻂﻳﺯ ' in tweet['text'] or ' ﻂﻳﺯ ' in tweet['text'] or ' ﻚﺳ ' in tweet['text'] or ' ﻒﺤﻟ ' in tweet['text'] or ' ﻒﺣﻮﻠﻫ ' in tweet['text'] or ' ﺬﺑ ' in tweet['text'] or ' نيك ' in tweet['text'] or 'شرموط' in tweet['text'] or ' ناك ' in tweet['text'] or 'تتناك' in tweet['text'] or 'نياك' in tweet['text'] or 'زبر' in tweet['text'] or ' نيك' in tweet['text'] or ' كسه' in tweet['text']:
                print("naughty"+tweet['text'])
            else:
                if tweet['in_reply_to_status_id'] != None:
                    time.sleep(9)
                    item.conversation_reply = tweet['in_reply_to_status_id']
                    d = threading.Thread(target=runSearch,args=(tweet['in_reply_to_status_id'],stock,item.twitter_id))
                    d.start()
                item.save()
                if parent != '':
                    item = Opinion.objects.filter(twitter_id = que,stock = stock)[0]
                    item.similarId = parent
                    item.save()
        except: 
            pass  



from twython import Twython
twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")
#f_in = open('..//TwitterCrawler//stocks.txt', 'r', encoding='utf-8')
#lines = f_in.readlines()

while True:
    print("startt:" + str(datetime.datetime.now()) )
    for line in stock_list:
        fullname=full_name[line]
        try:
            time.sleep(9)
            d = threading.Thread(target=runSearch,args=(fullname,line,''))
            d.start()        
        except:
            pass
        #item.stock = "test"
    for qo in query_list: 
        #line.strip()
        #line = line.replace(u'\ufeff', '')
        #line = line.replace(u'\n', '')
        #print(line[::-1])
        for line in stock_list:
            #print("before")
            #print(qo)
            if line in qo:
                break 
                #print("break££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££")
                #print(qo)
        #else:
            #print("not break")
            #print(qo)
            #line='ﺎﺴﺘﺜﻣﺍﺭ' 
            #line='ﺕﺎﺴﻳ'            ####################################### working
            #line='يسات'
            #combinations=synonyms[line[::-1]]
            #line='ﺕﺎﺴﻳ'
            #print(line)
            #line = str(line).encode('utf8')
            #print(line)
            #line='ﺕﺎﺴﻳ'
            #line = str(line).encode('utf8')
            #print(line)
            combinations=synonyms[line]
            #print(combinations)

            #remove adult content
            #naughty_words=" AND ( -ﺰﺑ -ﻂﻳﺯ -ﻂﻴﻇ -ﺲﻜﺳ -ﺲﻜﺴﻳ -ﺲﺣﺎﻗ -ﺞﻨﺳ -ﻦﻴﻛ -ﺞﻨﺳ -ﺏﺯ -ﺏﺯﺍﺯ -ﻚﺳ -ﻒﺤﻟ -ﻒﺣﻮﻠﻫ -ﺬﺑ )" 
            query = combinations + qo 
            #print(query)
            try:
                time.sleep(9)
                t = threading.Thread(target=runSearch,args=(query,line,''))
                t.start()
            except:
                pass

    print("End:" + str(datetime.datetime.now()) )
