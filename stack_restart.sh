export PYTHONPATH=/project/DjangoWebProject1_20150924
export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
service mysql restart
service apache2 restart
swapoff -a
swapon -a
/project/DjangoWebProject1_20150924/update_counter.sh
