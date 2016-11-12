if ! ps -fe | grep -v "grep" | grep --quiet -i "python3.4 sentiment_train.py" 
    then 
        export PYTHONPATH=/project/DjangoWebProject1_20150924/
        export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
        cd /project/DjangoWebProject1_20150924
        nohup python3.4 sentiment_train.py >> app/logs/sentiment_train_$(date +"%Y%m%d").out 2>&1& 
	kill -9 $(ps -fe | grep -v "grep" | grep -i "python3.4 sentiment_classify.py" | tr -s ' ' | cut -d" " -f2) || /project/DjangoWebProject1_20150924/relevancy_classify.sh
fi
