if ! ps -fe | grep -v "grep" | grep --quiet -i "mysql -u root -px"
    then 
        export PYTHONPATH=/home/ubuntu/DjangoWebProject1_20150620
        export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
        cd /home/ubuntu/DjangoWebProject1_20150620
	mysql --host=kalamacom.cganvnnahixy.us-east-1.rds.amazonaws.com --port=3306 --user=root --password=kalamacom kalamacom < /home/ubuntu/DjangoWebProject1_20150620/daily_prices.sql > /home/ubuntu/DjangoWebProject1_20150620/daily_prices.out
fi
