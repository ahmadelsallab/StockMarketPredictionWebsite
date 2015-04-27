"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),
    url(r'^home', 'app.views.home', name='home'),
    url(r'^get_tweets', 'app.views.get_tweets', name='get_tweets'),
    url(r'^get_prices_line', 'app.views.get_prices_line', name='get_prices_line'),
    url(r'^get_prices_candle', 'app.views.get_prices_candle', name='get_prices_candle'),
    url(r'^get_stocks_weights', 'app.views.get_stocks_weights', name='get_stocks_weights'),
    url(r'^get_correction', 'app.views.get_correction', name='get_correction'),    
    url(r'^correction_sentiment', 'app.views.correction_sentiment', name='correction_sentiment'),
    url(r'^contact', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login', 'app.views.login_user', name='login'),
    url(r'^register', 'app.views.register', name='register'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),
    url(r'^news', 'app.views.news', name='news'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
