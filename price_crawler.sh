export PYTHONPATH=/home/ubuntu/DjangoWebProject1_20150128/
export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
cd /home/ubuntu/DjangoWebProject1_20150128/app
if ps -aux | grep -v grep | grep -iq f12775be29bbcf5d99e532507dc1456c
        then
	kill -9 $(ps -aux | grep -i f12775be29bbcf5d99e532507dc1456c | grep -v grep | tr -s ' ' | cut -d" " -f2) 
fi
/usr/bin/python3.4 /home/ubuntu/DjangoWebProject1_20150128/manage.py crontab run f12775be29bbcf5d99e532507dc1456c >> price_crawler.out
