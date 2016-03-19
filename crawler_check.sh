if ! ps -fe | grep -v "grep" | grep --quiet -i "python3.4 crawl_thread.py" 
    then 
        export PYTHONPATH=/project/DjangoWebProject1_20150924/
        export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
        cd /project/DjangoWebProject1_20150924/app
        date >> whenitrestarts
        nohup python3.4 crawl_thread.py >> logs/crawl_thread$(date +"%Y%m%d").out 2>&1&
fi

