export PYTHONPATH=/home/ubuntu/DjangoWebProject1_20150128/
export DJANGO_SETTINGS_MODULE=DjangoWebProject1.settings
cd /home/ubuntu/DjangoWebProject1_20150128/app
if ps -aux | grep -v grep | grep -iq c22a2d8721c1984835c31c0addeec098
        then
	kill -9 $(ps -aux | grep -i c22a2d8721c1984835c31c0addeec098 | grep -v grep | tr -s ' ' | cut -d" " -f2) 
fi
