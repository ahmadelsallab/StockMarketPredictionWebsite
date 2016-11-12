if [ ! -f /project/DjangoWebProject1_20150924/update_counter.lockfile ]
    then 
        touch /project/DjangoWebProject1_20150924/update_counter.lockfile
        export PYTHONPATH=/project/DjangoWebProject1_20150924
        export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
        cd /project/DjangoWebProject1_20150924/app
	time mysql -uroot -pDjango1.5 kalamacom < /project/DjangoWebProject1_20150924/update_counter.sql >> logs/update_counter$(date +"%Y%m%d").out 2>&1
        rm /project/DjangoWebProject1_20150924/update_counter.lockfile
fi
