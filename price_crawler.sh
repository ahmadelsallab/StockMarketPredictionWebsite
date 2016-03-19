export PYTHONPATH=/project/DjangoWebProject1_20150924/
export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
cd /project/DjangoWebProject1_20150924/app
date >> /project/DjangoWebProject1_20150924/app/whenthepricecrawlerworks
if ps -aux | grep -v grep | grep -iq 9a533c5f87acfdb07a81eb9b9624ec08
        then
	kill -9 $(ps -aux | grep -i 9a533c5f87acfdb07a81eb9b9624ec08 | grep -v grep | tr -s ' ' | cut -d" " -f2) 
fi
/usr/bin/python3.4 /project/DjangoWebProject1_20150924/manage.py crontab run 9a533c5f87acfdb07a81eb9b9624ec08 >> logs/price_crawler_$(date +"%Y%m%d").out 2>&1&

