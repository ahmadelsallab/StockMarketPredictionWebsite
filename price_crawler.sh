export PYTHONPATH=/home/ubuntu/DjangoWebProject1_20150620/
export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
cd /home/ubuntu/DjangoWebProject1_20150620/app
date >> /home/ubuntu/DjangoWebProject1_20150620/app/whenthepricecrawlerworks
if ps -aux | grep -v grep | grep -iq ad76d8d4de4f54e62583da4434440ceb
        then
	kill -9 $(ps -aux | grep -i ad76d8d4de4f54e62583da4434440ceb | grep -v grep | tr -s ' ' | cut -d" " -f2) 
fi
/usr/bin/python3.4 /home/ubuntu/DjangoWebProject1_20150620/manage.py crontab run ad76d8d4de4f54e62583da4434440ceb >> price_crawler.out
