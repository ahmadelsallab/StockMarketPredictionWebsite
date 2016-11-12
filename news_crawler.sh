export PYTHONPATH=/project/DjangoWebProject1_20150924/
export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
cd /project/DjangoWebProject1_20150924/app
if ps -aux | grep -v grep | grep -iq b4803a4dc8babd2abb565ba4c1567e42 
        then
	kill -9 $(ps -aux | grep -i b4803a4dc8babd2abb565ba4c1567e42 | grep -v grep | tr -s ' ' | cut -d" " -f2) 
fi
/usr/bin/python3.4 /project/DjangoWebProject1_20150924/manage.py crontab run b4803a4dc8babd2abb565ba4c1567e42 >> logs/news_crawler_$(date +"%Y%m%d").out 2>&1&

