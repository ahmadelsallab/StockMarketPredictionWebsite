if ! ps -fe | grep -v "grep" | grep --quiet -i "python3.4 relevancy_classify.py" 
    then 
        export PYTHONPATH=/project/DjangoWebProject1_20150924/
        export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
        cd /project/DjangoWebProject1_20150924
        nohup python3.4 relevancy_classify.py >> app/logs/relevancy_classify_$(date +"%Y%m%d").out 2>&1& 
fi
