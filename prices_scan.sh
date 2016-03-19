if ! ps -fe | grep -v "grep" | grep --quiet -i "python3.4 prices_scan.py" 
    then 
        export PYTHONPATH=/project/DjangoWebProject1_20150924/
        export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
        cd /project/DjangoWebProject1_20150924/app
        nohup python3.4 prices_scan.py > logs/prices_scan_$(date +"%Y%m%d").out 2>&1&
fi

