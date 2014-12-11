from django.conf.urls import url

from freeuser import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
]