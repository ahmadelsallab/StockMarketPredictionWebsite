if ! ps -fe | grep -v "grep" | grep --quiet -i "python3.4 question_train.py" 
    then 
        export PYTHONPATH=/project/DjangoWebProject1_20150924/
        export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
        cd /project/DjangoWebProject1_20150924
        nohup python3.4 question_train.py >> app/logs/question_train_$(date +"%Y%m%d").out 2>&1& 
fi
