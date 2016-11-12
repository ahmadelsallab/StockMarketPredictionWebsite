export PYTHONPATH=/project/DjangoWebProject1_20150924/
export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
cd /project/DjangoWebProject1_20150924/app
date >> /project/DjangoWebProject1_20150924/app/whenthepricecrawlerworks
if ps -aux | grep -v grep | grep -iq ddf65cfe58864e143b3ea650d6df1a77 
        then
	kill -9 $(ps -aux | grep -i ddf65cfe58864e143b3ea650d6df1a77 | grep -v grep | tr -s ' ' | cut -d" " -f2) 
fi
/usr/bin/python3.4 /project/DjangoWebProject1_20150924/manage.py crontab run ddf65cfe58864e143b3ea650d6df1a77 >> logs/price_crawler_$(date +"%Y%m%d").out 2>&1&

