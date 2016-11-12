if ! ps -fe | grep -v "grep" | grep --quiet -i "mysql -u root -px"
    then 
        export PYTHONPATH=/project/DjangoWebProject1_20150924
        export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
        cd /project/DjangoWebProject1_20150924/app
	mysql -u root -pDjango1.5  kalamacom < /project/DjangoWebProject1_20150924/daily_prices.sql >> logs/daily_prices$(date +"%Y%m%d").out 2>&1 
fi
