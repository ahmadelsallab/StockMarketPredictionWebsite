if ! ps -fe | grep -v "grep" | grep --quiet -i "python3.4 crawl_thread.py" 
    then 
        export PYTHONPATH=/home/ubuntu/DjangoWebProject1_20150620/
        export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
        cd /home/ubuntu/DjangoWebProject1_20150620/app
        date >> whenitrestarts
        nohup python3.4 crawl_thread.py &
fi

